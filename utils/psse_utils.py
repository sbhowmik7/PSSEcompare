"""psse_utils: Contains functions that create references to each elements api access function
for the real,integral, complex and character field. Uses either caspy based accessor functions
or psspy based accessor function depending on wheter caspy crashes (crashes from v 33.0 to 33.8]
"""
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"

from itertools import groupby, izip, repeat, imap, ifilter
from operator import itemgetter
import os
import sys

# import app_settings (which sets up the rest of the paths).
try:
    import app_settings
except ImportError:
    this_dir = os.path.dirname(__file__)
    sys.path.append(os.path.join(this_dir,'..'))
    import app_settings

try:
    import psspy
except ImportError:
    # Bad magic number if importing from a non-compliant python/psse mix
    # This is ok as sometimes this fn is called from modules which don't
    # require a working psspy.
    pass

attr_type = itemgetter(0)
MAX_REAL_BUSNUM = 10e6

def subsystem_info(name, attributes, sid=-1, flags=None):
    """
    Returns requested attributes from the PSS(r)E subsystem API
    for the given subsystem id and subsystem element name.

    e.g. to retrieve bus attributes "NAME", "NUMBER" and "PU"

      subsystem_info('bus', ["NAME", "NUMBER", "PU"])

    where the 'bus' `name` argument comes from the original
    PSS(r)E subsystem API naming convention found in Chapter 8 of the
    PSS(r)E API.

    abusint  # bus
    amachint # mach
    aloadint # load

    Args:
      inservice [optional]: True (default) to list only information
         for in service elements;
      sid [optional]: list only information for elements in this
         subsystem id (-1, all elements by default).

    """
    if flags is None: flags = {}

    name = name.lower()
    gettypes = getattr(psspy, 'a%stypes' % name)
    apilookup = {
            'I': getattr(psspy, 'a%sint' % name),
            'R': getattr(psspy, 'a%sreal' % name),
            'X': getattr(psspy, 'a%scplx' % name),
            'C': getattr(psspy, 'a%schar' % name), }

    result = []
    ierr, attr_types = gettypes(attributes)

    for k, group in groupby(zip(attr_types, attributes), key=attr_type):
        func = apilookup[k]
        strings = list(zip(*group)[1])
        ierr, res = func(sid, string=strings, **flags)
        result.extend(res)

    return izip(*result)

def check_psse_version(line):
    "Only needed for raw files"
    ver ='33'
    spaceparse=line.split() # Read first line in raw file
    for wrd in spaceparse[2:]: # read 3rd item onwards
        if not wrd[0].isalpha():
            continue
        elif wrd[:2].isdigit():
             ver=wrd[:2]
             break
        else:
            tmp= wrd.split('-') # Assume defined as PSSE-XX.0
            if tmp[1][:2].isdigit():
                ver =tmp[1][:2]
                break

    return ver
    
#---------------------------------------------------------
# Caspy related.

def convert_complex(row_start, param_name):
    """
    Lots of the caspy return complex values as a simple tuple,
    or where there are multiple complex values it returns a long tuple.

    Returns a complex number i, j based on the starting index in the array

    e.g.

    (1,2,3,4) with index 2 becomes:
    complex(3,4)
    or with index 0:
    complex(1,2)

    the param_name is the name to take from the given case.
    """
    def row_to_complex(row):
        return complex(*row[row_start:row_start+2])
    return lambda case: map(row_to_complex, case[param_name])

def first_key(getter, keys):
    """
    Returns the value from the first matching key

    >>> d = {'LDSCALE': 10}
    >>> first_key(d.get, ['LDSCAL', 'LDSCALE'])
    10

    raises StopIteration exception if no matching keys exist.
    """
    return ifilter(None, imap(getter, keys)).next()

def convert_int(*param_names):
    return lambda case: map(int, first_key(case.get, param_names))

def dedupe(iter):
    "Removes duplicate items"
    seen_before = set()
    items = []
    for item in iter:
        if item in seen_before:
            continue
        else:
            seen_before.add(item)
        items.append(item)
    return items

def mimick_home_bus(param_name, home_bus):
    def substitute_home_bus(case):
        """
        If the requested param is zero, substitute in the home bus.
        Used for IREG whose default 0 really means use the immediate bus.
        """
        home_buses = case[home_bus]
        def param_or_home((i, value)):
            if value:
                return value
            return home_buses[i]

        return map(param_or_home, enumerate(case[param_name]))
    return substitute_home_bus

