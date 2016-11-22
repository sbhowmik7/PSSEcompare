"""TODO
"""
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"

import sqlite3
import sys
import os.path
import platform

# ====   directories
APP_DIR = os.path.abspath(os.path.dirname(__file__))
ADMIN_DIR = os.path.join(APP_DIR, 'admin')
UTILS_DIR = os.path.join(APP_DIR, 'utils')
META_DIR = os.path.join(APP_DIR, 'meta')
LIB_DIR = os.path.join(APP_DIR, 'ext_libs')

def add_to_syspath(new_dir):
    if new_dir not in sys.path:
        sys.path.insert(0, new_dir)

for app_dir in reversed([APP_DIR, ADMIN_DIR, UTILS_DIR, META_DIR,LIB_DIR]):#BOTTLE_TEMPLATE_DIR, STATIC_DIR,
    add_to_syspath(app_dir)

if 'Windows' in platform.platform():
    import pssepath
    pssepath.ignore_python_mismatch = True


# ====   sqlite3 options
detect_types_arg = sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES

# ====   db options
SLURP_DB = os.path.join(APP_DIR,'admin','slurp.db')
COMPARE_DB = os.path.join(APP_DIR,'admin','compare.db')
JOB_TABLE = 'jobs'
MSG_TABLE = 'msg'

# ====   Psse options:
PREF_PSSE_VER = None
# this adds pssbin to system path. System path is global for all modules so
# there is no need to run this in any files that import app_settings, just run
# import psspy
USE_CASPY =True
if 'Windows' in platform.platform():
    pssepath.add_pssepath(PREF_PSSE_VER)
    # python exec required for the selected psse.
    PYTHON_EXEC = pssepath.req_python_exec
else:
    # If not windows, define this as just the currently running python.
    PYTHON_EXEC = sys.executable
