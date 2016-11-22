"""compare: """
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"

from collections import defaultdict
import sqlite3
from math import fabs
import sys

import app_settings
sys.path.append(app_settings.UTILS_DIR)
sys.path.append(app_settings.META_DIR)
from elements import elements

def get_bus_from_node(nodeid):
    # For all elements that don't use a name as their nodeid, this is easy as
    # pie. (I think only FACTS devices use names as their primary key)
    return int(nodeid.split('|')[0])

def changes_by_bus():
    changes = defaultdict(list)

    conn = sqlite3.connect(app_settings.COMPARE_DB)
    curs = conn.cursor()

    curs.execute("""SELECT * FROM compare""")

    results = curs.fetchmany()
    while results:
        for row in results:
            #MAGIC
            changes[get_bus_from_node(row[0])].append(row)
        results = curs.fetchmany()

    return changes

def unique_elems_by_type(table):
    """Return a dictionary structure of the requested unique elems by type"""

    comp_db = sqlite3.connect(app_settings.COMPARE_DB)
    comp_db.text_factory = str

    params = {'table':table}

    changes = defaultdict(list)
    for e in elements.values():
        params['unique_opt'] = e.writables.keys()[0]
        request = comp_db.execute("""SELECT node, type from %(table)s
                                    where 
                                    option='%(unique_opt)s'""" % params)
        results = request.fetchmany()
        while results:
            for node, elem_type in results:
                changes[elem_type].append(node)
            results = request.fetchmany()
    request.close()
    comp_db.close()
    return changes


def changes_by_type(table):
    """Return a dictionary structure of the requested changes"""

    comp_db = sqlite3.connect(app_settings.COMPARE_DB)
    comp_db.text_factory = str

    params = {'table':table}

    request = comp_db.execute("SELECT * from %(table)s" % params)

    changes = defaultdict(list)
    results = request.fetchmany()
    while results:
        for row in results:
            # MAGIC
            changes[row[1]].append(row)
        results = request.fetchmany()
    request.close()
    comp_db.close()
    return changes


def similar(a,b):
    '''
    Returns True if a approximately equals b.
    '''
    tol = 1e-5
    if fabs(a-b) < tol:
        return True

    if fabs(a) > fabs(b):
        try:
            relative_error = fabs((a-b) / b)
        except ZeroDivisionError:
            return fabs(a-b) < tol
    else:
        try:
            relative_error = fabs((a-b) / a)
        except ZeroDivisionError:
            return fabs(a-b) < tol

    if relative_error <= tol:
        return True
    return False

def drop_similar_floats(rows):
    """
    Drop floats whose value is similar before and after.
    """
    tol = 1e-5
    for node, elemtype, option, before, after in rows:
        try:
            if similar(float(before), float(after)):
                continue
        except ValueError:
            # its a string!
            pass

        yield (node, elemtype, option, before, after)


def compare(comp_con, slurp_con):
    sql_vals = {'caseA':'A','caseB':'B'}
    base_query = """SELECT A.node,A.type,A.option,A.value,B.value
            FROM slurpA as A
            INNER JOIN slurpB as B
            ON  A.node=B.node and
                A.type=B.type and A.option=B.option
            where A.value!=B.value""" % sql_vals

    compared_curs = list(slurp_con.execute(base_query))
    comp_con.executemany("INSERT INTO compare VALUES (?, ?, ?, ?, ?)",
                         drop_similar_floats(compared_curs))
    comp_con.commit()

    add_added_elems_to_db(slurp_con, comp_con)
    add_removed_elems_to_db(slurp_con, comp_con)

def get_except_nodes(slurp_con, params, unique_opt):
    # Get except nodes
    sql_exec = """SELECT s.node, s.type, s.option, s.value
                  FROM slurp%(keep_elems_case)s s
                  WHERE s.node NOT IN (
                    SELECT node FROM slurp%(except_case)s)
        """ % params

    return slurp_con.execute(sql_exec)

def add_added_elems_to_db(slurp_con, comp_con):
    """Write to a db of all the new elements being added to this case.
    TODO: Will need to add special code for subsystem peculiarities to be handled
    here.
    """
    params = {'keep_elems_case':'B', 'except_case':'A'}

    for e in elements.values():
        # get the first writable variable name (as this is a primary param, it
        # will always be the same and present.)
        params['elem_name'] = e.elem_name
        nodes = get_except_nodes(slurp_con, params, e.writables.keys()[0])
        insert_new = "INSERT INTO new values (?, ?, ?, ?)"
        comp_con.executemany(insert_new, nodes)

    comp_con.commit()

def add_removed_elems_to_db(slurp_con, comp_con):
    """Write to a db of all the elements being removed from case A.
    TODO: Will need to add special code for subsystem peculiarities to be handled
    here.
    """
    params = {'keep_elems_case':'A', 'except_case':'B'}

    for e in elements.values():
        # get the first writable variable name (as this is a primary param, it
        # will always be the same and present.)
        nodes = get_except_nodes(slurp_con, params, e.writables.keys()[0])
        params['elem_name'] = e.elem_name
        sql_insert = "INSERT INTO removed values (?, ?, ?, ?)"
        comp_con.executemany(sql_insert, nodes)

    comp_con.commit()


def do_compare():
    """
    Compares the two files from the data in the SQLite database
    """
    slurp_con = sqlite3.connect(app_settings.SLURP_DB)
    slurp_con.text_factory = str
    comp_con = sqlite3.connect(app_settings.COMPARE_DB)
    comp_con.text_factory = str
    comp_con.execute("DELETE from compare")
    comp_con.execute("DELETE from new")
    comp_con.execute("DELETE from removed")
    comp_con.commit()

    print "Starting comparison between the 2 files"

    try:
        compare(comp_con, slurp_con)
    except:
        print('Fatal compare error.')
        raise
    print('Comparison Complete.')

if __name__ == "__main__":
    do_compare()