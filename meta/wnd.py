"""TODO
"""
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"

import textwrap
from elem_obj import ReadParam, WriteParam, PSSE_Fn, Element
from elem_obj import make_param_dict, get_real, get_imag

COMMON_READ_FN_KEY = "wnd"

slurp_flags = {'ties': 3, 'flag': 3}

read_params = [
    ReadParam(name='WNDBUSNUMBER',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='OTHER1NUMBER',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='OTHER2NUMBER',
        data_type='int',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='WNDNUM',
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
    ReadParam(name='WIND3NUMBER',
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
    ReadParam(name='STATUS',
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
    ReadParam(name='NOMV',
        data_type='real',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='SBASE',
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
    ReadParam(name='RXNOM',
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
    ReadParam(name='WNDBUSNAME',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='WNDBUSEXNAME',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='OTHER1NAME',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='OTHER1EXNAME',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='OTHER2NAME',
        data_type='char',
        read_fn_key='COMMON_READ_FN_KEY',
        display_name="",
        description=textwrap.dedent("""\

        """)
        ),
    ReadParam(name='OTHER2EXNAME',
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
        )
]

read_param_dict = make_param_dict(read_params)

fn_param_dict = {
    'three_wnd_winding_data_3':{
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
                ),
            WriteParam(name='warg',
                read_param='WNDNUM',
                base_param=read_param_dict['WNDNUM']
                )
        ],
        'writables':[
            WriteParam(name='intgar1',
                read_param='NTPOSN',
                base_param=read_param_dict['NTPOSN']
                ),
            WriteParam(name='intgar2',
                read_param='TABLE',
                base_param=read_param_dict['TABLE']
                ),
            WriteParam(name='intgar3',
                read_param='ICONTNUMBER',
                base_param=read_param_dict['ICONTNUMBER']
                ),
            # WriteParam(name='intgar4',
            #     read_param='None',
            #     base_param=read_param_dict['None']
            #     ),
            WriteParam(name='intgar5',
                read_param='CODE',
                base_param=read_param_dict['CODE']
                ),
            WriteParam(name='realari1',
                read_param='RATIO',
                base_param=read_param_dict['RATIO']
                ),
            WriteParam(name='realari2',
                read_param='NOMV',
                base_param=read_param_dict['NOMV']
                ),
            WriteParam(name='realari3',
                read_param='ANGLE',
                base_param=read_param_dict['ANGLE']
                ),
            WriteParam(name='realari4',
                read_param='RATEA',
                base_param=read_param_dict['RATEA']
                ),
            WriteParam(name='realari5',
                read_param='RATEB',
                base_param=read_param_dict['RATEB']
                ),
            WriteParam(name='realari6',
                read_param='RATEC',
                base_param=read_param_dict['RATEC']
                ),
            WriteParam(name='realari7',
                read_param='RMAX',
                base_param=read_param_dict['RMAX']
                ),
            WriteParam(name='realari8',
                read_param='RMIN',
                base_param=read_param_dict['RMIN']
                ),
            WriteParam(name='realari9',
                read_param='VMAX',
                base_param=read_param_dict['VMAX']
                ),
            WriteParam(name='realari10',
                read_param='VMIN',
                base_param=read_param_dict['VMIN']
                ),
            WriteParam(name='realari11',
                read_param='COMPRX',
                data_type='real',
                trns_fn=get_real,
                base_param=read_param_dict['COMPRX']
                ),
            WriteParam(name='realari12',
                read_param='COMPRX',
                data_type='real',
                trns_fn=get_imag,
                base_param=read_param_dict['COMPRX']
                ),
            # WriteParam(name='realari13',
            #     read_param='None',
            #     base_param=read_param_dict['None']
            #     )
        ]
    }
}

del_params = None

fns = [
    PSSE_Fn('three_wnd_winding_data_3',
        make_param_dict(fn_param_dict['three_wnd_winding_data_3']['primaries']),
        make_param_dict(fn_param_dict['three_wnd_winding_data_3']['writables']),
    )
]

del_fn = None

wnd_elem = Element("wnd", ('WIND1NUMBER', 'WIND2NUMBER', 'WIND3NUMBER', 'ID', 'WNDNUM'), read_param_dict, slurp_flags, fns, )