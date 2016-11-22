"""TODO
"""
__author__ = "Sudipto Bhowmik, whit.com.au"
__license__ = "GPL"
__version__ = "1.0.0"

import unittest
import textwrap

import elem_obj

class TestParams(unittest.TestCase):

    def test_derive_read_fn(self):
        param = elem_obj.parameter(read_name='AREA',read_fn='abusint')
        read_fn = param.derive_read_fn('bus', 'int')
        self.assertEqual('abusint', read_fn)

    def test_no_fn_read_fails(self):
        """Check that it correctly detects an inability to derive read_fn."""
        # No actual read_fn nor read_fn_key
        input_dict = dict(read_name='AREA',
            data_type='int',
            )
        self.assertRaises(Exception, elem_obj.parameter, input_dict)
        # No actual read_fn nor data_type
        input_dict = dict(read_name='AREA',
            read_fn_key='bus',
            )
        self.assertRaises(Exception, elem_obj.parameter, input_dict)
        # No data read_fn data of any type
        input_dict = dict(read_name='AREA')
        self.assertRaises(Exception, elem_obj.parameter, input_dict)

    def test_initial_get_read_fn(self):
        """Check initial_get_read_fn returns the correct fn name"""
        param = elem_obj.parameter(read_name='AREA',read_fn='abusint')
        # All parameters, matching.
        read_fn = param.initial_get_read_fn('bus', 'int', 'abusint')
        self.assertEqual('abusint', read_fn)
        # Only read_fn
        read_fn = param.initial_get_read_fn(None, None, 'abusint')
        self.assertEqual('abusint', read_fn)
        # Derived type.
        read_fn = param.initial_get_read_fn('bus', 'int', None)
        self.assertEqual('abusint', read_fn)

    def test_mismatch_fn_read_names(self):
        """Check supplying incorrect read_fn, read_fn_key and data_type
        fails"""

        input_dict = dict(read_name='AREA',
            data_type='int',
            read_fn_key='car',
            read_fn='abusint',
            )
        self.assertRaises(Exception, elem_obj.parameter, input_dict)


if __name__ == "__main__":
    unittest.main()
