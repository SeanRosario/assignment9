'''
Author: Aditi Nair (asn264)
Date: November 15 2015

Description: This file contains the class required in Problem 6. 
It provides histograms and boxplots to graphically explore the distribution of
income per person by region for a given year, and saves these graphs to individual files.
It also contains a custom exception pertaining to the class. 
'''

from utilities import *

class InvalidDistributionRequest(Exception):
	def __str__(self):
		return "Invalid Distribution Request."

class regionalGDP(object):
	'''Each instance of this class is associated with a merged dataframe for the given year, grouped by region.'''

	def __init__(self, countries, income, year):

		tempdf = merge_by_year(countries, income, year)

		#tempdf will be None if 'year' is not a row in income df
		if tempdf is not None:

			#Drop the Country column and all rows without a Region value
			self.df = tempdf.drop('Country', axis=1)
			self.df = self.df[self.df['Region'].notnull()]

			#Pandas loads column as type 'Object', want type float
			self.df['Income']=self.df['Income'].astype(float)

			self.year = year

		else:
			raise InvalidDistributionRequest
	
	def plot_hist(self):

		'''Plot histograms of the series and format nicely.'''
		self.df['Income'].hist(by=self.df['Region'], xlabelsize=6, xrot = True, ylabelsize=8, bins=20)
		plt.suptitle('GDP Distribution in ' + str(self.year), fontsize=16)
		plt.savefig("Income_by_Region_" + str(self.year) + "_Histogram.pdf")
		


	def plot_boxplot(self):
			
		'''Create boxplots of the series and format nicely.'''

		plt.figure()
		self.df.boxplot(column='Income', by='Region', figsize=(10,5))
		plt.title("Income per Person by Region " + str(self.year))
		plt.ylabel("Income")
		plt.savefig("Income_by_Region_" + str(self.year) + "_Boxplot.pdf")

