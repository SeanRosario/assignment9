'''
Varun D N, vdn207
DS-GA 1007 - Assignment 9
'''

'''Unit tests for functions working to respond to the user'''

from unittest import TestCase
import data_frame_class as df_class
import custom_exceptions as cexcep
import question_specific_module as qspec
import matplotlib.pyplot as plt
import exploratory_analysis as ea 
import pandas as pd 

class PositionTests(TestCase):
	'''Unit Tests for positions'''

	def setUp(self):
		'''Setting up the test environment'''

		self.input1 = [1, 10, 100, -1]
		income = pd.read_excel("data/indicator gapminder gdp_per_capita_ppp.xlsx")
		self.income_obj = df_class.Dataframe(income, True)
		self.test_year = 100

	def test_not_a_dataframe_exception_raised(self):
		'''Raises the NotADataFrameException'''

		self.assertRaises(cexcep.NotADataFrameException, df_class.Dataframe, self.input1)

	def test_year_not_available_exception(self):
		'''Raises the YearNotFoundException'''

		self.assertRaises(cexcep.YearNotFoundException, qspec.income_per_person_by_year, self.test_year, self.income_obj)



