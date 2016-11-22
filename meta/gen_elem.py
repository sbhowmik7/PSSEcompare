"""gen_elem: generates the element definition file (elem_name.py) from an
outline file for that element. The purpose of the outline file is to be able to
get a clear overview of the element in a short number of lines. The final
description file is spaced out a lot more.

The final description file has several pieces of data which still require data
to be added to them. These are the additional peices of information such as the
display name and the description. An empty place holder (which doesn't cause
any exceptions) are inserted for these fields.

The required fields in the outline file are:
    elem_name: The name of the element.
    elem_primaries: A tuple (in the order you want them concatenated for
        nodeid) of the read names that uniquely identify an element.
    COMMON_READ_FN_KEY: The common string for all the subsystem retrieval
        functions. ie. for abusint, abuxcplx, etc it would be 'bus'
    read_dict: A dict of all the read_names in the subsystem data retrieval
        fns. The keys of the dict are the data_types which correspond to a list
        of all the read names for that data_type.
    write_fns: A dictionary for all the write names for all the functions.
        The dict is arranged with the function name being the keys. This points
        to another dictionary with the keys 'primaries' and 'writables'. These
        keys point to a list of keyword dictionaries that define the parameter.
        The keyword dictionaries have the following keys:
            name: the keyword used in the function signature.
            read_name: the name of the parameter in the subsystem data
                retrieval which corresponds to this keyword.
            trns_fn: a string containing the function to extract the necessary
                data for this keyword from the data returned by the subsystem
                data retrieval.
            data_type: data type is usually taken from the read_name's
                datatype. But if a different data type is required for this
                parameter, override it with this keyword.

    Optional:
        additional_imports: A string with addition lines to be added to the
            start of the file.
        special_elem_class: Specify the class of the element if it is to be
            different from 'Element'.
        derived_reads: Similar to 'read_dict'. Parameter names to be used to
            read data, but these are used as place holders for another routine
            to actually get the data. Requires the use of a
            'special_elem_class'. See tr3_Elem for an example.
    """
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"


import textwrap
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))

import app_settings

import psspy
psspy.throwPsseExceptions = True

# Four spaces
indent = '    '

# All the imports required for the definition file.
common_imports = textwrap.dedent("""\
        import textwrap
        from elem_obj import ReadParam, WriteParam, PSSE_Fn, Element
        from elem_obj import make_param_dict, get_real, get_imag"""
        )

# mapping of the data_types to the names returned from psspy.a*types()
types = {'I':'int','R':'real','X':'cplx','C':'char'}

def prepend_block(block, prepend):
    """Return the same block with 'prepend' added to the beginning of lines.

    Doesn't add to empty lines or lines with all spaces."""
    new = []
    for line in block.split('\n'):
        if line and not line.isspace():
            new.append('%s%s' % (prepend, line))
        else:
            new.append(line)

    return '\n'.join(new)

def is_primary_read_name(read_name, data_type):
    """Checks if psspy.a*types() returns the same data type as what is
    specified in read_dict.

    Some times the same read_name will be reused for different data types. We
    choose to acknowledge the data type returned from this function as the
    primary one. The other is commented out."""
    print read_name
    types_func = getattr(psspy, 'a%stypes' % elem_name)
    ierr, vals = types_func(read_name)
    if types[vals[0]] != data_type:
        return False
    return True

def make_slurp_flags(slurp_flags):
    return 'slurp_flags = %s' % str(slurp_flags)


def make_ReadParam(name, data_type, common_read_key=None, read_fn=None):
    """Return the block of text for one of the read_names.

    Block may be commented out depending on is_primary_read_name.

    Input (from the read_dict in the elem outline):
        name: parameter name in the subsystem data retrieval.
        data_type: data type of this parameter.
        common_read_key: the name of the CONSTANT that holds the common string
            for all the subsystem retrieval functions.
        read_fn: An alternative to common_read_key. Currently not implemented.
    """
    strs = {'name':name, 'data_type':data_type,
            'common_read_key':common_read_key, 'read_fn':read_fn}
    if read_fn:
        strs['fn_str'] = "read_fn='%s'," % read_fn
    else:
        strs['fn_str'] = "read_fn_key='%s'," % common_read_key
    paramstr = textwrap.dedent("""\
            ReadParam(name='%(name)s',
                data_type='%(data_type)s',
                %(fn_str)s
                display_name="",
                description=textwrap.dedent(\"\"\"\\

                \"\"\")
                )""" % strs)

    if not is_primary_read_name(name, data_type):
        paramstr = prepend_block(paramstr, '# ')

    return paramstr

def make_DerivedParam(name, data_type):
    """Return the block of text for one of the derived_reads.

    Block may be commented out depending on is_primary_read_name.

    Input (from the read_dict in the elem outline):
        name: parameter name in the subsystem data retrieval.
        data_type: data type of this parameter.
    """
    strs = {'name':name, 'data_type':data_type}
    paramstr = textwrap.dedent("""\
            Parameter(name='%(name)s',
                data_type='%(data_type)s',
                display_name="",
                description=textwrap.dedent(\"\"\"\\

                \"\"\")
                )""" % strs)

    return paramstr

