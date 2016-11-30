"""brn: element branch
"""
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"

from collections import defaultdict
import os.path
import sys
from textwrap import dedent

# import app_settings (which sets up the rest of the paths).
try:
    import app_settings
except ImportError:
    this_dir = os.path.dirname(__file__)
    sys.path.append(os.path.join(this_dir,'..'))
    import app_settings

# import Grid Compare modules.
from collections import OrderedDict
from psse_utils import caspy_info

try:
    from psse_utils import subsystem_info
except ImportError:
    sys.path.append(app_settings.UTILS_DIR)
    from psse_utils import subsystem_info

def make_param_dict(param_list):
    param_dict = OrderedDict()
    for param in param_list:
        if param.name in param_dict:
            raise Exception(dedent("""\
                    Read parameter name conflict for "%s".
                        Make sure there is no repeated names in the parameter
                        definitions. If there is a conflict, use the type that
                        is returned from a "psspy.a*types" call for that
                        parameter name."""
                        % (param.name,)))
        else:
            param_dict[param.name] = param
    return param_dict

# Functions to retrieve the real or imaginary components from a cplx attr
def get_real(cplx_str):
    try:
        return complex(cplx_str).real
    except TypeError:
        return 0

def get_imag(cplx_str):
    try:
        return complex(cplx_str).imag
    except TypeError:
        return 0

class Parameter(object):
    """This object holds meta info for one parameter of an element,
    ie. TYPE parameter for the BUS element.

    The input data is:
        data_type: Although probably not often used, this is the data type of
            this parameter.
        display_name: The pretty name you want displayed for human consumption.
            Get this data from the best description found in the POM, PSSEAPI
            read fn or PSSEAPI write fn. (falls back to one of the other names)
        description: The best description found from either the POM, PSSEAPI
            read fn or PSSEAPI write fn. (Read and write, if significantly
            different.)
    """

    def __init__(self, name, data_type=None, display_name=None,
            description=None):

        self.name = name
        self.data_type = data_type
        self.display_name = display_name
        self.description = description

    def dump_string(self):
        # get all defined attributes for this object
        attr = [x for x in dir(self) if not x.endswith('__')]
        # create a attr='val' string for each attr
        attr_eq_val = ["%s='%s'" % (x, self.__getattribute__(x))
                for x in attr if isinstance(self.__getattribute__(x), str)]
        # join and return
        return ', '.join(attr_eq_val)


class ReadParam(Parameter):
    """This object holds meta info for one parameter of an element,
    ie. TYPE parameter for the BUS element.

    The input data is:
        read_name: The name used to specify this parameter in the read_fn in
            the PSSEAPI.
        data_type: Although probably not often used, this is the data type of
            this parameter.
        read_fn_key: The identifying string of characters used in the subsystem
            data retrieval functions for this element type.
        read_fn: The function used to read this parameter.
        display_name: The pretty name you want displayed for human consumption.
            Get this data from the best description found in the POM, PSSEAPI
            read fn or PSSEAPI write fn. (falls back to one of the other names)
        description: The best description found from either the POM, PSSEAPI
            read fn or PSSEAPI write fn. (Read and write, if significantly
            different.)

    The other data that may be written to:
        write_fn: The function which is used to change this variable. This
            value is only set when processed by the encompassing 'element'
            object.
    """
    def __init__(self, name, data_type=None, read_fn_key=None,
            read_fn=None, display_name=None, description=None, base_param=None):

        if base_param:
            # used keyword in preference to base_param value.
            super(ReadParam, self).__init__(
                    name=name,
                    data_type=(data_type or base_param.data_type),
                    display_name=(display_name or base_param.display_name),
                    description=(description or base_param.description))
        else:
            super(ReadParam, self).__init__(
                    name=name,
                    data_type=data_type,
                    display_name=display_name ,
                    description=description)

        self.read_fn_key = read_fn_key
        self.read_fn = read_fn
        # This is the second time self.read_fn is defined in the init. This is
        # to aid in debugging. The first definition is so 'dump_string' can
        # access the value passed in if there is an error.
        self.read_fn = self.initial_get_read_fn(read_fn_key, data_type,
                read_fn)

    def initial_get_read_fn(self, read_fn_key, data_type, read_fn):
        if read_fn_key and data_type:
            derived_read_fn = self.derive_read_fn(read_fn_key, data_type)
            # Check to make sure that this matches the supplied fn, if given.
            if read_fn and (read_fn != derived_read_fn):
                raise Exception("Mismatch of read_fn names.\n"
                    "Only specify the read_fn_key if this string can be\n"
                    "used to derive the read_fn, eg:\n"
                    "    read_fn_key='bus' and data_type='int'\n"
                    "       ==> 'abusint'\n"
                    "If you have done this, perhaps you have a spelling\n"
                    "mistake.\n"
                    "param vals: %s" % (self.dump_string(),)
                    )
            else:
                # no self.read_fn set
                return derived_read_fn
        else:
            # Until I find a parameter that is write only, read_fn cannot
            # be None
            if not read_fn:
                raise Exception("No read function defined for parameter:\n"
                        "    %s" % (self.dump_string(),))
            return read_fn

    def derive_read_fn(self, read_fn_key, data_type):
        return "a%s%s" % (read_fn_key, data_type)

