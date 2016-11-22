"""TODO
"""
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"

import textwrap
from elem_obj import ReadParam, WriteParam, PSSE_Fn, Element
from elem_obj import make_param_dict, get_real, get_imag
from elem_obj import Parameter, tr3_Elem

COMMON_READ_FN_KEY = "tr3"

slurp_flags = {'ties': 3, 'flag': 2}

read_params = [
    ReadParam(name='WIND1NUMBER',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='WIND2NUMBER',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='WIND3NUMBER',
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
    ReadParam(name='NMETERNUMBER',
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
    ReadParam(name='CW',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='CZ',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='CM',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='CNXCOD',
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
    ReadParam(name='VMSTAR',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='ANSTAR',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='PLOSS',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='QLOSS',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='O_PLOSS',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='O_QLOSS',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RX1-2ACT',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RX1-2ACTCZ',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RX1-2NOM',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RX1-2NOMCZ',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RX2-3ACT',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RX2-3ACTCZ',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RX2-3NOM',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RX2-3NOMCZ',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RX3-1ACT',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RX3-1ACTCZ',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RX3-1NOM',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RX3-1NOMCZ',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='YMAG',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='YMAGCM',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='ZGRND',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='PQLOSS',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='O_PQLOSS',
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
    ReadParam(name='WIND1NAME',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='WIND1EXNAME',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='WIND2NAME',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='WIND2EXNAME',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='WIND3NAME',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='WIND3EXNAME',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='NMETERNAME',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='NMETEREXNAME',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='XFRNAME',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    Parameter(name='SBASE1-2',
        data_type='real',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    Parameter(name='SBASE2-3',
        data_type='real',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    Parameter(name='SBASE3-1',
        data_type='real',
        display_name="",
        description=textwrap.dedent("""\

        """)
        )
]

read_param_dict = make_param_dict(read_params)

fn_param_dict = {
    'three_wnd_impedance_data':{
        'primaries':[
            WriteParam(name='i',
                read_param='WIND1NUMBER',
                base_param=read_param_dict['WIND1NUMBER']
                ),
            WriteParam(name='j',
                read_param='WIND2NUMBER',
                base_param=read_param_dict['WIND2NUMBER']
                ),
            WriteParam(name='k',
                read_param='WIND3NUMBER',
                base_param=read_param_dict['WIND3NUMBER']
                ),
            WriteParam(name='ckt',
                read_param='ID',
                base_param=read_param_dict['ID']
                )
        ],
        'writables':[
            WriteParam(name='name',
                read_param='XFRNAME',
                base_param=read_param_dict['XFRNAME']
                ),
            WriteParam(name='intgar1',
                read_param='OWN1',
                base_param=read_param_dict['OWN1']
                ),
            WriteParam(name='intgar2',
                read_param='OWN2',
                base_param=read_param_dict['OWN2']
                ),
            WriteParam(name='intgar3',
                read_param='OWN3',
                base_param=read_param_dict['OWN3']
                ),
            WriteParam(name='intgar4',
                read_param='OWN4',
                base_param=read_param_dict['OWN4']
                ),
            WriteParam(name='intgar5',
                read_param='CW',
                base_param=read_param_dict['CW']
                ),
            WriteParam(name='intgar6',
                read_param='CZ',
                base_param=read_param_dict['CZ']
                ),
            WriteParam(name='intgar7',
                read_param='CM',
                base_param=read_param_dict['CM']
                ),
            WriteParam(name='intgar8',
                read_param='STATUS',
                base_param=read_param_dict['STATUS']
                ),
            WriteParam(name='intgar9',
                read_param='NMETERNUMBER',
                base_param=read_param_dict['NMETERNUMBER']
                ),
            WriteParam(name='intgar10',
                read_param='WIND1NUMBER',
                base_param=read_param_dict['WIND1NUMBER']
                ),
            WriteParam(name='intgar11',
                read_param='WIND2NUMBER',
                base_param=read_param_dict['WIND2NUMBER']
                ),
            WriteParam(name='intgar12',
                read_param='WIND3NUMBER',
                base_param=read_param_dict['WIND3NUMBER']
                ),
            WriteParam(name='realari1',
                read_param='RX1-2NOM',
                data_type='real',
                trns_fn=get_real,
                base_param=read_param_dict['RX1-2NOM']
                ),
            WriteParam(name='realari2',
                read_param='RX1-2NOM',
                data_type='real',
                trns_fn=get_imag,
                base_param=read_param_dict['RX1-2NOM']
                ),
            WriteParam(name='realari3',
                read_param='RX2-3NOM',
                data_type='real',
                trns_fn=get_real,
                base_param=read_param_dict['RX2-3NOM']
                ),
            WriteParam(name='realari4',
                read_param='RX2-3NOM',
                data_type='real',
                trns_fn=get_imag,
                base_param=read_param_dict['RX2-3NOM']
                ),
            WriteParam(name='realari5',
                read_param='RX3-1NOM',
                data_type='real',
                trns_fn=get_real,
                base_param=read_param_dict['RX3-1NOM']
                ),
            WriteParam(name='realari6',
                read_param='RX3-1NOM',
                data_type='real',
                trns_fn=get_imag,
                base_param=read_param_dict['RX3-1NOM']
                ),
            WriteParam(name='realari7',
                read_param='SBASE1-2',
                base_param=read_param_dict['SBASE1-2']
                ),
            WriteParam(name='realari8',
                read_param='SBASE2-3',
                base_param=read_param_dict['SBASE2-3']
                ),
            WriteParam(name='realari9',
                read_param='SBASE3-1',
                base_param=read_param_dict['SBASE3-1']
                ),
            WriteParam(name='realari10',
                read_param='YMAG',
                data_type='real',
                trns_fn=get_real,
                base_param=read_param_dict['YMAG']
                ),
            WriteParam(name='realari11',
                read_param='YMAG',
                data_type='real',
                trns_fn=get_imag,
                base_param=read_param_dict['YMAG']
                ),
            WriteParam(name='realari12',
                read_param='FRACT1',
                base_param=read_param_dict['FRACT1']
                ),
            WriteParam(name='realari13',
                read_param='FRACT2',
                base_param=read_param_dict['FRACT2']
                ),
            WriteParam(name='realari14',
                read_param='FRACT3',
                base_param=read_param_dict['FRACT3']
                ),
            WriteParam(name='realari15',
                read_param='FRACT4',
                base_param=read_param_dict['FRACT4']
                ),
            WriteParam(name='realari16',
                read_param='VMSTAR',
                base_param=read_param_dict['VMSTAR']
                ),
            WriteParam(name='realari17',
                read_param='ANSTAR',
                base_param=read_param_dict['ANSTAR']
                )
        ]
    }
}

del_params = {
    'purg3wnd':{
        'primaries':[
            WriteParam(name='frmbus',
                read_param='WIND1NUMBER',
                base_param=read_param_dict['WIND1NUMBER']
                ),
            WriteParam(name='tobus1',
                read_param='WIND2NUMBER',
                base_param=read_param_dict['WIND2NUMBER']
                ),
            WriteParam(name='tobus2',
                read_param='WIND3NUMBER',
                base_param=read_param_dict['WIND3NUMBER']
                ),
            WriteParam(name='ckt',
                read_param='ID',
                base_param=read_param_dict['ID']
                )
        ],
        'writables':[

        ]
    }
}

fns = [
    PSSE_Fn('three_wnd_impedance_data',
        make_param_dict(fn_param_dict['three_wnd_impedance_data']['primaries']),
        make_param_dict(fn_param_dict['three_wnd_impedance_data']['writables']),
    )
]

del_fn = [
    PSSE_Fn('purg3wnd',
        make_param_dict(del_params['purg3wnd']['primaries']),
        make_param_dict(del_params['purg3wnd']['writables']),
    )
]

tr3_elem = tr3_Elem("tr3", ('WIND1NUMBER', 'WIND2NUMBER', 'WIND3NUMBER', 'ID'), read_param_dict, slurp_flags, fns, del_fn[0])