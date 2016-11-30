"""slurp: Reads in the PSSE data case (either sav or raw case) using PSSE API functions for reading
Each elements real, char,integer and complex fields
"""
__author__ = "Sudipto Bhowmik,whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"


import os
import sqlite3
import sys
import subprocess

try:
    import app_settings
except ImportError:
    this_dir = os.path.dirname(__file__)
    sys.path.append(os.path.join(this_dir,'..'))
    import app_settings

import createdb
from elements import elements
# import db_tools
from psse_utils import check_psse_version
# PSSBIN added in app_settings
import psspy

def slurp_element(e, case, slurp_con):
    """
    Given an element (elem_type ex: load). Create records with unique primary key
    (load: Bus no|ID) and all its required fields into the SQlite database
"""
    curs = slurp_con.cursor()

    primary = e.primaries
    options = e.required_writables()
    required = e.required_readables()
    n_primary = len(primary)

    zipper_func = e.map_func(required[n_primary:], options)

    rows = []
    for row in e.slurp(required):
        node = '|'.join([str(val) for val in row[:n_primary]])
        # sql_string = sql_base_str % node
        rows.extend([(node,) + x
            for x in zipper_func(options, row[n_primary:])])

    # the values part of this string is:
    #    (case_id | node | type | option | value)
    # This leaves the "node" position to be filled as a %s.
    sql_string = ("INSERT INTO slurp%s VALUES ( ?, '%s', ?, ?)" %
                  (case, e.elem_name,))
    curs.executemany(sql_string, rows)
    curs.close()

    return len(rows)


def slurp_single_case(filename,case_letter):
    """
    Slurps a single case and initializes each element.
    Stores each row of data with unique keys in to the database
    """
    if not os.path.isfile(filename):
        print "Could not find file %s" %(filename,)
        raise IOError
    fnam,fext = os.path.splitext(filename)
    print '\nReading %s' %filename

    if 'sav' in fext:
        if app_settings.USE_CASPY and run_in_python('slurp.py',filename):
            # test to see if we can use CASPY or it crashes in a subprocess
            import caspy
            import psse_utils as utils
            case = caspy.Savecase(filename)
            assert case.pssopn['IERR'] is 0,'Error using caspy to read in %s: Check savecase version!!' %filename
            utils.fix_caspy_case(case)
        else:
            app_settings.USE_CASPY =False
            print 'Could not use Caspy'
            check_pssedongle()
            psspy.case(filename)
    else:
        check_pssedongle()
        app_settings.USE_CASPY = False
        with open(filename,'r') as fid:
            rawheader=fid.readline()

        pssevers=check_psse_version(rawheader)
        psspy.readrawversion(0,pssevers,filename)

    slurp_con = get_slurp_db_con()
    slurp_con.execute("DELETE FROM slurp%s" %(case_letter,))

    for e in elements.values():
        param_cnt = slurp_element(e, case_letter, slurp_con)
        elem_cnt = param_cnt / len(e.writables)

        if elem_cnt == 1:
            print 'Read in %s %s element.' % (elem_cnt, e.elem_name)
        else:
            print 'Read in %s %s elements.' % (elem_cnt, e.elem_name)

    slurp_con.commit()
    slurp_con.close()

def get_slurp_db_con():
    """Return a database connection to where the slurp data should be saved.
    """
    if app_settings.SLURP_DB == ':memory:':
        slurp_con = createdb.create_independent_slurp_db()
    else:
        slurp_con = sqlite3.connect(app_settings.SLURP_DB)
    return slurp_con

def check_pssedongle():
    try:
        psspy.psseinit(90000)
        return True
    except:
        _, e, _ = sys.exc_info()
        print str(e)
        return False


def slurp(filename,case_letter = None):
    if case_letter:
        try:
            slurp_single_case(filename,case_letter)
        except err:
            print('File read Error: ' + str(err))
            raise

        print("Slurp Finished for case " + case_letter )

def run_in_python(filename,*args,**kwargs):
    python_exec = app_settings.PYTHON_EXEC
    slurp_py = os.path.join(app_settings.APP_DIR,'admin', filename)
    slurp_args = [python_exec, slurp_py]
    slurp_args.extend(args)
    try:
        p=subprocess.Popen(slurp_args)
        output= p.wait()
        if output == 0:
            return True
        else:
            print " Could not use caspy trying psspy"
            return False
    except Exception in e:
        raise

def try_import_caspy(filename):
    from caspy import Savecase
    file = os.path.join(app_settings.APP_DIR, filename)
    try:
        case=Savecase(file)
        return case
    except:
        return False

#This is the assumed pathway when the subprocess is called for CASPY usage
if __name__ == "__main__":
    filename =sys.argv[1]
    try_import_caspy(filename)
