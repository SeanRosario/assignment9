#Author: Xing Cui
#NetID: xc918
#Data: 11/16


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""getting the data from dataframe for given year."""

class data_in_given_year():

	def __init__(self, year):
		if year > 1799 and year < 2013:
			self.year = year
		else:
			print year
			raise KeyError

	#Question4
	def annual_income(self):
		"""Plot histgram for the given year of distribution of income per person across all countries."""
		data = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx')
		income = data[self.year]
		plt.figure()
		plt.hist(list(income.dropna()), bins=15)
		plt.title('Distribution of income per person across all countries in {}'.format(self.year))
		plt.show()
	    
	#Question5
	def merge_by_year(self):
		""" This function is going to merge the countries and income for any given year.
			It will return a dataframe with three columns titled Country, Region and Income."""

		countries = pd.read_csv('countries.csv')
		income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx', index_col = 0)
		target_year = income[self.year].to_frame()
		target_year.reset_index(level = 0, inplace = True)
		target_year.columns = ['Country', 'Income']
		target_year = target_year.dropna()
		result = pd.merge(countries, target_year)
		return result

