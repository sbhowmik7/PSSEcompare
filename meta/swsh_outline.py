"""TODO
"""
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"

elem_name = 'swsh'
elem_primaries = ('NUMBER',)
COMMON_READ_FN_KEY = 'fxshunt'

slurp_flags = {'flag':4}

read_dict = {'int':['NUMBER','TYPE','AREA','ZONE','OWNER','DUMMY','MODE',
             'STATUS',
            # Bug: ADJMETHOD is listed as 'ADJM' in the PSSEAPI and is invalid.
             'ADJMETHOD',
            'IREG','BLOCKS',
            'STEPSBLOCK1','STEPSBLOCK2','STEPSBLOCK3','STEPSBLOCK4',
            'STEPSBLOCK5','STEPSBLOCK6','STEPSBLOCK7','STEPSBLOCK8'],
        'real':['BASE','PU','KV','ANGLE','ANGLED','VSWHI','VSWLO','RMPCT',
            'PU_BSWZERO',
            'PUBZERBLOCK1','PUBZERBLOCK2','PUBZERBLOCK3','PUBZERBLOCK4',
            'PUBZERBLOCK5','PUBZERBLOCK6','PUBZERBLOCK7','PUBZERBLOCK8',
            'BSWNOM','BSWMAX','BSWMIN','BSWACT','BSWZERO',
            'BSTPBLOCK1','BSTPBLOCK2','BSTPBLOCK3','BSTPBLOCK4',
            'BSTPBLOCK5','BSTPBLOCK6','BSTPBLOCK7','BSTPBLOCK8',
            'BZERBLOCK1','BZERBLOCK2','BZERBLOCK3','BZERBLOCK4',
            'BZERBLOCK5','BZERBLOCK6','BZERBLOCK7','BZERBLOCK8',
            'MISMATCH',
            'O_BSTPBLOCK1','O_BSTPBLOCK2','O_BSTPBLOCK3','O_BSTPBLOCK4',
            'O_BSTPBLOCK5','O_BSTPBLOCK6','O_BSTPBLOCK7','O_BSTPBLOCK8',
            'O_BZERBLOCK1','O_BZERBLOCK2','O_BZERBLOCK3','O_BZERBLOCK4',
            'O_BZERBLOCK5','O_BZERBLOCK6','O_BZERBLOCK7','O_BZERBLOCK8',
            'O_MISMATCH'
            ],
        'cplx':['VOLTAGE','YSWACT','MISMATCH','O_YSWACT','O_MISMATCH'],

        # VSCNAME only returned for devices with 'MODE=4'
        # FACTSNAME only returned for devices with 'MODE=6'
        # DEVICENAME only returned for devices with 'MODE=4' or 'MODE=6'
        'char':['VSCNAME','FACTSNAME','DEVICENAME','NAME','EXNAME','IREGNAME',
            'IREGEXNAME']
        }


write_fns = {'switched_shunt_data_3':{
        'primaries':[
            {'name':'i', 'read_name':'NUMBER'},
            ],
        'writables':[
            {'name':'intgar1','read_name':'STEPSBLOCK1'},
            {'name':'intgar2','read_name':'STEPSBLOCK2'},
            {'name':'intgar3','read_name':'STEPSBLOCK3'},
            {'name':'intgar4','read_name':'STEPSBLOCK4'},
            {'name':'intgar5','read_name':'STEPSBLOCK5'},
            {'name':'intgar6','read_name':'STEPSBLOCK6'},
            {'name':'intgar7','read_name':'STEPSBLOCK7'},
            {'name':'intgar8','read_name':'STEPSBLOCK8'},
            {'name':'intgar9','read_name':'MODE'},
            {'name':'intgar10','read_name':'IREG'},
            {'name':'intgar11','read_name':'STATUS'},
            {'name':'intgar12','read_name':'ADJMETHOD'},

            {'name':'realar1','read_name':'BSTPBLOCK1'},
            {'name':'realar2','read_name':'BSTPBLOCK2'},
            {'name':'realar3','read_name':'BSTPBLOCK3'},
            {'name':'realar4','read_name':'BSTPBLOCK4'},
            {'name':'realar5','read_name':'BSTPBLOCK5'},
            {'name':'realar6','read_name':'BSTPBLOCK6'},
            {'name':'realar7','read_name':'BSTPBLOCK7'},
            {'name':'realar8','read_name':'BSTPBLOCK8'},
            {'name':'realar9','read_name':'VSWHI'},
            {'name':'realar10','read_name':'VSWLO'},
            {'name':'realar11','read_name':'BSWNOM'},
            {'name':'realar12','read_name':'RMPCT'},

            # VSCNAME is only returned for devices with "MODSW=4"
            {'name':'rmidnt','read_name':'VSCNAME'},
            ]
        },
    }

del_fn = {'purgsws':{
        'primaries':[
            {'name':'frmbus',  'read_name':'NUMBER'},
            ],
        'writables':[]
        }
        }
