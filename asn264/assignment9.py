'''
Author: Aditi Nair
Date: November 12 2015
Resources: http://stackoverflow.com/questions/6986986/bin-size-in-matplotlib-histogram

TO DO:
- Organize
- Write Test Cases
'''

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 

#Load countries.csv into the dataframe called countries
countries = pd.read_csv('../countries.csv')

#Load the indicator gapminder gdp_per_capita_ppp.xlsx data set into the dataframe called income
income = pd.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx')

#Years are column names. Transpose the dataset to have years as the rows
income = income.transpose()

#Make the countries the column names
income.columns = income.ix[0]

#Remove the row with the country names and reindex. This means income.ix[0] no longer exists. 
income = income.ix[1:]

#Show the head of this data
#print "Income DataFrame looks like:/n", income.head()

#THIS LOOKS GOOD FOR YEAR = 1808, BUT BAD FOR YEAR = 1900
def inc_by_year(year, df):
	'''Graphically display the distribution of income per person across all countries in the world for a the given year using a bar graph.'''
	
	#Get the GDP values for year. Throw out NaN values and sort by value. 
	gdp_dist = df.ix[year].dropna().order()	

	#Plot a histogram of the series and format it nicely. 
	hist = gdp_dist.plot(kind = 'hist', bins=np.arange(min(gdp_dist), max(gdp_dist) + 100, 100), color='#483D8B', figsize = (18,6))
	plt.xticks(np.arange(min(gdp_dist), max(gdp_dist), 100))
	plt.axis('tight')
	plt.title('GDP Distribution in ' + str(year))
	plt.xlabel('GDP per Person')
	plt.ylabel('Number of Countries')
	plt.show()

	
def merge_by_year(year):
	'''Merge the countries and income datasets for any given year. Result is a dataframe with three columns: country, region, income.'''
	
	try:

		#Controlling for year, left outer join on income.index (country names) being equal to entries in Country column in the countries df.
		merged = pd.merge(income.ix[year].to_frame(), countries, how = 'left', left_index=True, right_on='Country')
	
		#Renaming the column with year name
		merged = merged.rename(columns = {year:'Income'})

		#Reseting indices to 0,1,2,...
		return merged.reset_index(drop=True)

	#Occurs if 'year' is not a row in income df. 
	except KeyError:
		return None

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