def default_if_equals(param_name, equalto, default):
    """
    if case[param_name] == equalto:
        return default
    else:
        return case[param_name]

    used to replace an integer 0 with twelve char space field.
    """
    def choice(value):
        if value == equalto:
            return default
        else:
            return value

    return lambda case: map(choice, case[param_name])

def sbase(fn_or_param_name):
    # we can accept another function or a parameter string.
    if isinstance(fn_or_param_name, basestring):
        func = lambda case: case[fn_or_param_name]
    else:
        func = fn_or_param_name

    def multiply_sbase(case):
        sbase = multiply_sbase._sbase
        return map(lambda x: x*sbase, func(case))
    return multiply_sbase

def get_column_number(index, param_name, default=None):
    """
    The one casepy tuple holds many PSSEAPI parameters.
    Return the index from the list of tuples as a column.
    """
    getitem = itemgetter(index)
    def default_getitem(row):
        try:
            return getitem(row)
        except IndexError:
            return default

    return lambda case: map(default_getitem, case[param_name])

notimplemented = object()

name_lu = {
    'load': 'lod',
    'fxshunt': 'fsh',
    'genbus': 'genbus',
    'tr3': 'tr3fix',
    'bus': 'bus',
    'brn': 'brnfix',
    'trn': 'trnfix',
    'wnd': 'wndfix',
    'mach': 'gen',
    'swsh': 'wsh'}

attr_lu = {
    'NUMBER': 'NUM',
    'lod': {
            # 'SCALE': convert_int('LDSCAL', 'LDSCALE'),
            'MVANOM': sbase(convert_complex(0, 'LOAD')),
            'ILNOM': sbase(convert_complex(2, 'LOAD')),
            'YLNOM': sbase(convert_complex(4, 'LOAD')),},
    'fsh': {
            'SHUNTNOM': sbase('SHUNT')},

    'bus': {
            'ANGLED': 'VA',
            'TYPE': 'IDE',
            'BASE': 'BASKV',
            'PU': 'VM',},

    # brn values.
    'FROMNUMBER': 'FRMBUS',
    'TONUMBER': 'TOBUS',
    'METERNUMBER': 'METBUS',
    'CHARGING': 'B',
    'FROMSHNT': 'GBI',
    'TOSHNT': 'GBJ',
    'LENGTH': 'LINLEN',
    'FRACT1': get_column_number(0, 'OWNPCT'),
    'FRACT2': get_column_number(1, 'OWNPCT'),
    'FRACT3': get_column_number(2, 'OWNPCT'),
    'FRACT4': get_column_number(3, 'OWNPCT'),
    'OWN1': get_column_number(0, 'OWNER'),
    'OWN2': get_column_number(1, 'OWNER'),
    'OWN3': get_column_number(2, 'OWNER'),
    'OWN4': get_column_number(3, 'OWNER'),

    'brnfix': {
            'STATUS': 'STAT',
            'ID': 'CKT',},

    'wndfix': {
            'WIND1NUMBER': 'BUS1ST',
            'WIND2NUMBER': 'BUS2ND',
            'WIND3NUMBER': 'BUS3RD',
            'ID': 'CKT',
            'NTPOSN': 'NTAPS',
            'ICONTNUMBER': 'CONBUS',
            'CODE': 'CNTL',
            'RATIO': 'WIND1',
            'NOMV': 'NOMV1',
            'SBASE': 'SBASE1',
            'ANGLE': 'ANG1',
            'COMPRX': 'XFRCMP',
    },

    'tr3fix': {
            'WIND1NUMBER': 'BUS1ST', 
            'WIND2NUMBER': 'BUS2ND', 
            'WIND3NUMBER': 'BUS3RD',
            'ID': 'CKT',
            'XFRNAME': 'TRNAME',
            'NMETERNUMBER':'NMETER',
            'CW': notimplemented,
            'CZ': notimplemented,
            'CM': notimplemented,
    },

    'trnfix': {
            'CODE': 'CNTL',
            'NTPOSN': 'NTAPS',
            # we create caspy's wind1number field in the trn fix.
            'WIND1NUMBER': 'WIND1NUMBER',

            'ICONTNUMBER': 'CONBUS',
            'COMPRX': 'XFRCMP',
            'CW': notimplemented,
            'CZ': notimplemented,
            'CM': notimplemented,
            'RXNOM': 'RXTRAN',
            'ID': 'CKT',
            'YMAG': 'GBI',
            'STATUS': 'STAT',
            'RATIO': 'WIND1',
            'RATIO2': 'WIND2',
            'ANGLE': 'ANG1',
            'XFRNAME': 'TRNAME',},

    'genbus': {
            'VSPU': 'VS',
            'IREG': mimick_home_bus('IREG', 'NUM'),},

    'gen': {
            'VSPU': 'VS',
            'ID': 'IDE',
            'STATUS': 'STAT',
            'PGEN': sbase('PG'),
            'QGEN': sbase('QG'),
            'PMAX': sbase('PT'),
            'PMIN': sbase('PB'),
            'QMAX': sbase('QT'),
            'QMIN': sbase('QB'),
            'GENTAP': 'GTAP',},
    'wsh': {
            'STEPSBLOCK1': get_column_number(0, 'NI', 0),
            'STEPSBLOCK2': get_column_number(1, 'NI', 0),
            'STEPSBLOCK3': get_column_number(2, 'NI', 0),
            'STEPSBLOCK4': get_column_number(3, 'NI', 0),
            'STEPSBLOCK5': get_column_number(4, 'NI', 0),
            'STEPSBLOCK6': get_column_number(5, 'NI', 0),
            'STEPSBLOCK7': get_column_number(6, 'NI', 0),
            'STEPSBLOCK8': get_column_number(7, 'NI', 0),
            'STEPSBLOCK9': get_column_number(8, 'NI', 0),
            'BSTPBLOCK1': sbase(get_column_number(0, 'BI', 0)),
            'BSTPBLOCK2': sbase(get_column_number(1, 'BI', 0)),
            'BSTPBLOCK3': sbase(get_column_number(2, 'BI', 0)),
            'BSTPBLOCK4': sbase(get_column_number(3, 'BI', 0)),
            'BSTPBLOCK5': sbase(get_column_number(4, 'BI', 0)),
            'BSTPBLOCK6': sbase(get_column_number(5, 'BI', 0)),
            'BSTPBLOCK7': sbase(get_column_number(6, 'BI', 0)),
            'BSTPBLOCK8': sbase(get_column_number(7, 'BI', 0)),
            'BSTPBLOCK9': sbase(get_column_number(8, 'BI', 0)),
            'MODE': 'MODSW',
            'STATUS': 'STAT',
            'IREG': 'SWREM',
            'ADJMETHOD': 'ADJM',
            'BSWNOM': sbase('BINIT'),

            # facts device name. stored in pssfct
            'VSCNAME': default_if_equals('RMINDX', 0, ' '*12)
    }

}

