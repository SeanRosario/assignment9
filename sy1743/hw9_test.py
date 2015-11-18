import unittest
from unittest import TestCase
import hw9_functions
from hw9_functions import plot_income_by_yr, merge_by_year
import visualize_tool as vs

# DS-GA 1007
# HW9
# Author: Sida Ye
# test file

"""tests for hw9"""

class hw9_unittest(unittest.TestCase):

    def setUp(self):
        pass


    def test_plot_income_by_yr_1(self):
        with self.assertRaises(KeyError) as cm:
            hw9_functions.plot_income_by_yr(2015)
        the_exception = cm.exception
        self.assertEquals(str(the_exception), "'Invalid Year!'")

    def test_plot_income_by_yr_2(self):
        with self.assertRaises(KeyError) as cm:
            hw9_functions.plot_income_by_yr(1000)
        the_exception = cm.exception
        self.assertEquals(str(the_exception), "'Invalid Year!'")

    def test_vs_1(self):
        with self.assertRaises(KeyError) as cm:
            vs.visualize_tool(1000)
        the_exception = cm.exception
        self.assertEquals(str(the_exception), "'Invalid Year!'")

    def test_vs_2(self):
        with self.assertRaises(KeyError) as cm:
            vs.visualize_tool(9000)
        the_exception = cm.exception
        self.assertEquals(str(the_exception), "'Invalid Year!'")



if __name__ == '__main__':
    unittest.main()
