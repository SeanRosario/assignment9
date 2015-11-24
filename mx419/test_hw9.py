"""this module contains unittest for the functions in the program"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from unittest import TestCase
import unittest
import data_process_functions

#author: Muhe Xie
#netID: mx419
#date: 11/16/2015

class Test_HW9(TestCase):
    '''this class will test the function merge_by_year in module data_process_functions'''
    def setUp(self):
        pass

    def test_merge_by_year_case1(self):
        #load the data
        countries = pd.read_csv('countries.csv',sep=',')
        income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',sheetname='Data',index_col=0)
        income_new = income.transpose()
        #merge function
        merged_result = data_process_functions.merge_by_year(2003,countries,income_new)
        self.assertEqual(merged_result['Country'][27],'Mauritius')
        self.assertEqual(merged_result['Region'][27],'AFRICA')
        self.assertEqual(int(merged_result['Income'][27]),9564)

    def test_merge_by_year_case2(self):
        #load the data
        countries = pd.read_csv('countries.csv',sep=',')
        income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',sheetname='Data',index_col=0)
        income_new = income.transpose()
         #merge function
        merged_result = data_process_functions.merge_by_year(1800,countries,income_new)
        self.assertEqual(merged_result['Country'][27],'Mauritius')
        self.assertEqual(merged_result['Region'][27],'AFRICA')
        self.assertEqual(int(merged_result['Income'][27]),799)


    def test_merge_by_year_case3(self):
        #load the data
        countries = pd.read_csv('countries.csv',sep=',')
        income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',sheetname='Data',index_col=0)
        income_new = income.transpose()
         #merge function
        merged_result = data_process_functions.merge_by_year(1800,countries,income_new)
        self.assertEqual(merged_result['Country'][176],'Venezuela')
        self.assertEqual(merged_result['Region'][176],'SOUTH AMERICA')
        self.assertEqual(int(merged_result['Income'][176]),442)


    def test_merge_by_year_case4(self):
        #load the data
        countries = pd.read_csv('countries.csv',sep=',')
        income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',sheetname='Data',index_col=0)
        income_new = income.transpose()
         #merge function
        merged_result = data_process_functions.merge_by_year(2012,countries,income_new)
        self.assertEqual(merged_result['Country'][147],'Saint Kitts and Nevis')
        self.assertEqual(merged_result['Region'][147],'NORTH AMERICA')
        self.assertEqual(int(merged_result['Income'][147]),12659)


if __name__ == '__main__':
    unittest.main()