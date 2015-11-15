'''
Author: Aditi Nair
Date: November 15 2015

Description: This file is responsible for setting up the countries and income dataframes as required in Problems 1-3.
It also contains the required functions inc_by_year and merge_by_year as required in Problems 4 and 5. 
'''


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 

countries = pd.read_csv('../countries.csv')

income = pd.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx')

#Years are column names. Transpose the dataset to have years as the rows
income = income.transpose()

#Make the countries the column names
income.columns = income.ix[0]

#Remove the row with the country names and reindex. This means income.ix[0] no longer exists. 
income = income.ix[1:]

#print "Income DataFrame looks like:/n", income.head()

#THIS LOOKS GOOD FOR YEAR = 1808, BUT BAD FOR YEAR = 1900
#Need to encapsulate this in a try/except
def inc_by_year(year):
	'''Graphically display the distribution of income per person across all countries in the world for a the given year using a bar graph.'''
	
	try:
		#Get the GDP values for year. Throw out NaN values and sort by value. 
		gdp_dist = income.ix[year].dropna().order()	

		#Plot a histogram of the series and format it nicely. 
		hist = gdp_dist.plot(kind = 'hist', bins=np.arange(min(gdp_dist), max(gdp_dist) + 100, 100), color='#483D8B', figsize = (18,6))
		plt.xticks(np.arange(min(gdp_dist), max(gdp_dist), 100))
		plt.axis('tight')
		plt.title('GDP Distribution in ' + str(year))
		plt.xlabel('GDP per Person')
		plt.ylabel('Number of Countries')
		plt.show()

	except KeyError:
		print "Invalid input."

	
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