def make_WriteParam(name, read_name, data_type='', trns_fn=''):
    """Return the block of text for one of the write_names.

    Assumes:
        read_param_dict: holds the dictionary of read params.

    Input (from the write_fns in the elem outline):
        name: parameter name function signature.
        read_name: the name of the parameter in the subsystem data retrieval
            which corresponds to this keyword.
        trns_fn: a string containing the function to extract the necessary data
            for this keyword from the data returned by the subsystem data
            retrieval.
        data_type: data type is usually taken from the read_name's datatype.
            But if a different data type is required for this parameter,
            override it with this keyword.
    """
    strs = {'name':name, 'read_name':read_name, 'data_type_arg':data_type,
            'trns_fn_arg':trns_fn}

    predent = '                '
    if data_type:
        strs['data_type_arg'] = "\n%sdata_type='%s'," % (predent, data_type)
    if trns_fn:
        strs['trns_fn_arg'] = "\n%strns_fn=%s," % (predent, trns_fn)

    paramstr = textwrap.dedent("""\
            WriteParam(name='%(name)s',
                read_param='%(read_name)s',%(data_type_arg)s%(trns_fn_arg)s
                base_param=read_param_dict['%(read_name)s']
                )""" % strs)

    # Comment out write parameters that have no corresponding read_name.
    if not read_name:
        paramstr = prepend_block(paramstr, '# ')
    return paramstr

def do_ReadParams(read_dict, derived_reads=None):
    """Return the string of the list of all the read parameters and
    derived_reads (if supplied).

    The string always uses read_params as the variable name for the list that
    contains all the read parameters.
    """
    if 'read_fn' in read_dict:
        read_fn = read_dict[read_fn]
    else:
        read_fn = None

    order = ['int', 'real', 'cplx', 'char']
    params = []
    for p_type in order:
        if p_type in read_dict:
            for read_name in read_dict[p_type]:
                params.append(prepend_block(make_ReadParam(read_name, p_type,
                    'COMMON_READ_FN_KEY', read_fn), indent))

    # This time for the derived parameters.
    if derived_reads:
        for p_type in order:
            if p_type in derived_reads:
                for read_name in derived_reads[p_type]:
                    params.append(
                            prepend_block(make_DerivedParam(read_name, p_type),
                                indent))

    read_params = textwrap.dedent("""\
        read_params = [
        %s
        ]""")
    return read_params % ',\n'.join(params)


def do_WriteParams(fn_dict, param_container):
    """Return the string of the dict of dicts of all the read parameters
    grouped by function name.

    param_container is used for the variable which holds all the write
        parameters.
    """
    if fn_dict == None:
        return '%s = None' % param_container
    overall_str = textwrap.dedent("""\
            %s = {
            %%s
            }""" % param_container)
    fn_str= textwrap.dedent("""\
            '%s':{
            %s
            }""")
    fns = []
    for k, v in fn_dict.items():
        primary_blocks = []
        for param in v['primaries']:
            primary_blocks.append(prepend_block(make_WriteParam(**param),
                indent))

        writable_blocks = []
        for param in v['writables']:
            writable_blocks.append(prepend_block(make_WriteParam(**param),
                indent))

        blocks = textwrap.dedent("""\
                'primaries':[
                %s
                ],
                'writables':[
                %s
                ]""")
        blocks = prepend_block(blocks % (',\n'.join(primary_blocks),
            ',\n'.join(writable_blocks)), indent)

        fns.append(fn_str % (k,blocks))
    return overall_str % prepend_block(',\n'.join(fns), indent)

def do_makefns(list_name, fn_dict, param_container):
    """Return the string of the list of all the PSSE_Fn's.

    The same param_container as before to hold all the write parameters.
        fns is the variable name to be used for the list of PSSE_Fn's.
    """
    if fn_dict == None:
        return '%s = None' % list_name

    fns = []
    for key in fn_dict.keys():
        fns.append(textwrap.dedent("""\
                PSSE_Fn('%(key)s',
                    make_param_dict(%(container)s['%(key)s']['primaries']),
                    make_param_dict(%(container)s['%(key)s']['writables']),
                )"""% {'container':param_container, 'key': key})
                )
    return '%s = [\n%s\n]' % (list_name, prepend_block('\n'.join(fns), indent))

def do_make_elem(elem_name, elem_primaries):
    """Returns the string of the element definition.

    The variable name is the element name with '_elem' appended."""

    if 'special_elem_class' in globals():
        elem_class = special_elem_class
    else:
        elem_class = 'Element'

    del_fn_arg = ''
    if del_fn:
        del_fn_arg = ', del_fn[0]'

    return ('%s_elem = %s("%s", %s, read_param_dict, slurp_flags, fns, %s)' %
            (elem_name, elem_class, elem_name, str(elem_primaries), del_fn_arg))


def make_all():
    """Returns the contents of the final file."""
    if 'derived_reads' in globals():
        read_params_strs = do_ReadParams(read_dict,derived_reads)
    else:
        read_params_strs = do_ReadParams(read_dict)

    if 'additional_imports' in globals():
        imports = '%s\n%s' % (common_imports, additional_imports)
    else:
        imports = common_imports

    bits = [imports,
        'COMMON_READ_FN_KEY = "%s"' % COMMON_READ_FN_KEY,
        make_slurp_flags(slurp_flags),
        read_params_strs,
        "read_param_dict = make_param_dict(read_params)",
        do_WriteParams(write_fns, 'fn_param_dict'),
        do_WriteParams(del_fn, 'del_params'),
        do_makefns('fns', write_fns, 'fn_param_dict'),
        do_makefns('del_fn', del_fn, 'del_params'),
        do_make_elem(elem_name, elem_primaries)]

    return '\n\n'.join(bits)

if __name__=="__main__":
    import sys
    outline_py = sys.argv[1]
    exec 'from %s import *' % outline_py

    fout = open('%s.py'%elem_name, 'w')

    fout.write(make_all())
    fout.close()
