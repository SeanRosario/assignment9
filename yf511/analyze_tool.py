#author Yichen Fan
'''This class is for Q5 used exploratory data analysis tools (histograms and boxplots) to graphically explore the 
distribution of the income per person by region data set from question 5 for a given year and save to individual files. '''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Input_merge import *

class analyze_tool(object):

	def __init__(self,year,merge_by_year):
		self.year = year
		self.merge_by_year = merge_by_year

	def hist_by_region(self):
		uniq_region = self.merge_by_year['Region'].unique()#get a unique list of each region
		income_region = [] #get income by region
		for i in uniq_region:
			income_region.append(self.merge_by_year[self.merge_by_year['Region']==i].Income)
		#df.hist('Income',by = df['Region'],xrot= 80, xlabelsize = 10, ylabelsize = 10, bins = 20, figsize = [10,10])
		plt.figure()
		plt.hist(income_region,stacked=True, bins=20,label = list(uniq_region))#show histogram of distribution by region
		plt.title('Histogram plot')
		plt.legend()
		plt.savefig('Histogram_by_region_in{}.png'.format(self.year))

	def by_boxplots(self):
		plt.figure()
		self.merge_by_year.boxplot(by='Region')
		plt.ylabel('Income per person')
		plt.title('Box Plot')
		plt.savefig('Box_Plot_by_region_in_{}.png'.format(self.year))