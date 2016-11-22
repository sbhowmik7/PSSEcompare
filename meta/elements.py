"""brn: element branch
"""
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"

from brn import brn_elem
from bus import bus_elem
from fxshunt import fxshunt_elem
from genbus import genbus_elem
from load import load_elem
from mach import mach_elem
from swsh import swsh_elem
from tr3 import tr3_elem
from trn import trn_elem
from wnd import wnd_elem

elements = {'brn':brn_elem, 'bus':bus_elem, 'fxshunt':fxshunt_elem,
        'genbus':genbus_elem, 'load':load_elem, 'mach':mach_elem,
        'swsh':swsh_elem, 'tr3':tr3_elem, 'trn':trn_elem, 'wnd':wnd_elem}
