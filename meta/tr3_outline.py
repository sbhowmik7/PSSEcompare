"""TODO
"""
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"

elem_name = 'tr3'
elem_primaries = ('WIND1NUMBER','WIND2NUMBER','WIND3NUMBER','ID')
COMMON_READ_FN_KEY = 'tr3'

slurp_flags = {'ties':3, 'flag':2}

additional_imports = 'from elem_obj import Parameter, tr3_Elem'

special_elem_class = 'tr3_Elem'

read_dict = {'int':['WIND1NUMBER','WIND2NUMBER','WIND3NUMBER',
            # common to tnr (2 winding transformer) args
            'STATUS', 'NMETERNUMBER','OWNERS','OWN1','OWN2','OWN3','OWN4',
            'CW','CZ','CM','CNXCOD'],
        'real':['FRACT1','FRACT2','FRACT3','FRACT4','VMSTAR','ANSTAR',
            'PLOSS','QLOSS','O_PLOSS','O_QLOSS'],
        'cplx':['RX1-2ACT','RX1-2ACTCZ','RX1-2NOM','RX1-2NOMCZ',
            'RX2-3ACT','RX2-3ACTCZ','RX2-3NOM','RX2-3NOMCZ',
            'RX3-1ACT','RX3-1ACTCZ','RX3-1NOM','RX3-1NOMCZ',
            'YMAG','YMAGCM','ZGRND','PQLOSS','O_PQLOSS'],
        'char':['ID', 'WIND1NAME','WIND1EXNAME','WIND2NAME','WIND2EXNAME',
            'WIND3NAME','WIND3EXNAME','NMETERNAME','NMETEREXNAME','XFRNAME']
        }

derived_reads = {'real':['SBASE1-2','SBASE2-3','SBASE3-1']}

write_fns = {'three_wnd_impedance_data':{
        'primaries':[
            {'name':'i',  'read_name':'WIND1NUMBER'},
            {'name':'j',  'read_name':'WIND2NUMBER'},
            {'name':'k',  'read_name':'WIND3NUMBER'},
            {'name':'ckt','read_name':'ID'}
            ],
        'writables':[
            {'name':'name','read_name':'XFRNAME'},

            {'name':'intgar1','read_name':'OWN1'},
            {'name':'intgar2','read_name':'OWN2'},
            {'name':'intgar3','read_name':'OWN3'},
            {'name':'intgar4','read_name':'OWN4'},
            {'name':'intgar5','read_name':'CW'},
            {'name':'intgar6','read_name':'CZ'},
            {'name':'intgar7','read_name':'CM'},
            {'name':'intgar8','read_name':'STATUS'},
            {'name':'intgar9','read_name':'NMETERNUMBER'},
            {'name':'intgar10','read_name':'WIND1NUMBER'},
            {'name':'intgar11','read_name':'WIND2NUMBER'},
            {'name':'intgar12','read_name':'WIND3NUMBER'},

            # Need to figure out if the CZ, CM, CW options alter the values
            # being read by the API and if they need to be corrected for.
            {'name':'realari1','read_name':'RX1-2NOM','trns_fn':'get_real','data_type':'real'},
            {'name':'realari2','read_name':'RX1-2NOM','trns_fn':'get_imag','data_type':'real'},
            {'name':'realari3','read_name':'RX2-3NOM','trns_fn':'get_real','data_type':'real'},
            {'name':'realari4','read_name':'RX2-3NOM','trns_fn':'get_imag','data_type':'real'},
            {'name':'realari5','read_name':'RX3-1NOM','trns_fn':'get_real','data_type':'real'},
            {'name':'realari6','read_name':'RX3-1NOM','trns_fn':'get_imag','data_type':'real'},

            # The SBASE is not specified under the tr3 outline. The winding
            # specific API has an SBASE read parameter.
            # They are derived by making a call to the wnd api.
            {'name':'realari7','read_name':'SBASE1-2',},
            {'name':'realari8','read_name':'SBASE2-3'},
            {'name':'realari9','read_name':'SBASE3-1'},

            {'name':'realari10','read_name':'YMAG','trns_fn':'get_real','data_type':'real'},
            {'name':'realari11','read_name':'YMAG','trns_fn':'get_imag','data_type':'real'},
            {'name':'realari12','read_name':'FRACT1'},
            {'name':'realari13','read_name':'FRACT2'},
            {'name':'realari14','read_name':'FRACT3'},
            {'name':'realari15','read_name':'FRACT4'},
            {'name':'realari16','read_name':'VMSTAR'},
            {'name':'realari17','read_name':'ANSTAR'},
            ]
        },
    }

del_fn = {'purg3wnd':{
        'primaries':[
            {'name':'frmbus',  'read_name':'WIND1NUMBER'},
            {'name':'tobus1',  'read_name':'WIND2NUMBER'},
            {'name':'tobus2',  'read_name':'WIND3NUMBER'},
            {'name':'ckt','read_name':'ID'}
            ],
        'writables':[]
            }
        }