class WriteParam(Parameter):
    """This object holds meta info for one parameter of an element,
    ie. TYPE parameter for the BUS element.

    The input data is:
        name: The name of this parameter.
        trns_fn: The function used to convert the value read in, to the value
            require by the writing function.
        read_param: The parameter that reads the value from the PSSE case.
        data_type: Although probably not often used, this is the data type of
            this parameter.
        display_name: The pretty name you want displayed for human consumption.
            Get this data from the best description found in the POM, PSSEAPI
            read fn or PSSEAPI write fn. (falls back to one of the other names)
        description: The best description found from either the POM, PSSEAPI
            read fn or PSSEAPI write fn. (Read and write, if significantly
            different.)
   """
    def __init__(self, name, read_param, trns_fn=None, data_type=None,
            display_name=None, description=None, base_param=None):

        if base_param:
            # used keyword in preference to base_param value.
            super(WriteParam, self).__init__(
                    name=name,
                    data_type=(data_type or base_param.data_type),
                    display_name=(display_name or base_param.display_name),
                    description=(description or base_param.description))
        else:
            super(WriteParam, self).__init__(
                    name=name,
                    data_type=data_type,
                    display_name=display_name ,
                    description=description)

        self.read_param = read_param
        self.trns_fn = trns_fn

        self.write_fn = None


