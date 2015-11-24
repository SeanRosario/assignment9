'''
This test module tests the exception-handlings in merg_by_year in data.py. 
'''

import unittest
from unittest import TestCase
from data import load_data, merge_by_year


countries, income = load_data()

class Assignment9_test(unittest.TestCase):
    def setUp(self):
        pass
 
    def test_merge_by_year_value(self):
        with self.assertRaises(KeyError) as mby:
            merge_by_year(countries, income, '1700')
            mby.exception
            self.assertEquals(str(mby.exception), 'Invalid year.')
       
    def test_merge_by_year_type(self):
        with self.assertRaises(KeyError) as mby:
            merge_by_year(countries, income, 'A')
            mby.exception
            self.assertEquals(str(mby.exception), 'Invalid input type.')


if __name__ == '__main__':
    unittest.main()


