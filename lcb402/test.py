### Laura Buchanan
### lcb402

import unittest
from country_gdp import *
import os.path

class test_country_gdp(unittest.Testcase):
	
	def test_load_countries(self):
		self.assertTrue(os.path.isfile('../countries.csv')) 
		self.assertFalse(os.path.isfile('./countries.csv'))

	def test_load_income(self):
		self.assertTrue(os.path.isfile('../indicator gapminder gdp_per_capita_ppp.csv'))
                self.assertFalse(os.path.isfile('./indicator gapminder gdp_per_capita_ppp.csv'))

if __name__ == '__main__':
	unittest.main()
