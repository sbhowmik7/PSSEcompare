"""TODO
"""
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"

elem_name = 'trn'
elem_primaries = ('FROMNUMBER','TONUMBER','ID')
COMMON_READ_FN_KEY = 'trn'

slurp_flags = {'ties':3,'flag':2}

read_dict = {'int':['FROMNUMBER','TONUMBER','STATUS','METERNUMBER',
            'NMETERNUMBER','OWNERS','OWN1','OWN2','OWN3','OWN4',
            # trn specfic ints (previous are common to branch data).
            'ICONTNUMBER','WIND1NUMBER','WIND2NUMBER','TABLE','CODE',
            'NTPOSN','CW','CZ','CM','CNXCOD','TPSTT','ANSTT'],
        'real':['AMPS','PUCUR','PCTRATE','PCTRATEA','PCTRATEB','PCTRATEC',
            'PCTMVARATE','PCTMVARATEA','PCTMVARATEB','PCTMVARATEC',
            'PCTCORPRATE','PCTCORPRATEA','PCTCORPRATEB','PCTCORPRATEC',
            'MAXPCTRATE','MAXPCTRATEA','MAXPCTRATEB','MAXPCTRATEC',
            'MXPCTMVARAT','MXPCTMVARATA','MXPCTMVARATB','MXPCTMVARATC',
            'MXPCTCRPRAT','MXPCTCRPRATA','MXPCTCRPRATB','MXPCTCRPRATC',
            'FRACT1','FRACT2','FRACT3','FRACT4',
            'RATE','RATEA','RATEB','RATEC',
            # trn specific reals (previous are common to branch data).
            'RATIO','RATIOCW','RATIO2','RATIO2CW','ANGLE','RMAX','RMAXCW',
            'RMIN','RMINCW','VMAX','VMAXKV','VMIN','VMINKV','STEP','STEPCW',
            'NOMV1','NOMV2','SBASE1',
            # common reals with brn (following vals returned as MW,Mvar or MVA)
            'P','Q','MVA','MAXMVA','PLOSS','QLOSS',
            'O_P','O_Q','O_MVA','O_MAXMVA','O_PLOSS','O_QLOSS'],

        'cplx':['RXACT','RXACTCZ','RXNOM','RXNOMCZ','YMAG','YMAGCM',
            'COMPRX','RXZERO','ZGRND','ZGRND2',
            # common cplx keywords with brn.
            'PQ','PQLOSS','O_PQ','O_PQLOSS'],

        'char':['ID','FROMNAME','FROMEXNAME','TONAME','TOEXNAME',
            'METERNAME','METEREXNAME','NMETERNAME','NMETEREXNAME',
            # trn specific keywords.
            'ICONTNAME','ICONTEXNAME','WIND1NAME','WIND1EXNAME',
            'WIND2NAME','WIND2EXNAME','XFRNAME']
        }


write_fns = {'two_winding_data_3':{
        'primaries':[
            # brn - frmbus
            {'name':'i',  'read_name':'FROMNUMBER'},
            # brn - tobus
            {'name':'j',  'read_name':'TONUMBER'},
            # brn - ckt
            {'name':'ckt','read_name':'ID'}
            ],
        'writables':[
            # trn - trname
            {'name':'name','read_name':'XFRNAME'},

            # brn - stat
            {'name':'intgar1','read_name':'STATUS'},
            # brn - metbus
            {'name':'intgar2','read_name':'METERNUMBER'},
            # brn - owner
            {'name':'intgar3','read_name':'OWN1'},
            {'name':'intgar4','read_name':'OWN2'},
            {'name':'intgar5','read_name':'OWN3'},
            {'name':'intgar6','read_name':'OWN4'},
            # trn = ntaps
            {'name':'intgar7','read_name':'NTPOSN'},
            # trn - table
            {'name':'intgar8','read_name':'TABLE'},
            # trn - wind1
            {'name':'intgar9','read_name':'WIND1NUMBER'},
            # trn - conbus
            {'name':'intgar10','read_name':'ICONTNUMBER'},

            # SICOD1: Not sure how to read this value in. It is set to a
            # negative when the bus being controlled is on the winding1 side of
            # the transformer. ICONTNUMBER must be set for this to have any
            # effect.
            {'name':'intgar11','read_name':None},

            # trn - cntl ???
            {'name':'intgar12','read_name':'CODE'},

            #
            {'name':'intgar13','read_name':'CW'},
            {'name':'intgar14','read_name':'CZ'},
            {'name':'intgar15','read_name':'CM'},

            # Need to figure out if the CZ, CM, CW options alter the values
            # being read by the API and if they need to be corrected for.
            {'name':'realari1','read_name':'RXNOM','trns_fn':'get_real','data_type':'real'},
            {'name':'realari2','read_name':'RXNOM','trns_fn':'get_imag','data_type':'real'},
            {'name':'realari3','read_name':'SBASE1'},
            {'name':'realari4','read_name':'RATIO'},
            {'name':'realari5','read_name':'NOMV1'},
            {'name':'realari6','read_name':'ANGLE'},
            {'name':'realari7','read_name':'RATIO2'},
            {'name':'realari8','read_name':'NOMV2'},
            {'name':'realari9','read_name':'RATEA'},
            {'name':'realari10','read_name':'RATEB'},
            {'name':'realari11','read_name':'RATEC'},
            {'name':'realari12','read_name':'FRACT1'},
            {'name':'realari13','read_name':'FRACT2'},
            {'name':'realari14','read_name':'FRACT3'},
            {'name':'realari15','read_name':'FRACT4'},
            {'name':'realari16','read_name':'YMAG','trns_fn':'get_real','data_type':'real'},
            {'name':'realari17','read_name':'YMAG','trns_fn':'get_imag','data_type':'real'},
            {'name':'realari18','read_name':'RMAX'},
            {'name':'realari19','read_name':'RMIN'},
            {'name':'realari20','read_name':'VMAX'},
            {'name':'realari21','read_name':'VMIN'},
            {'name':'realari22','read_name':'COMPRX','trns_fn':'get_real','data_type':'real'},
            {'name':'realari23','read_name':'COMPRX','trns_fn':'get_imag','data_type':'real'},

            # CNXA1: winding connection angle (0.0 by default).
            # Used with adjustment control mode 5 (unsymmatric
            # phase shift control of active power) implemented in
            # PSSE version 32.1.
            {'name':'realari24','read_name':None},
            ]
        },
    }

del_fn = {'purgbrn':{
        'primaries':[
            # brn - frmbus
            {'name':'frmbus',  'read_name':'FROMNUMBER'},
            # brn - tobus
            {'name':'tobus',  'read_name':'TONUMBER'},
            # brn - ckt
            {'name':'ckt','read_name':'ID'}
            ],
        'writables':[]
        }
        }
