"""TODO
"""
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"

import textwrap
from elem_obj import ReadParam, WriteParam, PSSE_Fn, Element
from elem_obj import make_param_dict, get_real, get_imag

COMMON_READ_FN_KEY = "mach"

slurp_flags = {'flag': 4}

read_params = [
    ReadParam(name='NUMBER',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='STATUS',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='WMOD',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='OWNERS',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='OWN1',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='OWN2',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='OWN3',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='OWN4',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='FRACT1',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='FRACT2',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='FRACT3',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='FRACT4',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='PERCENT',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='MBASE',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='GENTAP',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='WPF',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='PGEN',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='QGEN',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='MVA',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='PMAX',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='PMIN',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='QMAX',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='QMIN',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='O_PGEN',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='O_QGEN',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='O_MVA',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='O_PMAX',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='O_PMIN',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='O_QMAX',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='O_QMIN',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='ZSORCE',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='XTRAN',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='ZPOS',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='ZNEG',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='ZZERO',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='PQGEN',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='O_PQGEN',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='ID',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='NAME',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='EXNAME',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        )
]

read_param_dict = make_param_dict(read_params)

fn_param_dict = {
    'machine_data_2':{
        'primaries':[
            WriteParam(name='i',
                read_param='NUMBER',
                base_param=read_param_dict['NUMBER']
                ),
            WriteParam(name='id',
                read_param='ID',
                base_param=read_param_dict['ID']
                )
        ],
        'writables':[
            WriteParam(name='intgar1',
                read_param='STATUS',
                base_param=read_param_dict['STATUS']
                ),
            WriteParam(name='intgar2',
                read_param='OWN1',
                base_param=read_param_dict['OWN1']
                ),
            WriteParam(name='intgar3',
                read_param='OWN2',
                base_param=read_param_dict['OWN2']
                ),
            WriteParam(name='intgar4',
                read_param='OWN3',
                base_param=read_param_dict['OWN3']
                ),
            WriteParam(name='intgar5',
                read_param='OWN4',
                base_param=read_param_dict['OWN4']
                ),
            WriteParam(name='intgar6',
                read_param='WMOD',
                base_param=read_param_dict['WMOD']
                ),
            WriteParam(name='realar1',
                read_param='PGEN',
                base_param=read_param_dict['PGEN']
                ),
            WriteParam(name='realar2',
                read_param='QGEN',
                base_param=read_param_dict['QGEN']
                ),
            WriteParam(name='realar3',
                read_param='QMAX',
                base_param=read_param_dict['QMAX']
                ),
            WriteParam(name='realar4',
                read_param='QMIN',
                base_param=read_param_dict['QMIN']
                ),
            WriteParam(name='realar5',
                read_param='PMAX',
                base_param=read_param_dict['PMAX']
                ),
            WriteParam(name='realar6',
                read_param='PMIN',
                base_param=read_param_dict['PMIN']
                ),
            WriteParam(name='realar7',
                read_param='MBASE',
                base_param=read_param_dict['MBASE']
                ),
            WriteParam(name='realar8',
                read_param='ZSORCE',
                data_type='real',
                trns_fn=get_real,
                base_param=read_param_dict['ZSORCE']
                ),
            WriteParam(name='realar9',
                read_param='ZSORCE',
                data_type='real',
                trns_fn=get_imag,
                base_param=read_param_dict['ZSORCE']
                ),
            WriteParam(name='realar10',
                read_param='XTRAN',
                data_type='real',
                trns_fn=get_real,
                base_param=read_param_dict['XTRAN']
                ),
            WriteParam(name='realar11',
                read_param='XTRAN',
                data_type='real',
                trns_fn=get_imag,
                base_param=read_param_dict['XTRAN']
                ),
            WriteParam(name='realar12',
                read_param='GENTAP',
                base_param=read_param_dict['GENTAP']
                ),
            WriteParam(name='realar13',
                read_param='FRACT1',
                base_param=read_param_dict['FRACT1']
                ),
            WriteParam(name='realar14',
                read_param='FRACT2',
                base_param=read_param_dict['FRACT2']
                ),
            WriteParam(name='realar15',
                read_param='FRACT3',
                base_param=read_param_dict['FRACT3']
                ),
            WriteParam(name='realar16',
                read_param='FRACT4',
                base_param=read_param_dict['FRACT4']
                ),
            WriteParam(name='realar17',
                read_param='WPF',
                base_param=read_param_dict['WPF']
                )
        ]
    }
}

del_params = {
    'purgmac':{
        'primaries':[
            WriteParam(name='frmbus',
                read_param='NUMBER',
                base_param=read_param_dict['NUMBER']
                ),
            WriteParam(name='id',
                read_param='ID',
                base_param=read_param_dict['ID']
                )
        ],
        'writables':[

        ]
    }
}

fns = [
    PSSE_Fn('machine_data_2',
        make_param_dict(fn_param_dict['machine_data_2']['primaries']),
        make_param_dict(fn_param_dict['machine_data_2']['writables']),
    )
]

del_fn = [
    PSSE_Fn('purgmac',
        make_param_dict(del_params['purgmac']['primaries']),
        make_param_dict(del_params['purgmac']['writables']),
    )
]

mach_elem = Element("mach", ('NUMBER', 'ID'), read_param_dict, slurp_flags, fns, del_fn[0])