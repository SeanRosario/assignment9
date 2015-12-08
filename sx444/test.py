"""this is the unit tests to test the program"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from unittest import TestCase
import unittest
import data_process_functions

class Test(TestCase):
      '''this is to test the function of merge_by_year in module data_process_functions'''
      def setUp(self):
	  pass

      def test_merge_by_year_1(self):
          '''this is to test for the first time'''
          countries = pd.read_csv('./countries.csv', sep=',')
	  income = pd.read_excel('./indicator gapminder gdp_per_capita_ppp.xlsx',sheetname='Data',index_col=0)
	  income2 = income.transpose()
	  result = data_process_functions.merge_by_year(1800,countries,income2)
 	  self.assertEqual(result['Country'][176],'Venezuela')
	  self.assertEqual(result['Region'][176],'SOUTH AMERICA')
	  self.assertEqual(int(result['Income'][176]),442)

      def test_merge_by_year_2(self):
	  '''this is to test for the second time'''
	  countries = pd.read_csv('countries.csv',sep=',')
	  income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',sheetname='Data',index_col=0)
	  income2 = income.transpose()
	  result = data_process_functions.merge_by_year(2003,countries,income2)
	  self.assertEqual(result['Country'][27],'Mauritius')
	  self.assertEqual(result['Region'][27],'AFRICA')
	  self.assertEqual(int(result['Income'][27]),9564)

      def test_merge_by_year_3(self):
	  '''this is to test for the third time'''
	  countries = pd.read_csv('countries.csv',sep=',')
	  income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',sheetname='Data',index_col=0)
	  income2 = income.transpose()
	  result = data_process_functions.merge_by_year(1800,countries,income2)
	  self.assertEqual(result['Country'][27],'Mauritius')
	  self.assertEqual(result['Region'][27],'AFRICA')
	  self.assertEqual(int(result['Income'][27]),799)

if __name__ == '__main__':
   unittest.main()
