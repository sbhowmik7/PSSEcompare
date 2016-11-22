import textwrap
from elem_obj import ReadParam, WriteParam, PSSE_Fn, Element, make_param_dict

# template to fill in:
# ReadParam(name=,
#     data_type=,
#     read_fn_key=,
#     read_fn=,
#     display_name=,
#     description=textwrap.dedent("""\
#
#             """)
#     ),

COMMON_READ_FN_KEY = 'bus'
"""brn: element branch
"""
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"

# flags:
# flag = 1 (default) only inservice buses.
# flag = 2 all buses.
slurp_flags = {'flag':2}

# When compiling this list, a conflict will cause an exception. Always test the
# list when making changes to these files. It starts off life as a list as it
# requires less typing and key conflicts can be detected later (instead of just
# written over)
read_params=[
#  ----- int data

ReadParam(name='NUMBER',
    data_type='int',
    read_fn_key=COMMON_READ_FN_KEY,
    display_name='number',
    description=textwrap.dedent("""\
            Bus number (1 through 999997). No default allowed.
            """)
    ),
ReadParam(name='TYPE',
    data_type='int',
    read_fn_key=COMMON_READ_FN_KEY,
    display_name='type',
    description=textwrap.dedent("""\
            IDE Bus type code:
                1 for a load bus or passive node (no generator boundary condition)
                2 for a generator or plant bus (either voltage regulating or fixed Mvar)
                3 for a swing bus
                4 for a disconnected (isolated) bus
            1 by default.
            """)
    ),
ReadParam(name='AREA',
    data_type='int',
    read_fn_key=COMMON_READ_FN_KEY,
    display_name='area',
    description=textwrap.dedent("""\
            Area number (1 through 9999). AREA = 1 by default.
        """)
    ),
ReadParam(name='ZONE',
    data_type='int',
    read_fn_key=COMMON_READ_FN_KEY,
    display_name='zone',
    description=textwrap.dedent("""\
            Zone number (1 through 9999). ZONE = 1 by default.
            """)
    ),
ReadParam(name='OWNER',
    data_type='int',
    read_fn_key=COMMON_READ_FN_KEY,
    display_name='owner',
    description=textwrap.dedent("""\
            Owner number (1 through 9999). OWNER = 1 by default.
            """)
    ),
ReadParam(name='DUMMY',
    data_type='int',
    read_fn_key=COMMON_READ_FN_KEY,
    display_name='dummy',
    description=textwrap.dedent("""\
            Returns 1 if the bus is a dummy bus of a multisection line, or 0 if
            it is not.
            """)
    ),

#  ----- real data
ReadParam(name='BASE',
    data_type='real',
    read_fn_key=COMMON_READ_FN_KEY,
    display_name='basekv',
    description=textwrap.dedent("""\
            Bus base voltage; entered in kV. BASKV = 0.0 by default.
            """)
    ),
    #Commented out since there is no need to compare final voltage/angle values from PF
# ReadParam(name='PU',
#     data_type='real',
#     read_fn_key=COMMON_READ_FN_KEY,
#     display_name='pu',
#     description=textwrap.dedent("""\
#             WRITE: VM, bus voltage magnitude in pu. (1.0 by default)
#             READ:  Actual bus voltage magnitude, in pu.
#             """)
#     ),
# ReadParam(name='KV',
#     data_type='real',
#     read_fn_key=COMMON_READ_FN_KEY,
#     display_name='kV',
#     description=textwrap.dedent("""\
#             Actual bus voltage magnitude, in kV (in pu if base voltage is 0.0).
#             """)
#     ),
# ReadParam(name='ANGLE',
#     data_type='real',
#     read_fn_key=COMMON_READ_FN_KEY,
#     display_name='angle (rad)',
#     description=textwrap.dedent("""\
#             Bus voltage phase angle, in radians.
#             """)
#     ),
# ReadParam(name='ANGLED',
#     data_type='real',
#     read_fn_key=COMMON_READ_FN_KEY,
#     display_name='angle (deg)',
#     description=textwrap.dedent("""\
#             Bus voltage phase angle, in degrees.
#             """)
#     ),
# -- real parameters "MISMATCH" and "O_MISMATCH" are superseded by the cplx
#        parameters of the same name.
# ReadParam(name='MISMATCH',
#     data_type='real',
#     read_fn_key=COMMON_READ_FN_KEY,
#     display_name='mismatch',
#     description=textwrap.dedent("""\
#             Bus mismatch in MVA (0.0 if bus type code > 3).
#             """)
#     ),
# ReadParam(name='O_MISMATCH',
#     data_type='real',
#     read_fn_key=COMMON_READ_FN_KEY,
#     display_name='o_mismatch',
#     description=textwrap.dedent("""\
#             Bus mismatch, in units determined by the power output option
#             setting (0.0 if bus type code > 3).
#             """)
#     ),

#  ----- cplx data

# ReadParam(name='VOLTAGE',
#     data_type='cplx',
#     read_fn_key=COMMON_READ_FN_KEY,
#     display_name='voltage cplx',
#     description=textwrap.dedent("""\
#             Actual bus voltage, in pu, rectangular coordinates.
#             """)
#     ),
ReadParam(name='SHUNTACT',
    data_type='cplx',
    read_fn_key=COMMON_READ_FN_KEY,
    description=textwrap.dedent("""\
            Actual total in-service fixed bus shunt, in MW and Mvar.
            """)
    ),
ReadParam(name='O_SHUNTACT',
    data_type='cplx',
    read_fn_key=COMMON_READ_FN_KEY,
    description=textwrap.dedent("""\
            Actual total in-service fixed bus shunt, in units determined by the
            power output option setting.
            """)
    ),
ReadParam(name='SHUNTNOM',
    data_type='cplx',
    read_fn_key=COMMON_READ_FN_KEY,
    description=textwrap.dedent("""\
            Nominal total in-service fixed bus shunt, in MW and Mvar at 1.0 pu
            voltage.
            """)
    ),
ReadParam(name='O_SHUNTNOM',
    data_type='cplx',
    read_fn_key=COMMON_READ_FN_KEY,
    description=textwrap.dedent("""\
            Nominal total in-service fixed bus shunt, in units determined by
            the power output option setting at 1.0 pu voltage.
            """)
    ),
ReadParam(name='SHUNTN',
    data_type='cplx',
    read_fn_key=COMMON_READ_FN_KEY,
    description=textwrap.dedent("""\
            Negative sequence shunt (pu, nominal).
            """)
    ),
ReadParam(name='SHUNTZ',
    data_type='cplx',
    read_fn_key=COMMON_READ_FN_KEY,
    description=textwrap.dedent("""\
            Zero sequence shunt (pu, nominal).
            """)
    ),
ReadParam(name='MISMATCH',
    data_type='cplx',
    read_fn_key=COMMON_READ_FN_KEY,
    description=textwrap.dedent("""\
            Bus mismatch, in MW and Mvar (0.0 if bus type code > 3).
            """)
    ),
ReadParam(name='O_MISMATCH',
    data_type='cplx',
    read_fn_key=COMMON_READ_FN_KEY,
    description=textwrap.dedent("""\
            Bus mismatch, in units determined by the power output option
            setting (0.0 if bus type code > 3).
            """)
    ),

#  ----- char data

ReadParam(name='NAME',
    data_type='char',
    read_fn_key=COMMON_READ_FN_KEY,
    display_name='name',
    description=textwrap.dedent("""\
            Bus name (12 characters).
            """)
    ),
ReadParam(name='EXNAME',
    data_type='char',
    read_fn_key=COMMON_READ_FN_KEY,
    display_name='extended name',
    description=textwrap.dedent("""\
            Extended bus name (18 characters).
            """)
    ),
]

