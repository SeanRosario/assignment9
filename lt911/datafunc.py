import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import pylab as pl

'''This module contains fucntions and class for solving the homework problems'''

countries = pd.read_csv('countries.csv')
income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx').T

def distribution_of_income_per_capita(year, income_df):
	# using histogram to graphically show the distribution of income per person by taking the year and the income dataframe
	plt.hist(income_df.loc[year].dropna().values, 100)
	plt.xlabel('Income per person across all countries')
	plt.ylabel('Number of counts')
	plt.title('Distribtion of income per person across all countries in '+ str(year))
	plt.savefig('IncomeDistribution_'+str(year)+'.pdf')
	plt.close()

def merge_by_year(year):
	# merging two dataframes by the given year
	left = countries
	right = pd.DataFrame({'Country': income.T['gdp pc test'], 'Income': income.T[year]})
	country_income_df = pd.merge(left, right, on = 'Country', how = 'inner')
	return country_income_df

class AnalysisTools:
	''' A class to manipulate different data analysis tools (histograms and boxplots)'''
	def __init__(self, year):
		# taking inputs for the class: a given year and the needed income dataframe
		self.year = year
		self.income_df = merge_by_year(year)
		self.income_df = self.income_df.convert_objects(convert_numeric = True)

	def histogram(self):
		# a method of the class to draw the histogram for the given year
		plt.figure()
		self.income_df.hist(column = 'Income', by = 'Region', figsize = (11.5, 8.5), bins = 20, xrot = 25, sharex = True, sharey = True)				
		pl.suptitle('Distriution of income in ' + str(self.year))
		plt.savefig('Historgram in '+ str(self.year) +'.pdf')
		plt.clf()

	def box_plot(self):
		# a method of the class to draw the box plot for the given year
		plt.figure()
		self.income_df.boxplot(column = 'Income', by = 'Region', figsize = (11.5,10), rot = 25)
		plt.title(str(self.year), y = 1.00000)
		plt.savefig('Boxplot in ' + str(self.year) + '.pdf')
		plt.clf()