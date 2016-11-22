"""TODO
"""
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"

import textwrap
from elem_obj import ReadParam, WriteParam, PSSE_Fn, Element
from elem_obj import make_param_dict, get_real, get_imag

COMMON_READ_FN_KEY = "trn"

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
    ReadParam(name='ICONTNUMBER',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
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
    ReadParam(name='TABLE',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='CODE',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='NTPOSN',
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
    ReadParam(name='TPSTT',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='ANSTT',
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
    ReadParam(name='RATIO',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RATIOCW',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RATIO2',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RATIO2CW',
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
    ReadParam(name='RMAX',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RMAXCW',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RMIN',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RMINCW',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='VMAX',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='VMAXKV',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='VMIN',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='VMINKV',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='STEP',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='STEPCW',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='NOMV1',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='NOMV2',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='SBASE1',
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
    ReadParam(name='RXACT',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RXACTCZ',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RXNOM',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='RXNOMCZ',
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
    ReadParam(name='COMPRX',
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
    ReadParam(name='ZGRND',
        data_type='cplx',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='ZGRND2',
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
        ),
    ReadParam(name='ICONTNAME',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='ICONTEXNAME',
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
    ReadParam(name='XFRNAME',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        )
]

read_param_dict = make_param_dict(read_params)

fn_param_dict = {
    'two_winding_data_3':{
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
            WriteParam(name='name',
                read_param='XFRNAME',
                base_param=read_param_dict['XFRNAME']
                ),
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
            WriteParam(name='intgar7',
                read_param='NTPOSN',
                base_param=read_param_dict['NTPOSN']
                ),
            WriteParam(name='intgar8',
                read_param='TABLE',
                base_param=read_param_dict['TABLE']
                ),
            WriteParam(name='intgar9',
                read_param='WIND1NUMBER',
                base_param=read_param_dict['WIND1NUMBER']
                ),
            WriteParam(name='intgar10',
                read_param='ICONTNUMBER',
                base_param=read_param_dict['ICONTNUMBER']
                ),
            # WriteParam(name='intgar11',
            #     read_param='None',
            #     base_param=read_param_dict['None']
            #     ),
            WriteParam(name='intgar12',
                read_param='CODE',
                base_param=read_param_dict['CODE']
                ),
            WriteParam(name='intgar13',
                read_param='CW',
                base_param=read_param_dict['CW']
                ),
            WriteParam(name='intgar14',
                read_param='CZ',
                base_param=read_param_dict['CZ']
                ),
            WriteParam(name='intgar15',
                read_param='CM',
                base_param=read_param_dict['CM']
                ),
            WriteParam(name='realari1',
                read_param='RXNOM',
                data_type='real',
                trns_fn=get_real,
                base_param=read_param_dict['RXNOM']
                ),
            WriteParam(name='realari2',
                read_param='RXNOM',
                data_type='real',
                trns_fn=get_imag,
                base_param=read_param_dict['RXNOM']
                ),
            WriteParam(name='realari3',
                read_param='SBASE1',
                base_param=read_param_dict['SBASE1']
                ),
            WriteParam(name='realari4',
                read_param='RATIO',
                base_param=read_param_dict['RATIO']
                ),
            WriteParam(name='realari5',
                read_param='NOMV1',
                base_param=read_param_dict['NOMV1']
                ),
            WriteParam(name='realari6',
                read_param='ANGLE',
                base_param=read_param_dict['ANGLE']
                ),
            WriteParam(name='realari7',
                read_param='RATIO2',
                base_param=read_param_dict['RATIO2']
                ),
            WriteParam(name='realari8',
                read_param='NOMV2',
                base_param=read_param_dict['NOMV2']
                ),
            WriteParam(name='realari9',
                read_param='RATEA',
                base_param=read_param_dict['RATEA']
                ),
            WriteParam(name='realari10',
                read_param='RATEB',
                base_param=read_param_dict['RATEB']
                ),
            WriteParam(name='realari11',
                read_param='RATEC',
                base_param=read_param_dict['RATEC']
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
                read_param='YMAG',
                data_type='real',
                trns_fn=get_real,
                base_param=read_param_dict['YMAG']
                ),
            WriteParam(name='realari17',
                read_param='YMAG',
                data_type='real',
                trns_fn=get_imag,
                base_param=read_param_dict['YMAG']
                ),
            WriteParam(name='realari18',
                read_param='RMAX',
                base_param=read_param_dict['RMAX']
                ),
            WriteParam(name='realari19',
                read_param='RMIN',
                base_param=read_param_dict['RMIN']
                ),
            WriteParam(name='realari20',
                read_param='VMAX',
                base_param=read_param_dict['VMAX']
                ),
            WriteParam(name='realari21',
                read_param='VMIN',
                base_param=read_param_dict['VMIN']
                ),
            WriteParam(name='realari22',
                read_param='COMPRX',
                data_type='real',
                trns_fn=get_real,
                base_param=read_param_dict['COMPRX']
                ),
            WriteParam(name='realari23',
                read_param='COMPRX',
                data_type='real',
                trns_fn=get_imag,
                base_param=read_param_dict['COMPRX']
                ),
            # WriteParam(name='realari24',
            #     read_param='None',
            #     base_param=read_param_dict['None']
            #     )
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
    PSSE_Fn('two_winding_data_3',
        make_param_dict(fn_param_dict['two_winding_data_3']['primaries']),
        make_param_dict(fn_param_dict['two_winding_data_3']['writables']),
    )
]

del_fn = [
    PSSE_Fn('purgbrn',
        make_param_dict(del_params['purgbrn']['primaries']),
        make_param_dict(del_params['purgbrn']['writables']),
    )
]

trn_elem = Element("trn", ('FROMNUMBER', 'TONUMBER', 'ID'), read_param_dict, slurp_flags, fns, del_fn[0])