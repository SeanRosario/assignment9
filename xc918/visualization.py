#Author: Xing Cui
#NetID: xc918
#Data: 11/16

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from assignment9_function import *


"""This class generates boxplots and histograms for income based on regions."""
#Question6
class visualization():

	def __init__(self, year):
		if year > 1799 and year < 2013:
			self.year = year
		else:
			raise KeyError


	def histogram_plotting(self):
		data = data_in_given_year(self.year).merge_by_year()
		region_uniqueness = data['Region'].unique()#get unique region list.
		regional_income = []#initialize income by region

		for i in region_uniqueness:
			regional_income.append(data[data['Region'] == i].Income)

		map_color = plt.get_cmap('cool')#choose map color
		# color = []
		# for j in [.15, .3, .45, .6, .75, .9, 1.0]:#separate colors for different level.
		# 	color.append = map_color(j)

		fig = plt.figure()
		plt.hist(regional_income, bins = 20, stacked = True, label = list(region_uniqueness))
		plt.title('Distribution of Income by Region in {}'.format(self.year))
		plt.legend()
		plt.savefig('Histogram_Distribution_by_Region_in_{}'.format(self.year))


	def boxplot_plotting(self):
		data = data_in_given_year(self.year).merge_by_year()
		plt.figure()
		data.boxplot('Income', by = 'Region')
		plt.title('Distribution of Income by Region in {}'.format(self.year))
		plt.ylabel('Income')
		plt.legend()
		plt.savefig('Boxplot_Distribution_by_Region_in_{}'.format(self.year))