class PSSE_Fn(object):
    def __init__(self, name, prim_ordered_dict, write_ordered_dict):
        self.name = name

        self.primaries = prim_ordered_dict
        self.primary_str = self.make_primary_str()

        self.writables = write_ordered_dict
        self.unique_writables = self.make_element_unique_name_dict()

        self.add_fnname_to_params()

        self.writeable_order = dict((option, index)
                for index, option in enumerate(self.unique_writables.keys()))


    def add_fnname_to_params(self):
        """Add a reference to the name of the parent function to the
        parameter."""

        for param in self.writables.values():
            param.write_fn = self.name

    def make_element_unique_name_dict(self):
        """Returns an ordered dict that points to the same objects as
        'writables', but has its key prepended with the name of the function.

        Some PSSE elements have more than one function to write data to. This
        makes a unique name that can be passed back to the Element class to
        refer to the correct writing function."""

        unique_names = OrderedDict()
        for k, v in self.writables.items():
            unique_names['%s__%s' % (self.name, k)] = v
        return unique_names

    def make_primary_str(self):
        """Return a string used to pass the keyword values into.

        We make the primary string seperately as the values for this may be
        passed in as the nodeid rather than keyword arguments.

        eg. say we need the ibus, jbus and ck, this function will return
        something like:
            'i=%s, j=%s, ck="%s"'
        so the values can be determined from the node value stored in the db
        and passed in.
        """
        def quote_or_not(keyword):
            if self.primaries[keyword].data_type == 'char':
                return '%s="%%s"' % (keyword,)
            return '%s=%%s' % (keyword,)
        keyword_args = map(quote_or_not, self.primaries.keys())
        return ', '.join(keyword_args)

    def get_keyword_vals_from_nodeid(self, nodeid):
        return tuple(nodeid.split('|'))

    def quote_or_not(self, arg_and_val):
            keyword, val = arg_and_val
            if self.writables[keyword].data_type == 'char':
                return '%s="%s"' % (keyword, val[-1])
            return '%s=%s' % (keyword, val[-1])

    def neat_write(self, fn, args, line_len=79, initial_indent='',
            subsequent_indent=''):

        lines = []

        cur_line = []
        cur_len = 0
        commas_and_space_len = 0

        new_line = True
        for arg in args:
            arg_len = len(arg)

            if ((not new_line) and
                    (cur_len + arg_len + 2 + commas_and_space_len > line_len)):
                # 2 is added for the comma and space required to join.
                cur_line[-1] = cur_line[-1] + ','
                lines.append(', '.join(cur_line))

                new_line = True

            if new_line:
                new_line = False
                cur_line = []
                # The number of commas is equal to the number of args.
                # The number of spaces is one less than number of commas.
                commas_and_space_len = 1

                # new line
                # add indents
                if not lines:
                    # First line
                    cur_len = len(fn) + len(initial_indent) + arg_len
                    cur_line.append('%s%s(%s' % (initial_indent, fn, arg))

                else:
                    cur_len = len(subsequent_indent) + arg_len
                    cur_line.append('%s%s' % (subsequent_indent, arg))

            else:
                # Continue current line.
                cur_len += arg_len
                cur_line.append(arg)
                commas_and_space_len += 2

        # finish last line.
        cur_line[-1] += ')'
        lines.append(', '.join(cur_line))

        return lines


    def write_psspy_cmd(self, nodeid, options=None, line_len=79,
            initial_indent='', subsequent_indent=''):
        cmd = 'psspy.%s' % (self.name,)
        primary = self.primary_str % self.get_keyword_vals_from_nodeid(nodeid)

        args = []
        if options:
            sorted_unique = sorted(options.keys(), key=self.writeable_order.get)
            sorted_args_and_vals = [(self.unique_writables[k].name, options[k])
                    for k in sorted_unique]

            args = map(self.quote_or_not, sorted_args_and_vals)
        args.insert(0,primary)

        return self.neat_write(cmd, args, line_len, initial_indent,
                subsequent_indent)


    # make some properties here to make getting unlisted data easier
    # ie. if grabbing display name, and it doesn't exist, return the read
    # name.

