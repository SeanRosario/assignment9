import unittest
from unittest import TestCase
import pandas as pd
from pandas.util.testing import assert_frame_equal
from user_exceptions import invalid_input, invalid_year
import load_csv

class assignment9_test(TestCase):
	'''test the functions: display_distribution and merge_by_year.'''

	def test_display_distribution_invalid_input(self):
		'''test display_distribution function raise error when input year can not be converted to an integer.'''
		
		Countries = pd.read_csv('countries.csv')
		self.assertRaises(invalid_input, lambda: load_csv.display_distribution('tt', Countries))

	def test_display_distribution_invalid_year(self):
		'''test display_distribution function raise error when input year out of range[2007-2012].'''

		Countries = pd.read_csv('countries.csv')
		self.assertRaises(invalid_year, lambda: load_csv.display_distribution(2013, Countries))

	def test_merge_by_year_invalid_input(self):
		'''test merge_by_year function raise error when input year can not be converted to an integer.'''

		Countries = pd.read_csv('countries.csv')
		income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx', index_col='gdp pc test').T
		self.assertRaises(invalid_input, lambda: load_csv.merge_by_year(income, Countries, 'tt'))

	def test_merge_by_year_invalid_year(self):
		'''test merge_by_year function raise error when input year out of range[2007-2012].'''

		Countries = pd.read_csv('countries.csv')
		income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx', index_col='gdp pc test').T
		self.assertRaises(invalid_year, lambda: load_csv.merge_by_year(income, Countries, 1799))

if __name__ == '__main__':
	unittest.main()