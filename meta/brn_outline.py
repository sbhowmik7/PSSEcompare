"""brn: element branch
"""
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"

elem_name = 'brn'
elem_primaries = ('FROMNUMBER','TONUMBER','ID')
COMMON_READ_FN_KEY = 'brn'

# flags:
# ties - the branches to be included - ignored if sid = -1
# 1 - interior subsystem branches only (default)
# 2 - only tie branches
# 3 - all branches
# flag:
# 1 - only inservice, non-transformer branches (default)
# 2 - all non-transformer branches
# 3 - only inservice non-transformer branches and two-winding transformers
# 4 - all inservice non-transformer branches and two-winding transformers
# 5 - only inservice two-winding transformers
# 6 - all two winding transformers.
slurp_flags = {'ties':3, 'flag':2}

read_dict = {'int':['FROMNUMBER','TONUMBER','STATUS','METERNUMBER',
            'NMETERNUMBER','OWNERS','OWN1','OWN2','OWN3','OWN4'],
        'real':['AMPS','PUCUR','PCTRATE','PCTRATEA','PCTRATEB','PCTRATEC',
            'PCTMVARATE','PCTMVARATEA','PCTMVARATEB','PCTMVARATEC',
            'PCTCORPRATE','PCTCORPRATEA','PCTCORPRATEB','PCTCORPRATEC',
            'MAXPCTRATE','MAXPCTRATEA','MAXPCTRATEB','MAXPCTRATEC',
            'MXPCTMVARAT','MXPCTMVARATA','MXPCTMVARATB','MXPCTMVARATC',
            'MXPCTCRPRAT','MXPCTCRPRATA','MXPCTCRPRATB','MXPCTCRPRATC',
            'FRACT1','FRACT2','FRACT3','FRACT4',
            'RATE','RATEA','RATEB','RATEC',
            'LENGTH','CHARGING','CHARGINGZERO',
            'P','Q','MVA','MAXMVA','PLOSS','QLOSS',
            'O_P','O_Q','O_MVA','O_MAXMVA','O_PLOSS','O_QLOSS'],

        'cplx':['RX','FROMSHNT','TOSHNT','RXZERO','FROMSHNTZERO','TOSHNTZERO',
            'PQ','PQLOSS','O_PQ','O_PQLOSS'],

        'char':['ID','FROMNAME','FROMEXNAME','TONAME','TOEXNAME',
            'METERNAME','METEREXNAME','NMETERNAME','NMETEREXNAME']
        }


write_fns = {'branch_data':{
        'primaries':[
            {'name':'i',  'read_name':'FROMNUMBER'},
            {'name':'j',  'read_name':'TONUMBER'},
            {'name':'ckt','read_name':'ID'}
            ],
        'writables':[
            {'name':'intgar1','read_name':'STATUS'},
            {'name':'intgar2','read_name':'METERNUMBER'},
            {'name':'intgar3','read_name':'OWN1'},
            {'name':'intgar4','read_name':'OWN2'},
            {'name':'intgar5','read_name':'OWN3'},
            {'name':'intgar6','read_name':'OWN4'},

            {'name':'realar1','read_name':'RX','trns_fn':'get_real','data_type':'real'},
            {'name':'realar2','read_name':'RX','trns_fn':'get_imag','data_type':'real'},
            {'name':'realar3','read_name':'CHARGING'},
            {'name':'realar4','read_name':'RATEA'},
            {'name':'realar5','read_name':'RATEB'},
            {'name':'realar6','read_name':'RATEC'},
            {'name':'realar7','read_name':'FROMSHNT','trns_fn':'get_real','data_type':'real'},
            {'name':'realar8','read_name':'FROMSHNT','trns_fn':'get_imag','data_type':'real'},
            {'name':'realar9','read_name':'TOSHNT','trns_fn':'get_real','data_type':'real'},
            {'name':'realar10','read_name':'TOSHNT','trns_fn':'get_imag','data_type':'real'},
            {'name':'realar11','read_name':'LENGTH'},
            {'name':'realar12','read_name':'FRACT1'},
            {'name':'realar13','read_name':'FRACT2'},
            {'name':'realar14','read_name':'FRACT3'},
            {'name':'realar15','read_name':'FRACT4'},
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
