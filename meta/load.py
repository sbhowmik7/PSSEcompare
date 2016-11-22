"""TODO
"""
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"

import textwrap
from elem_obj import ReadParam, WriteParam, PSSE_Fn, Element
from elem_obj import make_param_dict, get_real, get_imag

COMMON_READ_FN_KEY = "load"

slurp_flags = {'flag': 4}

read_params = [
    ReadParam(name='NUMBER',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='AREA',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='ZONE',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='OWNER',
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
    # ReadParam(name='SCALE',
    #     data_type='int',
    #     read_fn_key='COMMON_READ_FN_KEY',
    #     display_name="",
    #     description=textwrap.dedent("""\
    #
    #     """)
    #     ),
    # ReadParam(name='MVAACT',
    #     data_type='real',
    #     read_fn_key='COMMON_READ_FN_KEY',
    #     display_name="",
    #     description=textwrap.dedent("""\

    #     """)
    #     ),
    # ReadParam(name='MVANOM',
    #     data_type='real',
    #     read_fn_key='COMMON_READ_FN_KEY',
    #     display_name="",
    #     description=textwrap.dedent("""\

    #     """)
    #     ),
    # ReadParam(name='ILACT',
    #     data_type='real',
    #     read_fn_key='COMMON_READ_FN_KEY',
    #     display_name="",
    #     description=textwrap.dedent("""\

    #     """)
    #     ),
    # ReadParam(name='ILNOM',
    #     data_type='real',
    #     read_fn_key='COMMON_READ_FN_KEY',
    #     display_name="",
    #     description=textwrap.dedent("""\

    #     """)
    #     ),
    # ReadParam(name='YLACT',
    #     data_type='real',
    #     read_fn_key='COMMON_READ_FN_KEY',
    #     display_name="",
    #     description=textwrap.dedent("""\

    #     """)
    #     ),
    # ReadParam(name='YLNOM',
    #     data_type='real',
    #     read_fn_key='COMMON_READ_FN_KEY',
    #     display_name="",
    #     description=textwrap.dedent("""\

    #     """)
    #     ),
    # ReadParam(name='TOTALACT',
    #     data_type='real',
    #     read_fn_key='COMMON_READ_FN_KEY',
    #     display_name="",
    #     description=textwrap.dedent("""\

    #     """)
    #     ),
    # ReadParam(name='TOTALNOM',
    #     data_type='real',
    #     read_fn_key='COMMON_READ_FN_KEY',
    #     display_name="",
    #     description=textwrap.dedent("""\

    #     """)
    #     ),
    # ReadParam(name='O_MVAACT',
    #     data_type='real',
    #     read_fn_key='COMMON_READ_FN_KEY',
    #     display_name="",
    #     description=textwrap.dedent("""\

    #     """)
    #     ),
    # ReadParam(name='O_MVANOM',
    #     data_type='real',
    #     read_fn_key='COMMON_READ_FN_KEY',
    #     display_name="",
    #     description=textwrap.dedent("""\

    #     """)
    #     ),
    # ReadParam(name='O_ILACT',
    #     data_type='real',
    #     read_fn_key='COMMON_READ_FN_KEY',
    #     display_name="",
    #     description=textwrap.dedent("""\

    #     """)
    #     ),
    # ReadParam(name='O_YLACT',
    #     data_type='real',
    #     read_fn_key='COMMON_READ_FN_KEY',
    #     display_name="",
    #     description=textwrap.dedent("""\

    #     """)
    #     ),
    # ReadParam(name='O_YLNOM',
    #     data_type='real',
    #     read_fn_key='COMMON_READ_FN_KEY',
    #     display_name="",
    #     description=textwrap.dedent("""\

    #     """)
    #     ),
    # ReadParam(name='O_TOTALACT',
    #     data_type='real',
    #     read_fn_key='COMMON_READ_FN_KEY',
    #     display_name="",
    #     description=textwrap.dedent("""\

    #     """)
    #     ),
    # ReadParam(name='O_TOTALNOM',
    #     data_type='real',
    #     read_fn_key='COMMON_READ_FN_KEY',
    #     display_name="",
    #     description=textwrap.dedent("""\

    #     """)
    #     ),
    ReadParam(name='MVAACT',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='MVANOM',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='ILACT',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='ILNOM',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='YLACT',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='YLNOM',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='TOTALACT',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='TOTALNOM',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='O_MVAACT',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='O_MVANOM',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='O_ILACT',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='O_YLACT',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='O_YLNOM',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='O_TOTALACT',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='O_TOTALNOM',
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
    'load_data_3':{
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
                read_param='AREA',
                base_param=read_param_dict['AREA']
                ),
            WriteParam(name='intgar3',
                read_param='ZONE',
                base_param=read_param_dict['ZONE']
                ),
            WriteParam(name='intgar4',
                read_param='OWNER',
                base_param=read_param_dict['OWNER']
                ),
            # WriteParam(name='intgar5',
            #     read_param='SCALE',
            #     base_param=read_param_dict['SCALE']
            #     ),
            WriteParam(name='realar1',
                read_param='MVANOM',
                data_type='real',
                trns_fn=get_real,
                base_param=read_param_dict['MVANOM']
                ),
            WriteParam(name='realar2',
                read_param='MVANOM',
                data_type='real',
                trns_fn=get_imag,
                base_param=read_param_dict['MVANOM']
                ),
            WriteParam(name='realar3',
                read_param='ILNOM',
                data_type='real',
                trns_fn=get_real,
                base_param=read_param_dict['ILNOM']
                ),
            WriteParam(name='realar4',
                read_param='ILNOM',
                data_type='real',
                trns_fn=get_imag,
                base_param=read_param_dict['ILNOM']
                ),
            WriteParam(name='realar5',
                read_param='YLNOM',
                data_type='real',
                trns_fn=get_real,
                base_param=read_param_dict['YLNOM']
                ),
            WriteParam(name='realar6',
                read_param='YLNOM',
                data_type='real',
                trns_fn=get_imag,
                base_param=read_param_dict['YLNOM']
                )
        ]
    }
}

del_params = {
    'purgload':{
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
    PSSE_Fn('load_data_3',
        make_param_dict(fn_param_dict['load_data_3']['primaries']),
        make_param_dict(fn_param_dict['load_data_3']['writables']),
    )
]

del_fn = [
    PSSE_Fn('purgload',
        make_param_dict(del_params['purgload']['primaries']),
        make_param_dict(del_params['purgload']['writables']),
    )
]

load_elem = Element("load", ('NUMBER', 'ID'), read_param_dict, slurp_flags, fns, del_fn[0])