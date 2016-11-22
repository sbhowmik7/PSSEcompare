"""brn: element branch
"""
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"

elem_name = 'fxshunt'
elem_primaries = ('NUMBER','ID')
COMMON_READ_FN_KEY = 'fxshunt'

slurp_flags = {'flag':4}

read_dict = {'int':['NUMBER','STATUS'],
        'real':['PU_GBZERO','SHUNTACT','SHUNTNOM','GBZERO','O_SHUNTACT','O_SHUNTNOM','O_GBZERO'],
        'cplx':['PU_GBZERO','SHUNTACT','SHUNTNOM','GBZERO','O_SHUNTACT','O_SHUNTNOM','O_GBZERO'],
        'char':['ID','NAME','EXNAME']
        }


write_fns = {'shunt_data':{
        'primaries':[
            {'name':'i', 'read_name':'NUMBER'},
            {'name':'id','read_name':'ID'}
            ],
        'writables':[
            {'name':'intgar1','read_name':'STATUS'},
            {'name':'realar1','read_name':'SHUNTNOM', 'trns_fn':'get_real','data_type':'real'},
            {'name':'realar2','read_name':'SHUNTNOM', 'trns_fn':'get_imag','data_type':'real'},
            ]
        },
    }

del_fn = {'purgshunt':{
        'primaries':[
            {'name':'frmbus',  'read_name':'NUMBER'},
            {'name':'id','read_name':'ID'}
            ],
        'writables':[]
        }
        }
