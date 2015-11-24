"""Author: Akash Shah (ass502)

unittest for functions in the helper module"""

from helper import *
from unittest import TestCase

income, countries = load_data()

class HelperTest(TestCase):

	def test_invalid_year_plot_income(self):
		year1=1700
		year2=2200
		self.assertRaises(KeyError,plot_income_by_year,income,year1)
		self.assertRaises(KeyError,plot_income_by_year,income,year2)

	def test_invalid_merge_by_year(self):
		year1=1700
		year2=2200
		self.assertRaises(KeyError,merge_by_year,income,countries,year1)
		self.assertRaises(KeyError,merge_by_year,income,countries,year2)


