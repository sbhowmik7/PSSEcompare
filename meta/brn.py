"""brn: element branch
"""
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"


import textwrap
from elem_obj import ReadParam, WriteParam, PSSE_Fn, Element
from elem_obj import make_param_dict, get_real, get_imag

COMMON_READ_FN_KEY = "brn"

slurp_flags = {'ties': 3, 'flag': 2}

read_params = [
    ReadParam(name='FROMNUMBER',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='TONUMBER',
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
    ReadParam(name='METERNUMBER',
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
    ReadParam(name='AMPS',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='PUCUR',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='PCTRATE',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='PCTRATEA',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='PCTRATEB',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='PCTRATEC',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='PCTMVARATE',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='PCTMVARATEA',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='PCTMVARATEB',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='PCTMVARATEC',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='PCTCORPRATE',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='PCTCORPRATEA',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='PCTCORPRATEB',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='PCTCORPRATEC',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='MAXPCTRATE',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='MAXPCTRATEA',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='MAXPCTRATEB',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='MAXPCTRATEC',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='MXPCTMVARAT',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='MXPCTMVARATA',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='MXPCTMVARATB',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='MXPCTMVARATC',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='MXPCTCRPRAT',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='MXPCTCRPRATA',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='MXPCTCRPRATB',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='MXPCTCRPRATC',
        data_type='real',
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
    ReadParam(name='RATE',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RATEA',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RATEB',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RATEC',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='LENGTH',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='CHARGING',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='CHARGINGZERO',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='P',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='Q',
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
    ReadParam(name='MAXMVA',
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
    ReadParam(name='O_P',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='O_Q',
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
    ReadParam(name='O_MAXMVA',
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
    ReadParam(name='RX',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='FROMSHNT',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='TOSHNT',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RXZERO',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='FROMSHNTZERO',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='TOSHNTZERO',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='PQ',
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
    ReadParam(name='O_PQ',
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
    ReadParam(name='FROMNAME',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='FROMEXNAME',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='TONAME',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='TOEXNAME',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='METERNAME',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='METEREXNAME',
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
        )
]

read_param_dict = make_param_dict(read_params)

fn_param_dict = {
    'branch_data':{
        'primaries':[
            WriteParam(name='i',
                read_param='FROMNUMBER',
                base_param=read_param_dict['FROMNUMBER']
                ),
            WriteParam(name='j',
                read_param='TONUMBER',
                base_param=read_param_dict['TONUMBER']
                ),
            WriteParam(name='ckt',
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
                read_param='METERNUMBER',
                base_param=read_param_dict['METERNUMBER']
                ),
            WriteParam(name='intgar3',
                read_param='OWN1',
                base_param=read_param_dict['OWN1']
                ),
            WriteParam(name='intgar4',
                read_param='OWN2',
                base_param=read_param_dict['OWN2']
                ),
            WriteParam(name='intgar5',
                read_param='OWN3',
                base_param=read_param_dict['OWN3']
                ),
            WriteParam(name='intgar6',
                read_param='OWN4',
                base_param=read_param_dict['OWN4']
                ),
            WriteParam(name='realar1',
                read_param='RX',
                data_type='real',
                trns_fn=get_real,
                base_param=read_param_dict['RX']
                ),
            WriteParam(name='realar2',
                read_param='RX',
                data_type='real',
                trns_fn=get_imag,
                base_param=read_param_dict['RX']
                ),
            WriteParam(name='realar3',
                read_param='CHARGING',
                base_param=read_param_dict['CHARGING']
                ),
            WriteParam(name='realar4',
                read_param='RATEA',
                base_param=read_param_dict['RATEA']
                ),
            WriteParam(name='realar5',
                read_param='RATEB',
                base_param=read_param_dict['RATEB']
                ),
            WriteParam(name='realar6',
                read_param='RATEC',
                base_param=read_param_dict['RATEC']
                ),
            WriteParam(name='realar7',
                read_param='FROMSHNT',
                data_type='real',
                trns_fn=get_real,
                base_param=read_param_dict['FROMSHNT']
                ),
            WriteParam(name='realar8',
                read_param='FROMSHNT',
                data_type='real',
                trns_fn=get_imag,
                base_param=read_param_dict['FROMSHNT']
                ),
            WriteParam(name='realar9',
                read_param='TOSHNT',
                data_type='real',
                trns_fn=get_real,
                base_param=read_param_dict['TOSHNT']
                ),
            WriteParam(name='realar10',
                read_param='TOSHNT',
                data_type='real',
                trns_fn=get_imag,
                base_param=read_param_dict['TOSHNT']
                ),
            WriteParam(name='realar11',
                read_param='LENGTH',
                base_param=read_param_dict['LENGTH']
                ),
            WriteParam(name='realar12',
                read_param='FRACT1',
                base_param=read_param_dict['FRACT1']
                ),
            WriteParam(name='realar13',
                read_param='FRACT2',
                base_param=read_param_dict['FRACT2']
                ),
            WriteParam(name='realar14',
                read_param='FRACT3',
                base_param=read_param_dict['FRACT3']
                ),
            WriteParam(name='realar15',
                read_param='FRACT4',
                base_param=read_param_dict['FRACT4']
                )
        ]
    }
}

del_params = {
    'purgbrn':{
        'primaries':[
            WriteParam(name='frmbus',
                read_param='FROMNUMBER',
                base_param=read_param_dict['FROMNUMBER']
                ),
            WriteParam(name='tobus',
                read_param='TONUMBER',
                base_param=read_param_dict['TONUMBER']
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
    PSSE_Fn('branch_data',
        make_param_dict(fn_param_dict['branch_data']['primaries']),
        make_param_dict(fn_param_dict['branch_data']['writables']),
    )
]

del_fn = [
    PSSE_Fn('purgbrn',
        make_param_dict(del_params['purgbrn']['primaries']),
        make_param_dict(del_params['purgbrn']['writables']),
    )
]

brn_elem = Element("brn", ('FROMNUMBER', 'TONUMBER', 'ID'), read_param_dict, slurp_flags, fns, del_fn[0])