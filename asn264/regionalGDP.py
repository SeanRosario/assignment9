'''
Author: Aditi Nair (asn264)
Date: November 15 2015

Description: This file contains the class required in Problem 6. 
It provides histograms and boxplots to graphically explore the distribution of
income per person by region for a given year, and saves these graphs to individual files.
It also contains a custom exception pertaining to the class. 
'''

from utilities import *

class InvalidDistributionRequestion(Exception):
	def __str__(self):
		return "Invalid Distribution Request."

class RegionalGDP(object):
	'''Each instance of this class is associated with a merged dataframe for the given year, controlling for the given region.'''
	def __init__(self, reg, year):

		tempdf = merge_by_year(year)

		#tempdf will be None if 'year' is not a row in income df
		if tempdf is not None:

			tempdf = tempdf.loc[tempdf['Region']==reg.upper()]

			#tempdf will be empty if 'reg' is not in the 'Region' column of countries
			if tempdf.empty:
				raise InvalidDistributionRequest
			else:
				self.df = tempdf

		else:
			raise InvalidDistributionRequest
	
	def plot_hist(self):
		#Copy this over when you have the other histogram figured out
		#Save the graph to individual files
		pass

	def plot_boxplot(self):
		#Save the graph to individual files
		pass
