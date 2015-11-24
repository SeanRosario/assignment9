import unittest
from unittest import TestCase
import random
from Input_merge import *
import pandas as pd
import numpy as np
# countries=pd.read_csv('/Users/Yichen/Downloads/assignment9/countries.csv',header=0)
# countries=pd.DataFrame(countries)
# income=pd.read_csv('/Users/Yichen/Downloads/assignment9/indicator gapminder gdp_per_capita_ppp.csv', index_col='gdp pc test')
class Test(unittest.TestCase):
	def test_merge(self):
		countries=pd.read_csv('/Users/Yichen/Downloads/assignment9/countries.csv',header=0)
		countries=pd.DataFrame(countries)
		income=pd.read_csv('/Users/Yichen/Downloads/assignment9/indicator gapminder gdp_per_capita_ppp.csv', index_col='gdp pc test')
		year = np.random.randint(1800,2013)
		self.assertIsInstance(merge_by_year(income,countries,year-1800),pd.DataFrame)
	#Test whether merge is valid

		
	def test_load_countires(self):
	#Test whether load correct data
		new_df = load_countries_csv()
		self.assertEquals(len(new_df.columns),2)

	
if __name__ == '__main__':
	unittest.main()
	


