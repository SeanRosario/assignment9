'''this is for a class to make plots of boxplot and histogram'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class data_analysis(object):
      '''this class uses exploratory data analysis tools to graphically explore the distribution of the income per person by region dataset for a given year'''

      def __init__(self,year,merged_data_set):
	  self.year = year #the given year
	  self.merged_data_year = merged_data_set #the merged data
      def plot_boxplots(self):
	  '''this method will draw a boxplot of income distribution by region for a specific year'''
	  #group by Region to show the distribution
	  self.merged_data_year.boxplot('Income', by='Region', figsize = (10,8))
	  plt.ylabel('Income')
	  plt.savefig(str(self.year) + 'boxplot of income distribution' + '.png')

      def plot_histograms(self):
	  '''this method will draw a histogram of income distribution by region for a specific year'''
	  #get the regions
	  region_array = self.merged_data_year.Region.unique()
	  data_list = []
	  #get the data of each region
	  for region in region_array:
	      data_list.append(self.merged_data_year[self.merged_data_year['Region'] == region]['Income'])
	  region_list = region_array.tolist()
	  plt.figure(figsize=(10,8))
	  plt.hist(data_list,bins =15,stacked=True,label=region_list)
	  plt.xlabel('Income')
	  plt.title('Histogram of income distribution for the year of ' + str(self.year))
	  plt.legend()
	  plt.savefig(str(self.year) + ' histogram of income distribution' + '.png')




