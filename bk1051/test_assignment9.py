import unittest
# Don't show figures for testing
# From: http://stackoverflow.com/questions/19812818/how-to-test-that-matplotlibs-show-shows-a-figure-without-actually-showing-it
from assignment9 import *

class a9_test_case(unittest.TestCase):
    def test_validate_year(self):
        self.assertEqual(validate_year("2009"), 2009)
        with self.assertRaises(UserTerminationException):
            validate_year("finish")

        with self.assertRaises(UserTerminationException):
            validate_year("Finish")

        with self.assertRaises(ValueError):
            validate_year("^A")