def remove_ierr(caseattr):
    headers, values = caseattr.keys(), caseattr.values()
    ierr = headers.index('IERR')
    del values[ierr]
    del headers[ierr]
    return headers, values

def fix_caspy_case(case):
    """
    There are numerous fixes to apply to the returned caspy
    case to make it 'sane'.

    - inject 'sbase' value into some of the lu functions.
    - brnfix will contain just branches.
    - trnfix will contain just two winding transformers.
    - tr3fix will contain just three winding transformers.
    - plant is shared with machine data, split plant into its own 'genbus'
    - strange buses with names like '~~~~' are removed

    oh and btw all of those will contain the complete set of parameters.
    Even if it means duplicating shared params from brn like for trnfix
    """
    caspy_info.case = case

    #--------------------------------------------------------
    # attach SBASE value to conversion functions.

    sbase = case.pssmsc['SBASE']
    needs_sbase = [('lod', 'MVANOM'),
                   ('lod', 'YLNOM'),
                   ('lod', 'ILNOM'),
                   ('gen', 'PGEN'),
                   ('gen', 'QGEN'),
                   ('gen', 'PMAX'),
                   ('gen', 'QMAX'),
                   ('gen', 'QMIN'),
                   ('gen', 'PMIN'),
                   ('fsh', 'SHUNTNOM'),
                   ('wsh', 'BSTPBLOCK1'),
                   ('wsh', 'BSTPBLOCK2'),
                   ('wsh', 'BSTPBLOCK3'),
                   ('wsh', 'BSTPBLOCK4'),
                   ('wsh', 'BSTPBLOCK5'),
                   ('wsh', 'BSTPBLOCK6'),
                   ('wsh', 'BSTPBLOCK7'),
                   ('wsh', 'BSTPBLOCK8'),
                   ('wsh', 'BSTPBLOCK9'),
                   ('wsh', 'BSWNOM')]
    for key, attr in needs_sbase:
        try:
            value = attr_lu[attr]
        except KeyError:
            value = attr_lu[key][attr]
        value._sbase = sbase

    #-------------------------------------------------------------
    # redistribute the brn and trn info into trnfix - all in once place.

    brn_param_names, brns = remove_ierr(case.pssbrn)

    brn_and_tx_values = zip(*brns)

    # lots of 'brn' are actually 'tx' just check 'indx2w' == 0
    indx2w = brn_param_names.index('INDX2W')
    brn_values = filter(lambda row: row[indx2w] == 0, brn_and_tx_values)
    case.pssbrnfix = dict(zip(brn_param_names, zip(*brn_values)))

    # tx values on the other hand have non zero indx2w
    just_tx_values = filter(itemgetter(indx2w), brn_and_tx_values)

    tx_param_names, trns = remove_ierr(case.psstrn)
    tx_and_tx3_values = zip(*trns)

    # PSSE sorts the from and to fields based on int(from) < int(to).
    # Winding 1 is set to the original FROM bus
    # (the FROM bus before PSSE reorders the from and to).

    brn_param_names.append('WIND1NUMBER')
    indxfrm = brn_param_names.index('FRMBUS')
    indxto = brn_param_names.index('TOBUS')

    def swap_from_to(row):
        """
        Swaps the from and to if the to is less than from.
        appends the original from bus to the end of the row
        which is being used as the wind1number field.
        """
        row = list(row)
        frm, to = row[indxfrm], row[indxto]
        # adding nthe wind1number field to equal the 'from' bus always.
        row.append(frm)

        if to < frm:
            row[indxfrm] = to
            row[indxto] = frm

        return tuple(row)
    just_tx_values = map(swap_from_to, just_tx_values)

    indx3w = tx_param_names.index('INDX3W')

    # now for each tx (both 2 and 3 winding) grab the tx2 values
    # and tack them on to the brns.
    tx_records = [] 
    wnd_records = []

    for record in just_tx_values:

        tx2_record = tx_and_tx3_values[record[indx2w] - 1]
        if tx2_record[indx3w] > 0:
            wnd_records.append(record + tx2_record)
            continue

        tx_records.append(record + tx2_record)

    tx_headers = brn_param_names + tx_param_names
    case.psstrnfix = dict(zip(tx_headers, zip(*tx_records)))
    #-----------------
    # three winding transformer windings.
    wnd_param_names, wnds = remove_ierr(case.pss3wt)
    wnd_param_names.append('WNDNUM')

    indx3w = tx_headers.index('INDX3W')
    index = wnd_param_names.index
    bus1, bus2, bus3 = index('BUS1ST'), index('BUS2ND'), index('BUS3RD')
    wind1num = tx_headers.index('WIND1NUMBER')

    tx3_values = zip(*wnds)
    tx3s = []
    for record in wnd_records:
        wnd_record = tx3_values[record[indx3w] - 1]

        # calculate the wndnum by checking this branch's wind1number against
        # the bus1 bus2 and bu3 listed in the winding field.
        wndnum_lu = {wnd_record[bus1]: 1,
                     wnd_record[bus2]: 2,
                     wnd_record[bus3]: 3}
        wndnum = wndnum_lu[record[wind1num]]

        tx3s.append(record + wnd_record + (wndnum,))

    tx3_headers = tx_headers + wnd_param_names
    case.psswndfix = dict(zip(tx3_headers, zip(*tx3s)))

    #-----------------------------------------
    # tr3 transformers (not windings). One record per tranformer
    # it is a  mashup between windings, branches and transformer records.
    bus_param_names, bus_values = remove_ierr(case.pssbus)
    buses = zip(*bus_values)
    busnum = itemgetter(bus_param_names.index("NUM"))
    bus_lu = dict([(busnum(row), row) for row in buses])
    
    tr3_names, tr3s = remove_ierr(case.pss3ix)
    tr3_values = zip(*(wnds + tr3s))

    additional_names = ['RX1-2NOM', 'RX2-3NOM', 'RX3-1NOM',
                        'SBASE1-2', 'SBASE2-3', 'SBASE3-1',
                        'VMSTAR', 'ANSTAR', 'YMAG']
    tr3_param_names = (
        wnd_param_names[:-1] + # ignore fake WNDNUM column
        tr3_names +
        brn_param_names[:-1] + # ignore fake WIND1NUMBER column
        additional_names)

    indx_first_branch = tr3_param_names.index('IDX1BR')
    indx_second_branch = tr3_param_names.index('IDX2BR')
    indx_third_branch = tr3_param_names.index('IDX3BR')
    indx_star = tr3_param_names.index('BUSSTAR')

    indx_rx = brn_param_names.index('RX')
    indx_ymag = brn_param_names.index('GBI')

    indx_sbase = tx_param_names.index('SBASE1')

    indx_vmstar = bus_param_names.index('VM')
    indx_angstar = bus_param_names.index('VA')

    tr3s = []

    for record in tr3_values:
        tr3_first_brn = brn_and_tx_values[record[indx_first_branch] - 1]
        tr3_second_brn = brn_and_tx_values[record[indx_second_branch] - 1]
        tr3_third_brn = brn_and_tx_values[record[indx_third_branch] - 1]

        rx1 = tr3_first_brn[indx_rx]
        rx2 = tr3_second_brn[indx_rx]
        rx3 = tr3_third_brn[indx_rx]

        rx = (rx1 + rx2, rx2 + rx3, rx3 + rx1)

        tr3_first_tx = tx_and_tx3_values[tr3_first_brn[indx2w] - 1]
        tr3_second_tx = tx_and_tx3_values[tr3_second_brn[indx2w] - 1]
        tr3_third_tx = tx_and_tx3_values[tr3_third_brn[indx2w] - 1]

        sbase1 = tr3_first_tx[indx_sbase]
        sbase2 = tr3_second_tx[indx_sbase]
        sbase3 = tr3_third_tx[indx_sbase]

        sbase = (sbase1, sbase2, sbase3)

        starbus_num = record[indx_star]
        starbus = bus_lu[starbus_num]
        star_vals = (starbus[indx_vmstar], starbus[indx_angstar])

        ymag = (tr3_first_brn[indx_ymag],)

        tr3s.append(record + tr3_first_brn + rx + sbase + star_vals + ymag)

    case.psstr3fix = dict(zip(tr3_param_names, zip(*tr3s)))

    #-----------------
    # pssgen contains mach and genbus, meaning duplicates when querying for genbus
    # if there there is more than one machine at a bus.
    gen_param_names, gen_values = remove_ierr(case.pssgen)

    genbus_param_names = ['NUM', 'IREG', 'VS', 'RMPCT']

    keep_indexes = map(gen_param_names.index, genbus_param_names)
    genbus_values = map(gen_values.__getitem__, keep_indexes)

    # transpose into rows, deduplicate, transpose back to columns.
    genbus_dedupe = zip(*dedupe(zip(*genbus_values)))

    case.pssgenbus = dict(zip(genbus_param_names, genbus_dedupe))

    #----------------------------------------------------------------
    # clean crappily named '~~~~~~~~~~' buses from the caspy results.
    # their buse numbers all exceed 10000000.


    realbuses = filter(lambda row: busnum(row) < MAX_REAL_BUSNUM, buses)
    case.pssbus = dict(zip(bus_param_names, zip(*realbuses)))



def caspy_info(gname, params, sid=-1, flags=None):
    """
    A subsystem_info implementation that uses caspy instead of subsystem data
    retrieval api.
    TODO: Not yet feature complete with the subsystem_info function.
    """
    try:
        name = name_lu[gname]
    except KeyError:
        msg = 'No caspy translation implemented for %s' % name
        raise NotImplementedError(msg)

    case = getattr(caspy_info, 'case')
    datastore = getattr(case, 'pss' + name)
    if not datastore:
        return [() for param in params]

    columns = []
    for param in params:
        caspy_param = attr_lu[name].get(param, attr_lu.get(param, param))

        # silently replace not implemented params with an array of None.
        if caspy_param is notimplemented:
            columns.append(repeat(None))
            continue

        if callable(caspy_param):
            get_param = caspy_param
        else:
            get_param = itemgetter(caspy_param)
        try:
            columns.append(get_param(datastore))
        except:
            print 'Error: Unknown attibute %s in %s'%(str(caspy_param),gname)
            #TODO check

    return zip(*columns)