class Element(object):
    def __init__(self, elem_name, primaries, parameter_dict, slurp_flags,
            fn_list=None, del_fn=None):
        self.elem_name = elem_name
        self.parameter = parameter_dict

        self.primaries = primaries

        self.writables = OrderedDict()
        for fn in fn_list:
            self.writables.update(fn.unique_writables)

        self.write_fns = dict([(fn.name, fn) for fn in fn_list])

        self.del_fn = del_fn
        self.slurp_flags = slurp_flags

    def __repr__(self):
        return '%s, %s, %s, %s' % (
            self.elem_name,
            str(self.parameter.keys()),
            str(self.primaries),
            str(self.writables.keys()))

    def required_writables(self):
        """Return a list of the required writable options"""
        return self.writables.keys()

    def required_readables(self):
        """Return a list of the required readable options.

        This includes the primaries at the start of the returned list, in the
        order they are required in and the readable names of the writable
        options at the end."""
        readables = list(self.primaries)
        for option in self.required_writables():
            if option not in readables:
                readables.append(self.writables[option].read_param)
        return readables

    def _slurp(self, req_read_names, sid=-1, flags=None):
        """Return a iterator of the slurped data"""
        if not flags:
            flags = self.slurp_flags

        if app_settings.USE_CASPY:
            return caspy_info(self.elem_name, req_read_names, sid=sid,flags=flags)
        else:
            return subsystem_info(self.elem_name, req_read_names, sid=sid,
                                flags=flags)

    slurp = _slurp

    def needs_transform(self, options):
        for opt in options:
            if self.writables[opt].trns_fn:
                return True

    def map_func(self, read_opts, options):
        if self.needs_transform(options):
            trns = [self.writables[opt_name].trns_fn for opt_name in options]
            def transform(vals):
                return [trns_fn(val) if trns_fn else val
                        for trns_fn, val in zip(trns, vals)]

            if len(read_opts) == len(options):
                # just transform the data:
                def zipper(options, vals):
                    return zip(options, transform(vals))
            else:
                # Some read data needs to be added.
                val_ind = [read_opts.index(self.writables[opt_name].read_param)
                        for opt_name in options]

                def zipper(options, vals):
                    return zip(options,
                            transform([vals[ind] for ind in val_ind]))

            return zipper

        elif len(read_opts) != len(options):
            # Some read data needs to be added.
            val_ind = [read_opts.index(self.writables[opt_name].read_param)
                    for opt_name in options]

            def zipper(options, vals):
                return zip(options, [vals[ind] for ind in val_ind])

            return zipper
        else:
            # just a regular zipping of files.
            return zip

class tr3_Elem(Element):
    def get_sbases(self, sid):
        from wnd import wnd_elem
        # slurp 'WIND1NUMBER','WIND2NUMBER','WIND3NUMBER','ID', 'WNDNUM',
        # 'SBASE'
        wnd_slurp = wnd_elem.slurp(['WIND1NUMBER','WIND2NUMBER','WIND3NUMBER',
            'ID', 'WNDNUM','SBASE'], sid)
        if not wnd_slurp:
            return {}
        # compile 'WIND1NUMBER','WIND2NUMBER','WIND3NUMBER','ID' into nodeid

        sb_ind = {1:'SBASE1-2',2:'SBASE2-3',3:'SBASE3-1'}
        sbases = defaultdict(dict)
        for row in wnd_slurp:
            node = '|'.join([str(x) for x in row[:4]])
            sbases[node][sb_ind[row[4]]] = row[5]
        return sbases

    def slurp(self, req_read_names, sid=-1, flags=None):
        if not flags:
            flags = self.slurp_flags

        req_read_copy = req_read_names[:]
        sbase_loc = {'SBASE1-2':None,'SBASE2-3':None,'SBASE3-1':None}
        for sbase in sbase_loc.keys():
            if sbase in req_read_names:
                sbase_loc[sbase] = req_read_names.index(sbase)
                req_read_copy.remove(sbase)

        norm_slurp = self._slurp(req_read_copy, sid, flags)
        if any(norm_slurp):
            if len(req_read_copy) != len(req_read_names):
                sbases_dict = self.get_sbases(sid)
                sorted_keys = sorted(sbase_loc.keys(), key=sbase_loc.get)

                for row in norm_slurp:
                    # put sbase back into where they were taken from
                    row = list(row)
                    node = '|'.join([str(x) for x in row[:4]])
                    for k in sorted_keys:
                        # only if they were requested.
                        if sbase_loc[k]:
                            try:
                                row.insert(sbase_loc[k], sbases_dict[node][k])
                            except KeyError:
                                print('Error while getting data for %s node %s'%(k,node))
                                raise
                    yield row
            else:
                # yield another iterator once!?!
                yield norm_slurp

