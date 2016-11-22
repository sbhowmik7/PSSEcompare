"""brn: element branch
"""
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"

import textwrap
from elem_obj import ReadParam, WriteParam, PSSE_Fn, Element
from elem_obj import make_param_dict, get_real, get_imag

COMMON_READ_FN_KEY = "fxshunt"

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
    # ReadParam(name='PU_GBZERO',
    #     data_type='real',
    #     read_fn_key='COMMON_READ_FN_KEY',
    #     display_name="",
    #     description=textwrap.dedent("""\

    #     """)
    #     ),
    # ReadParam(name='SHUNTACT',
    #     data_type='real',
    #     read_fn_key='COMMON_READ_FN_KEY',
    #     display_name="",
    #     description=textwrap.dedent("""\

    #     """)
    #     ),
    # ReadParam(name='SHUNTNOM',
    #     data_type='real',
    #     read_fn_key='COMMON_READ_FN_KEY',
    #     display_name="",
    #     description=textwrap.dedent("""\

    #     """)
    #     ),
    # ReadParam(name='GBZERO',
    #     data_type='real',
    #     read_fn_key='COMMON_READ_FN_KEY',
    #     display_name="",
    #     description=textwrap.dedent("""\

    #     """)
    #     ),
    # ReadParam(name='O_SHUNTACT',
    #     data_type='real',
    #     read_fn_key='COMMON_READ_FN_KEY',
    #     display_name="",
    #     description=textwrap.dedent("""\

    #     """)
    #     ),
    # ReadParam(name='O_SHUNTNOM',
    #     data_type='real',
    #     read_fn_key='COMMON_READ_FN_KEY',
    #     display_name="",
    #     description=textwrap.dedent("""\

    #     """)
    #     ),
    # ReadParam(name='O_GBZERO',
    #     data_type='real',
    #     read_fn_key='COMMON_READ_FN_KEY',
    #     display_name="",
    #     description=textwrap.dedent("""\

    #     """)
    #     ),
    ReadParam(name='PU_GBZERO',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='SHUNTACT',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='SHUNTNOM',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='GBZERO',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='O_SHUNTACT',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='O_SHUNTNOM',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='O_GBZERO',
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
    'shunt_data':{
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
            WriteParam(name='realar1',
                read_param='SHUNTNOM',
                data_type='real',
                trns_fn=get_real,
                base_param=read_param_dict['SHUNTNOM']
                ),
            WriteParam(name='realar2',
                read_param='SHUNTNOM',
                data_type='real',
                trns_fn=get_imag,
                base_param=read_param_dict['SHUNTNOM']
                )
        ]
    }
}

del_params = {
    'purgshunt':{
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
    PSSE_Fn('shunt_data',
        make_param_dict(fn_param_dict['shunt_data']['primaries']),
        make_param_dict(fn_param_dict['shunt_data']['writables']),
    )
]

del_fn = [
    PSSE_Fn('purgshunt',
        make_param_dict(del_params['purgshunt']['primaries']),
        make_param_dict(del_params['purgshunt']['writables']),
    )
]

fxshunt_elem = Element("fxshunt", ('NUMBER', 'ID'), read_param_dict, slurp_flags, fns, del_fn[0])