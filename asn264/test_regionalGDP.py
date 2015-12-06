'''
Author: Aditi Nair (asn264)
Date: November 23 2015 

Description: this module contains unit-testing for the the merge_by_year and income_by_year functions.
'''

from unittest import TestCase
from regionalGDP import *

countries, income = load_session()

class regionalGDPTest(TestCase):

	def test_invalid_init(self):
		self.assertRaises(InvalidDistributionRequest, regionalGDP, countries, income, '2016')


