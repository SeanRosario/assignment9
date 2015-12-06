import unittest
from unittest import TestCase
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import datafunc
from datafunc import *
# from assignment9 import main

class Input_Test(unittest.TestCase):
	'''test made for assignment 9'''
	def setUp(self):
		pass

	def test_user_input(self):
		# test wherether input year is in the valid range
		year_input = range(1800, 2013, 1)
		self.assertTrue(1998 in year_input)
		self.assertFalse(2990 in year_input)

	def test_merge_by_year(self):
		# test if invalid input raises error
		countries = pd.read_csv('countries.csv')
		income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx').T
		self.assertRaises(ValueError, lambda: merge_by_year(int('dowidofijsn')))

	def test_AnalysisTools(self):
		# test if invalid input raises error
		countries = pd.read_csv('countries.csv')
		income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx').T
		self.assertRaises(ValueError, lambda: AnalysisTools(int('ldkf')))


if __name__ == "__main__":
	unittest.main()