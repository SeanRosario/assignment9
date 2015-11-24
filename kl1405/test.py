import unittest
from unittest import TestCase
from merge import *
from plot import *
import pandas as pd

# author: kaiwen Liu

""" this is a test for assignment9 """

income=pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx', index_col=0)
income=pd.DataFrame(income)
countries=pd.read_csv('countries.csv', index_col=0)
countries=pd.DataFrame(countries)

class test(unittest.TestCase):

    def setUp(self):
        pass

    # test two invalid inputs 1700 and 2015
    def test_input_1700(self): 
        self.assertRaises(KeyError, year = 1700)

    def test_input_2015(self):
        self.assertRaises(KeyError, year = 2015)

    def test_3_columns(self): # test if there are 3 columns in the merged 
        year = np.random.randint(1800,2013)
        self.assertTrue(len(merge_by_year(income, countries, year).columns) == 3)

    def test_data_frame_in_merge_function(self): # test if the merged is a data frame
        year = np.random.randint(1800,2013)
        self.assertIsInstance(merge_by_year(income, countries, year), pd.DataFrame)

if __name__ == '__main__':
    unittest.main()