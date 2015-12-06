import pandas as pd
from functions import *
from tools import *
import unittest
import numpy as np

class hw9_test(unittest.TestCase):

    def setUp(self):
         pass

    def test_year_throw_exception(self):
        '''
        see if the program would throw the exception
        '''
        with self.assertRaises(ValueError) as words:
            year = np.random.randint(0,1000)
            tools(year)
        self.assertTrue('year out of range' in words.exception)

    def test_number_of_col_in_data_frame_in_merge_function(self):
        '''
        see if the output of the function has 3 columns
        '''
        year = np.random.randint(1800,2013)
        self.assertTrue(len(merge_by_year(year).columns) == 3)

    def test_data_frame_in_merge_function(self):
        '''
        see if the output of the merge function is a data frame
        '''
        year = np.random.randint(1800,2013)
        self.assertIsInstance(merge_by_year(year),pd.DataFrame)

if __name__ == '__main__':
    unittest.main()