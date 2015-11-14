import pandas as pd
import matplotlib as plt 

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
print income.head()


def inc_by_year(year, df):
	'''Graphically display the distribution of income per person across all countries in the world for a the given year using a bar graph.'''
	
	#Get the GDP values for year. Throw out NaN values and sort by value. 
	gdp_dist = df.ix[year].dropna().order()
	
	plt.plot(kind='barh')

	plt.show()
	#Clear the plots for future use
	plf.clf()

	#need to transpose?
	#s.plt.plot(kind='barh')
	#consider clearing the plotting functionality
	
	
#def merge_by_year(year):
#	'''Merge the countries and income datasets for any given year. Result is a dataframe with three columns: country, region, income.'''
	
#class incomeByRegion(pass):
#	'''Graphically explore the distribution of the income per person by region for a given year. Uses histograms and boxplots.'''
#	pass
	
	
#Generate graphs for the years 2007-2012

#Write a description of the changes observed over the period into a file called results.txt

#Write unittests

#Write a README.txt'''