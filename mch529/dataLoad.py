'''
class to import and manipulate the data
important data can be found in dataLoadClass.countries and dataLoadClass.income
'''
#author:Michael Higgins
#netid: mch529

import pandas as pd
from pandas import ExcelFile
from pandas import DataFrame
import numpy as np

class Data:
	

	def __init__(self):
		self.countries = pd.read_csv('countries.csv', index_col = 'Country')
		self.income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',
 sheetname = 'Data', index_col = 'gdp pc test')
		
	def switch_rows_columns(self,data):
		transpose = pd.DataFrame.transpose(data)
		return transpose


	def mergeByYear(self,year):
		df = pd.DataFrame.join(self.countries, self.income[year], how = 'left')
		df = df.rename(columns = {year : 'Income'})
		df = df.dropna(how = 'any')
		return df
	



if __name__=='__main__':
	d=Data()
