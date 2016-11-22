"""TODO
"""
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"

elem_name = 'genbus'
elem_primaries = ('NUMBER',)
COMMON_READ_FN_KEY = 'genbus'

# flags:
# flag
# 1 - only inservice plant buses (type 2 or 3) with at least one inservice
#       machine. (default)
# 2 - only inservice plant buses (type 2 or 3) including those with no
#       inservice machines.
# 3 - all inservice buses, including those that are not plant buses.
# 4 - all plant buses, including those with no in-service machines
# 5 - all buses, including those that are not plant buses.
slurp_flags = {'flag':4}

read_dict = {'int':['NUMBER','TYPE','AREA','ZONE','OWNER','DUMMY','STATUS',
            'IREG'],
        'real':['BASE','PU','KV','ANGLE','ANGLED','PERCENT','IREGBASE',
            'IREGPU','IREGKV','VSPU','VSKV','RMPCT',
            'PGEN','QGEN','MVA','PMAX','PMIN','QMAX','QMIN','MISMATCH',
            'O_PGEN','O_QGEN','O_MVA','O_PMAX','O_PMIN','O_QMAX','O_QMIN',
            'O_MISMATCH'],
        'cplx':['VOLTAGE','PQGEN','MISMATCH','O_PQGEN','O_MISMATCH'],
        'char':['NAME','EXNAME','IREGNAME','IREGEXNAME']
        }


write_fns = {'plant_data':{
        'primaries':[
            {'name':'i', 'read_name':'NUMBER'},
            ],
        'writables':[
            {'name':'intgar1','read_name':'IREG'},
            {'name':'realar1','read_name':'VSPU'},
            {'name':'realar2','read_name':'RMPCT'},
            ]
        },
    }

del_fn = {'purgplnt':{
        'primaries':[
            {'name':'frmbus',  'read_name':'NUMBER'},
            ],
        'writables':[]
        }
        }
