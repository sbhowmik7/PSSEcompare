from __future__ import with_statement
import datetime
import os,sys
import traceback
""" Not used in the commandline version due to this being jsut tools for json
"""

# import app_settings (which sets up the rest of the paths).
try:
    import app_settings
except ImportError:
    this_dir = os.path.dirname(__file__)
    sys.path.append(os.path.join(this_dir,'..'))
    import app_settings

# import 3rd party packages


def insert_msg(msg):
    vals = {'msg':msg, 'time':str(datetime.datetime.now())}
    print(msg)


def update_status(status, **kwargs):
    print status
    return


def make_error_file():
    """
    Store the current traceback into a txt file in the static folder.
    return the full text filename.
    """
    exception = traceback.format_exc()
    now = datetime.datetime.now()
    exception_filename = now.strftime('tb-%y%m%d-%H%M%S.txt')
    location = os.path.join(app_settings.STATIC_DIR, exception_filename)
    with open(location, 'wb') as exception_file:
        exception_file.write(exception.replace('\n', '\r\n'))
    return exception_filename