read_param_dict = make_param_dict(read_params)

write_primary_list = [
    WriteParam(name='i',
        read_param='NUMBER',
        base_param=read_param_dict['NUMBER']
        ),
    ]

write_param_list = [
    WriteParam(name='name',
        read_param='NAME',
        base_param=read_param_dict['NAME']
        ),
    WriteParam(name='intgar1',
        read_param='TYPE',
        base_param=read_param_dict['TYPE']
        ),
    WriteParam(name='intgar2',
        read_param='AREA',
        base_param=read_param_dict['AREA']
        ),
    WriteParam(name='intgar3',
        read_param='ZONE',
        base_param=read_param_dict['ZONE']
        ),
    WriteParam(name='intgar4',
        read_param='OWNER',
        base_param=read_param_dict['OWNER']
        ),
    WriteParam(name='realar1',
        read_param='BASE',
        base_param=read_param_dict['BASE']
        ),
    # WriteParam(name='realar2',
    #     read_param='PU',
    #     base_param=read_param_dict['PU']
    #     ),
    # WriteParam(name='realar3',
    #     read_param='ANGLED',
    #     base_param=read_param_dict['ANGLED']
    #     ),
    ]

write_primary_dict = make_param_dict(write_primary_list)
write_param_dict = make_param_dict(write_param_list)

fns = [PSSE_Fn(name='bus_data_3',
    prim_ordered_dict=write_primary_dict,
    write_ordered_dict=write_param_dict,
    )
    ]


bus_elem = Element('bus', ('NUMBER',), read_param_dict, slurp_flags, fns)

if __name__ == "__main__":
    print bus_elem
