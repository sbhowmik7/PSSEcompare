"""createdb: Create the database for the PSSE comparison tool.
        Create the tables appropriate for the data collected about the psse
          api (element tables and plant/settings table).
"""
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"


import os
import sys
import sqlite3

# import app_settings (which sets up the rest of the paths).
try:
    import app_settings
except ImportError:
    this_dir = os.path.dirname(__file__)
    sys.path.append(os.path.join(this_dir,'..'))
    import app_settings


slurp_db_string_a = ("""CREATE TABLE slurpA (
        node TEXT NOT NULL,
        type TEXT NOT NULL,
        option TEXT NOT NULL,
        value TEXT)""")

slurp_db_string_b = ("""CREATE TABLE slurpB (
        node TEXT NOT NULL,
        type TEXT NOT NULL,
        option TEXT NOT NULL,
        value TEXT)""")

slurp_ind_stringa = """
        CREATE INDEX job_case_nodea on slurpA (node, type, option);
        """
slurp_ind_stringb = """
        CREATE INDEX job_case_nodeb on slurpB (node, type, option);
        """
slurp_new_ind_string = """
        CREATE INDEX new_ind on slurp (case_id, node)"""

compare_db_string = ("""CREATE TABLE compare (
        node TEXT NOT NULL,
        type TEXT NOT NULL,
        option TEXT NOT NULL,
        before TEXT,
        after TEXT)""")

new_db_string = ("""CREATE TABLE new (
        node TEXT NOT NULL,
        type TEXT NOT NULL,
        option TEXT NOT NULL,
        value TEXT)""")

removed_db_string = ("""CREATE TABLE removed (
        node TEXT NOT NULL,
        type TEXT NOT NULL,
        option TEXT NOT NULL,
        value TEXT)""")

# Most of these data types refer to lists and thus will be stored as JSON
# values.
subsys_opt_string = ("""CREATE TABLE subsys_opt (
        range_kv JSON,
        areas JSON,
        owners JSON,
        zones JSON,
        buses JSON)""")

def create_independent_slurp_db():
    con = sqlite3.connect(app_settings.SLURP_DB)
    con.execute(slurp_db_string_a)
    con.execute(slurp_db_string_b)
    con.execute(slurp_ind_stringa)
    con.execute(slurp_ind_stringb)
    #con.execute(slurp_new_ind_string)
    con.commit()
    return con

def createdb():

    if app_settings.SLURP_DB != ':memory:':
        # not the main db, but still a file.
        slurp_con = create_independent_slurp_db()


    # This will connect to an existing db, then create the table
    comp_con = sqlite3.connect(app_settings.COMPARE_DB)
    comp_con.execute(compare_db_string)
    comp_con.execute(new_db_string)
    comp_con.execute(removed_db_string)
    comp_con.commit()
    comp_con.close()


if __name__ == "__main__":
    createdb()

