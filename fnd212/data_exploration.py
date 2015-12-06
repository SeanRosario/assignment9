#Author: fnd212
# DataExploration class definition

import numpy as np
import pandas as pd
import sys
from utils import merge_by_year, year_gdp_histogram,load_dataframes, year_gdp_boxplot
import defined_exceptions


class DataExploration(object):
	
	#Set the class attributes countries and income.
	#It also prints income.head() when the module is imported.
	try:	
		countries, income = load_dataframes()
		print income.head()

	except defined_exceptions.FatalError, exception:
		print(exception.message)
		print('Program will exit now')
		sys.exit(1)

	REGIONS = countries.Region.unique()

	def __init__(self,year):
		'''Sets self.year as the year received and 
		self.data as the DataFrame for the corresponding year, with Country as index,
		and Income and Region as columns.'''
		
		try:
			self.data = merge_by_year(year, self.income.transpose(), self.countries)
		
		except KeyError:
			raise KeyError('{} is not a valid year'.format(year))

		self.year = year

	def save_boxplots(self):
		''' Saves a plot in ./figures containing a boxplot of 
		the distribution of GDP per region for the year corresponding
		to self.year '''
		save_to = './figures/gdp_boxplot_{}'.format(self.year)
		year_gdp_boxplot( self.data, self.year, save_path=save_to )
		print('Boxplot for year {} saved to {}'.format(self.year,save_to))


	def save_histogram(self):
		''' Saves a plot in ./figures containing a histogram of 
		the distribution of GDP per region for the year corresponding
		to self.year '''	
		for region in self.REGIONS:
			save_to = './figures/gdp_histogram_{}_{}'.format(self.year,region)
			year_gdp_histogram( self.data, self.year, region=region, save_path=save_to )
			print('Histogram for year {} and region {} saved to {}'.format(self.year,region,save_to))




