import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt 
from user_exceptions import invalid_input, invalid_year

'''functions including display_distribution and merge_by_year for Question 4 and 5.''' 

def RepresentsInt(s):
	'''define a function to generate a boolean value of s: if s can be converted to an integer return True.'''

	try:
		int(s)
		return True
	except ValueError:
		return False

def display_distribution(year, dataframe):
	'''function to display the distribution of income per person across all countries in the world for the given year.'''
	
	if RepresentsInt(year) == True:   #check if input year can be converted to an integer
		if int(year) >2012 or int(year) < 1800:   #check if input year in the right range
			raise invalid_year()
		else:
			year_distribution = dataframe.ix[int(year),:]   #select the data in the given year
			plt.figure(figsize = (10, 10))
			year_distribution.dropna().order().plot(kind = 'barh')   #drop the nan value and sort by the value
			plt.xlabel('Income per person')
			plt.ylabel('Countries')
			plt.yticks(fontsize = 4)
			plt.title('Income distribution of per person over countries in ' + str(year))
			plt.show()
	else:
		raise invalid_input()

def merge_by_year(dataframe1, dataframe2, year):
	'''function to merge the countries and income data sets for any given year.'''

	if RepresentsInt(year) == True:   #this part same as one in display_distribution
		if int(year) > 2012 or int(year) < 1800:
			raise invalid_year()
		else:
			year_distribution = dataframe1.ix[year,:]
			year_distribution.name = 'Income'   
			year_distribution.index.name = 'Country'
			region_distribution = pd.merge(pd.DataFrame(year_distribution), dataframe2, left_index = True, right_on = 'Country', how = 'inner')
			region_distribution_dropna = region_distribution.dropna()   #drop the nan value
			return region_distribution_dropna
	else:
		raise invalid_input()


