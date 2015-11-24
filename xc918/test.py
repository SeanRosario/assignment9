#Author: Xing Cui
#NetID: xc918
#Data: 11/16

import unittest
from unittest import TestCase
from assignment9_function import *
import visualization as v


"""This is the test for assignment9."""

class test_assignment9(unittest.TestCase):

	def setUp(self):
		pass

	def test_year(self):
		self.assertRaises(KeyError, var1 = 1799)

	def test_func_merge_by_year(self):
		year = data_in_given_year(2000)
		result = year.merge_by_year()
		self.assertTrue(len(result.columns) == 3)

	def test_visualization(self):
		self.assertRaises(KeyError, year = 1111)

	



if __name__ == '__main__':
	unittest.main()