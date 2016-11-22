"""TODO
"""
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"

elem_name = 'load'
elem_primaries = ('NUMBER','ID')
COMMON_READ_FN_KEY = 'load'

slurp_flags = {'flag':4}

read_dict = {'int':['NUMBER','AREA','ZONE','OWNER','STATUS'],#,'SCALE'],
        'real':['MVAACT','MVANOM','ILACT','ILNOM','YLACT','YLNOM','TOTALACT',
            'TOTALNOM','O_MVAACT','O_MVANOM','O_ILACT','O_YLACT','O_YLNOM',
            'O_TOTALACT','O_TOTALNOM'],
        'cplx':['MVAACT','MVANOM','ILACT','ILNOM','YLACT','YLNOM','TOTALACT',
            'TOTALNOM','O_MVAACT','O_MVANOM','O_ILACT','O_YLACT','O_YLNOM',
            'O_TOTALACT','O_TOTALNOM'],
        'char':['ID','NAME','EXNAME']
        }


write_fns = {'load_data_3':{
        'primaries':[
            {'name':'i', 'read_name':'NUMBER'},
            {'name':'id','read_name':'ID'}
            ],
        'writables':[
            {'name':'intgar1','read_name':'STATUS'},
            {'name':'intgar2','read_name':'AREA'},
            {'name':'intgar3','read_name':'ZONE'},
            {'name':'intgar4','read_name':'OWNER'},
            {'name':'intgar5','read_name':'SCALE'},
            {'name':'realar1','read_name':'MVANOM', 'trns_fn':'get_real','data_type':'real'},
            {'name':'realar2','read_name':'MVANOM', 'trns_fn':'get_imag','data_type':'real'},
            {'name':'realar3','read_name':'ILNOM',  'trns_fn':'get_real','data_type':'real'},
            {'name':'realar4','read_name':'ILNOM',  'trns_fn':'get_imag','data_type':'real'},
            {'name':'realar5','read_name':'YLNOM',  'trns_fn':'get_real','data_type':'real'},
            {'name':'realar6','read_name':'YLNOM',  'trns_fn':'get_imag','data_type':'real'},
            ]
        },
    }


del_fn = {'purgload':{
        'primaries':[
            {'name':'frmbus',  'read_name':'NUMBER'},
            {'name':'id','read_name':'ID'}
            ],
        'writables':[]
        }
        }
