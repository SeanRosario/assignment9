
import unittest
from LoadData import income_by_year, merge_by_year
from Explore import *
from assignment9 import *


class tests(unittest.TestCase):
    
    def test_load_functions(self):
        self.assertRaises(ValueError, income_by_year(1))
        self.assertRaises(ValueError, income_by_year(2013))
        self.assertRaises(ValueError, income_by_year('gsbou'))
        self.assertRaises(ValueError, merge_by_year(1))
        self.assertRaises(ValueError, merge_by_year(2013))
        self.assertRaises(ValueError, merge_by_year('gsbou'))
        