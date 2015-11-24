import pandas as pd
import matplotlib.pyplot as plt 
from functions import merge_by_year

''' class used to generate and save boxplots and histograms'''

class dataAnalysis():

	def __init__(self, year):

		if year >= 1800 and year <= 2012:

			self.year = year

		else:
			raise ValueError('Sorry! You should input a year between 1800 and 2012')

	# function used to generate and save boxplots
	def plot_boxplots(self):

		dataframe = merge_by_year(self.year)

		dataframe = dataframe.dropna()

		plt.figure()
		dataframe.boxplot('Income', by = 'Region')
		plt.xlabel('Region')
		plt.ylabel('Income per Person')
		plt.title('Income per Person by Region in year {}'.format(self.year))
		plt.savefig('boxplot_by_region_in_{}.png'.format(self.year))
		plt.close()

	# function used to generate and save histograms 
	def plot_histograms(self):

		dataframe = merge_by_year(self.year)

		dataframe = dataframe.dropna()

		plt.figure()
		dataframe.hist('Income', by = 'Region', xlabelsize = 7, ylabelsize = 10, bins = 30)
		plt.xlabel('Income per Person')
		plt.ylabel('Number of Countries')
		plt.savefig('histograms_by_region_in_{}.png'.format(self.year))
		plt.close()


