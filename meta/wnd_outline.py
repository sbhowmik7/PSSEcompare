"""TODO
"""
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"

elem_name = 'wnd'
elem_primaries = ('WIND1NUMBER','WIND2NUMBER','WIND3NUMBER','ID','WNDNUM')
COMMON_READ_FN_KEY = 'wnd'

slurp_flags = {'ties':3, 'flag':3}

read_dict = {'int':['WNDBUSNUMBER','OTHER1NUMBER','OTHER2NUMBER',
            'WNDNUM','WIND1NUMBER','WIND2NUMBER','WIND3NUMBER',
            # common to tnr (2 winding transformer) args
            'NMETERNUMBER','STATUS','OWNERS','OWN1','OWN2','OWN3','OWN4',
            'ICONTNUMBER','TABLE','CODE','NTPOSN',
            'CW','CZ','CM','CNXCOD','TPSTT','ANSTT'],
        'real':['AMPS','PUCUR','PCTRATE','PCTRATEA','PCTRATEB','PCTRATEC',
            'PCTMVARATE','PCTMVARATEA','PCTMVARATEB','PCTMVARATEC',
            'PCTCORPRATE','PCTCORPRATEA','PCTCORPRATEB','PCTCORPRATEC',
            'MAXPCTRATE','MAXPCTRATEA','MAXPCTRATEB','MAXPCTRATEC',
            'MXPCTMVARAT','MXPCTMVARATA','MXPCTMVARATB','MXPCTMVARATC',
            'MXPCTCRPRAT','MXPCTCRPRATA','MXPCTCRPRATB','MXPCTCRPRATC',
            'FRACT1','FRACT2','FRACT3','FRACT4',
            'RATE','RATEA','RATEB','RATEC',
            'RATIO','RATIOCW','ANGLE','RMAX','RMAXCW',
            'RMIN','RMINCW','VMAX','VMAXKV','VMIN','VMINKV','STEP','STEPCW',
            'NOMV','SBASE',
            'P','Q','MVA','MAXMVA','PLOSS','QLOSS',
            'O_P','O_Q','O_MVA','O_MAXMVA','O_PLOSS','O_QLOSS'],
        'cplx':['RXACT','RXNOM','COMPRX','RXZERO',
            'PQ','PQLOSS','O_PQ','O_PQLOSS'],
        'char':['ID', 'WNDBUSNAME','WNDBUSEXNAME','OTHER1NAME','OTHER1EXNAME',
            'OTHER2NAME','OTHER2EXNAME','WIND1NAME','WIND1EXNAME',
            'WIND2NAME','WIND2EXNAME','WIND3NAME','WIND3EXNAME',
            'NMETERNAME','NMETEREXNAME','XFRNAME']
        }

write_fns = {'three_wnd_winding_data_3':{
        'primaries':[
            {'name':'i',  'read_name':'WIND1NUMBER'},
            {'name':'j',  'read_name':'WIND2NUMBER'},
            {'name':'k',  'read_name':'WIND3NUMBER'},
            {'name':'ckt','read_name':'ID'},
            {'name':'warg','read_name':'WNDNUM'},
            ],
        'writables':[
            {'name':'intgar1','read_name':'NTPOSN'},
            {'name':'intgar2','read_name':'TABLE'},
            {'name':'intgar3','read_name':'ICONTNUMBER'},

            # SICODi: Not sure how to read this value in. It is set to a
            # negative when the bus being controlled is on the wind bus side of
            # the transformer. ICONTNUMBER must be set for this to have any
            # effect.
            {'name':'intgar4','read_name':None},

            {'name':'intgar5','read_name':'CODE'},

            # Need to figure out if the CZ, CM, CW options alter the values
            # being read by the API and if they need to be corrected for.
            {'name':'realari1','read_name':'RATIO'},
            {'name':'realari2','read_name':'NOMV'},
            {'name':'realari3','read_name':'ANGLE'},
            {'name':'realari4','read_name':'RATEA'},
            {'name':'realari5','read_name':'RATEB'},
            {'name':'realari6','read_name':'RATEC'},
            {'name':'realari7','read_name':'RMAX'},
            {'name':'realari8','read_name':'RMIN'},
            {'name':'realari9','read_name':'VMAX'},
            {'name':'realari10','read_name':'VMIN'},
            {'name':'realari11','read_name':'COMPRX','trns_fn':'get_real','data_type':'real'},
            {'name':'realari12','read_name':'COMPRX','trns_fn':'get_imag','data_type':'real'},

            # CNXA1: winding connection angle (0.0 by default).
            # Used with adjustment control mode 5 (unsymmatric
            # phase shift control of active power) implemented in
            # PSSE version 32.1.
            {'name':'realari13','read_name':None}
            ]
        },
    }

del_fn = None
