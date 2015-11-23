'''
Created on Nov 17, 2015

@author: Benjamin Jakubowski (buj201)
'''
import unittest
import os
import random
from exploratory_analysis_class import *

class Test(unittest.TestCase):

    def test_load_countries(self):
        if os.path.isfile('../countries.csv'):
            self.assertIsInstance(load_countries(),pd.DataFrame)
        else:
            self.assertIsNone(load_countries())
            
    def test_load_income(self):
        if os.path.isfile('../indicator gapminder gdp_per_capita_ppp.xlsx'):
            self.assertIsInstance(load_income(),pd.DataFrame)
        else:
            self.assertIsNone(load_income())
            
    def test_is_valid_year(self):
        bad_inputs = [1346, 2015, 103, 'ab', '   ']
        for input in bad_inputs:
            self.assertRaises(ValueError, is_valid_year, input)
            
    def test_merge_by_year(self):
        for iter in range(3):
            year = random.choice(range(1800,2012))
            self.assertIsInstance(merge_by_year(year),pd.DataFrame)
            
    def test_class(self):
        for iter in range(3):
            year = random.choice(range(1800,2012))
            self.assertIsInstance(Explore_year(year),Explore_year)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()