"""TODO
"""
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"

elem_name = 'mach'
elem_primaries = ('NUMBER','ID')
COMMON_READ_FN_KEY = 'mach'

slurp_flags = {'flag':4}

read_dict = {'int':['NUMBER','STATUS','WMOD','OWNERS','OWN1','OWN2','OWN3','OWN4'],
        'real':['FRACT1','FRACT2','FRACT3','FRACT4','PERCENT','MBASE',
            'GENTAP','WPF','PGEN','QGEN','MVA','PMAX','PMIN','QMAX','QMIN',
            'O_PGEN','O_QGEN','O_MVA','O_PMAX','O_PMIN','O_QMAX','O_QMIN'],
        'cplx':['ZSORCE','XTRAN','ZPOS','ZNEG','ZZERO','PQGEN','O_PQGEN'],
        'char':['ID','NAME','EXNAME']
        }


write_fns = {'machine_data_2':{
        'primaries':[
            {'name':'i', 'read_name':'NUMBER'},
            {'name':'id','read_name':'ID'}
            ],
        'writables':[
            {'name':'intgar1','read_name':'STATUS'},
            {'name':'intgar2','read_name':'OWN1'},
            {'name':'intgar3','read_name':'OWN2'},
            {'name':'intgar4','read_name':'OWN3'},
            {'name':'intgar5','read_name':'OWN4'},
            {'name':'intgar6','read_name':'WMOD'},

            {'name':'realar1','read_name':'PGEN'},
            {'name':'realar2','read_name':'QGEN'},
            {'name':'realar3','read_name':'QMAX'},
            {'name':'realar4','read_name':'QMIN'},
            {'name':'realar5','read_name':'PMAX'},
            {'name':'realar6','read_name':'PMIN'},
            {'name':'realar7','read_name':'MBASE'},
            {'name':'realar8','read_name':'ZSORCE','trns_fn':'get_real','data_type':'real'},
            {'name':'realar9','read_name':'ZSORCE','trns_fn':'get_imag','data_type':'real'},
            {'name':'realar10','read_name':'XTRAN','trns_fn':'get_real','data_type':'real'},
            {'name':'realar11','read_name':'XTRAN','trns_fn':'get_imag','data_type':'real'},
            {'name':'realar12','read_name':'GENTAP'},
            {'name':'realar13','read_name':'FRACT1'},
            {'name':'realar14','read_name':'FRACT2'},
            {'name':'realar15','read_name':'FRACT3'},
            {'name':'realar16','read_name':'FRACT4'},
            {'name':'realar17','read_name':'WPF'},
            ]
        },
    }

del_fn = {'purgmac':{
        'primaries':[
            {'name':'frmbus',  'read_name':'NUMBER'},
            {'name':'id','read_name':'ID'}
            ],
        'writables':[]
        }
        }
