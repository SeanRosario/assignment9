'''
Author: Aditi Nair (asn264)
Date: November 23 2015 

Description: this module contains unit-testing for the the merge_by_year and income_by_year functions.
'''

from unittest import TestCase
from utilities import *

countries, income = load_session()

class test_income_by_year(TestCase):

	#Make sure invalid years (years that are not in the income df) as handled correctly
	def test_invalid_year(self):
		self.assertEqual(income_by_year(income, 2016), False)

class test_merge_by_year(TestCase):

	#Make sure invalid years (years that are not in the income df) are handled correctly
	def test_invalid_year(self):
		self.assertEqual(merge_by_year(countries, income, 2016), None)

	#Make sure the output df has three columns
	def test_num_columns(self):
		self.assertEqual(len(merge_by_year(countries, income, 1801).columns), 3)
	


