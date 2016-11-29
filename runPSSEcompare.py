#!/usr/bin/env python
"""
runPSSEcompare: Main file that initiates the comparison of 2 PSSE case/raw files Can be used in command line mode
"""
from __future__ import with_statement
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"


import os.path
import os
import sqlite3
import sys
import time

# import app_settings (which sets up the rest of the paths).
try:
    import app_settings
except ImportError:
    sys.path.append(os.path.dirname(__file__))
    import app_settings


# import Grid Compare modules.
import createdb
from downloadwrite import make_python, make_csv, make_excel
from slurp import slurp
from compare import do_compare


def main(FileA, FileB):
    # Start everything! Called at the end of the file.
    #debug(True)
    createdb_if_absent()

    slurp(FileA,'A')
    slurp(FileB,'B')
    do_compare()
    pth,fa =os.path.split(FileA)
    fb =os.path.splitext(os.path.split(FileB)[1])[0]
    outfname =os.path.join(pth,os.path.splitext(fa)[0]+'-'+fb)
    if write_py:
        downloadpy(outfname+'.py',FileA)
    if write_excel:
        downloadxl(outfname+'.xlsx')


def createdb_if_absent():
    try:
        if os.path.isfile(app_settings.SLURP_DB):
            os.remove(app_settings.SLURP_DB)
        if os.path.isfile(app_settings.COMPARE_DB):
            os.remove(app_settings.COMPARE_DB)
    except OSError:
        _, err, _ = sys.exc_info()
        print("OS error: ", str(err))
        raise
    createdb.createdb()

def flush_tables(remove_slurp=True):
    if remove_slurp:
        con = sqlite3.connect(app_settings.SLURP_DB)
        for attempt in range(3):
            try:
                con.execute("DELETE FROM slurp")
                break
            except sqlite3.OperationalError:
                time.sleep(0.4)

        con.commit()
        con.close()


def downloadpy(fname,origfile):
    filename = fname
    with open(filename,'wb') as buff:
        make_python(buff,origfile)
    print("Done writing python file")

def downloadcsv(fname):
    filename = fname
    with open(filename, 'wb') as buff:
        make_csv(buff)
    print("Done writing csv file")

def downloadxl(fname):
    filename = fname
    make_excel(filename)
    print("Done writing excel file")

def usage():
    print 'python runPSSEcompare -o <Originalfile> -c <File2compare> -x[WriteoutExcelFile]'

# kick everything off!
import getopt

if __name__ == "__main__":
    ifileA = os.path.join(app_settings.APP_DIR, 'savnw.sav')
    ifileB = os.path.join(app_settings.APP_DIR, 'savcnv.sav')
    write_py = True
    write_excel = True
    try:
        opts, args = getopt.getopt(sys.argv[1:], "o:c:hxp",
                                   ["orgfile=", "cmpfile="])
    except getopt.GetoptError:
        _, err, _ = sys.exc_info()
        print str(err)
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit(2)
        elif opt in ('-o', '--origfil'):
            ifileA = os.path.join(app_settings.APP_DIR, arg)
        elif opt in ('-c', '--cmpfil'):
            ifileB =  os.path.join(app_settings.APP_DIR, arg)
        elif opt in ('-x', '--wrtxcl'):
            write_excel =True
        elif opt in ('-p', '--wrtpy'):
            pass
        else:
            usage()
            sys.exit(2)


    main(ifileA,ifileB)