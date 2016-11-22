"""TODO
"""
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"

import textwrap
from elem_obj import ReadParam, WriteParam, PSSE_Fn, Element
from elem_obj import make_param_dict, get_real, get_imag

COMMON_READ_FN_KEY = "genbus"

slurp_flags = {'flag': 4}

read_params = [
    ReadParam(name='NUMBER',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='TYPE',
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
    ReadParam(name='DUMMY',
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
    ReadParam(name='IREG',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='BASE',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='PU',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='KV',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='ANGLE',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='ANGLED',
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
    ReadParam(name='IREGBASE',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='IREGPU',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='IREGKV',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='VSPU',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='VSKV',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RMPCT',
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
    # ReadParam(name='MISMATCH',
    #     data_type='real',
    #     read_fn_key='COMMON_READ_FN_KEY',
    #     display_name="",
    #     description=textwrap.dedent("""\

    #     """)
    #     ),
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
    # ReadParam(name='O_MISMATCH',
    #     data_type='real',
    #     read_fn_key='COMMON_READ_FN_KEY',
    #     display_name="",
    #     description=textwrap.dedent("""\

    #     """)
    #     ),
    ReadParam(name='VOLTAGE',
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
    ReadParam(name='MISMATCH',
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
    ReadParam(name='O_MISMATCH',
        data_type='cplx',
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
        ),
    ReadParam(name='IREGNAME',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='IREGEXNAME',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        )
]

read_param_dict = make_param_dict(read_params)

fn_param_dict = {
    'plant_data':{
        'primaries':[
            WriteParam(name='i',
                read_param='NUMBER',
                base_param=read_param_dict['NUMBER']
                )
        ],
        'writables':[
            WriteParam(name='intgar1',
                read_param='IREG',
                base_param=read_param_dict['IREG']
                ),
            WriteParam(name='realar1',
                read_param='VSPU',
                base_param=read_param_dict['VSPU']
                ),
            WriteParam(name='realar2',
                read_param='RMPCT',
                base_param=read_param_dict['RMPCT']
                )
        ]
    }
}

del_params = {
    'purgplnt':{
        'primaries':[
            WriteParam(name='frmbus',
                read_param='NUMBER',
                base_param=read_param_dict['NUMBER']
                )
        ],
        'writables':[

        ]
    }
}

fns = [
    PSSE_Fn('plant_data',
        make_param_dict(fn_param_dict['plant_data']['primaries']),
        make_param_dict(fn_param_dict['plant_data']['writables']),
    )
]

del_fn = [
    PSSE_Fn('purgplnt',
        make_param_dict(del_params['purgplnt']['primaries']),
        make_param_dict(del_params['purgplnt']['writables']),
    )
]

genbus_elem = Element("genbus", ('NUMBER',), read_param_dict, slurp_flags, fns, del_fn[0])