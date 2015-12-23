''' check that code runs well '''
#author: Michael Higgins
#netid: mch529

#https://docs.python.org/2/library/unittest.html
# Please tell me what I did wrong here, I couldn't get this to run for the life of me!!!!!

from unittest import TestCase
from exploreData import *
from assignment9 import *
from dataLoad import *
import pandas as pd
import numpy as np

class test_Program(TestCase):
	
	def test_CountriesLoad(self):
		''' check that countries has correct dimensions '''
		d=Data()
		self.assertEquals(d.countries.shape, (194,1))   #check countries shape


	def test_IncomeLoad(self):
		''' check that Income has correct dimensions '''
		d=Data()
		self.assertEquals(d.income.shape, (260,213)) 	#check income shape

	def test_Merge(self):
		d=Data()
		year =1822
		mergedcolumns = list(d.mergeByYear(year).columns.values)
		#print mergedcolumns
        self.assertEquals(mergedcolumns,[ 'Region', 'Income']) #check column names 
		# kept row names as country


