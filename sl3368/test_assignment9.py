import unittest
from unittest import TestCase
from functions import *
import functions
from data_analysis import *
import data_analysis

''' test for assignment9'''

class AssignmentTest(TestCase):

	def setUp(self):
		pass

	# test the ValueError when the year is above 2012 
	def test_plotDistribution_1(self):

		with self.assertRaises(ValueError) as cm:

			functions.plotDistribution(2013)

		the_exception = cm.exception 
		self.assertEqual(str(the_exception), 'Sorry! You should input a year between 1800 and 2012')

	# test the ValueError when the year is below 1800 
	def test_plotDistribution_2(self):

		with self.assertRaises(ValueError) as cm:

			functions.plotDistribution(1799)

		the_exception = cm.exception 
		self.assertEqual(str(the_exception), 'Sorry! You should input a year between 1800 and 2012')

	# test the ValueError when the year is above 2012
	def test_dataAnalysis_1(self):

		with self.assertRaises(ValueError) as cm:

			data_analysis.dataAnalysis(3000)

		the_exception = cm.exception 
		self.assertEqual(str(the_exception), 'Sorry! You should input a year between 1800 and 2012')


	# test the ValueError when the year is below 1800 
	def test_dataAnalysis_2(self):

		with self.assertRaises(ValueError) as cm:

			data_analysis.dataAnalysis(1000)

		the_exception = cm.exception 
		self.assertEqual(str(the_exception), 'Sorry! You should input a year between 1800 and 2012')

	# test the ValueError when the input is not a 4-digital integer
	def test_dataAnalysis_3(self):

		with self.assertRaises(ValueError) as cm:

			data_analysis.dataAnalysis(100)

		the_exception = cm.exception 
		self.assertEqual(str(the_exception), 'Sorry! You should input a year between 1800 and 2012')

if __name__ == '__main__':

	unittest.main()



