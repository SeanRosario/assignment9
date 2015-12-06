"""Author: Akash Shah (ass502)

This module contains code that loads and preprocesses the relevant data,
along with functions for plotting and merging data for an input year"""

import pandas as pd
import matplotlib.pyplot as plt

def load_data():
	"""function that loads and processes the data into dataframes"""

	#load data
	countries = pd.read_csv("../countries.csv")
	income = pd.read_excel("../indicator gapminder gdp_per_capita_ppp.xlsx")

	#change index to country name
	income.set_index('gdp pc test',inplace=True)
	income.index.names=[None]

	#transpose so that years are rows and countries are columns
	income=income.transpose()

	print income.head()

	return [income, countries]

def plot_income_by_year(income,year):
	"""plot income distribution across all countries for the input year"""

	#get income information for the year we want
	curr_year = income.ix[year,:]

	#plot data
	plt.hist(curr_year.dropna(),bins=50)

	#set axis labels and titles
	plt.xlabel('Mean Income (per person)')
	plt.ylabel('Number of Countries')
	plt.title('Mean Income Per Capita in '+str(year))

	plt.show()

def merge_by_year(income,countries,year):
	"""merges income and countries dataframes"""

	#get income information for the year we want, convert to dataframe
	curr_year=income.ix[year,:].to_frame()
	
	#merge dataframes on the Country column
	merged_frame = pd.merge(countries,curr_year,left_on='Country',right_index=True)
	
	#change column name from the year to Income and return the dataframe
	return merged_frame.rename(columns = {year:'Income'},inplace=False)