"""Author: Akash Shah (ass502)

contains the ExploreYear class, which represents 
income and region data for all countries for a given year"""

from helper import *

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as b_pdf

class ExploreYear:

	def __init__(self,income,countries,year):
		"""instantiates an income year object represented by a dataframe"""

		self.year = year
		self.data_df = merge_by_year(income,countries,year)

	def getRegions(self):
		"""returns series of regions in the current year's data"""
		
		return pd.unique(self.data_df['Region'].values.ravel())

	def plotRegionHistograms(self):
		"""plots individual histograms for each region's income distribution for the input year in one pdf file"""

		#create output pdf file to hold multiple plots 
		output = b_pdf.PdfPages('region_histograms_'+str(self.year)+'.pdf')
		for region in self.getRegions():
			#filter data for the current region
			region_data = self.data_df.loc[self.data_df['Region'] == region]

			#drop index
			region_data = region_data.reset_index(drop=True)
			
			region_income = region_data['Income']
			
			#create histogram for the current region
			plt.clf()
			plt.hist(region_income.dropna(),bins=20)

			#set axis labels and title
			plt.xlabel('Mean Income (per person)')
			plt.ylabel('Number of Countries')
			plt.title('Mean Income Per Capita in ' + region + ' in ' + str(self.year))

			#save plots to single pdf
			plt.savefig(output,format='pdf')
		output.close()

	def plotRegionsBoxplot(self):
		"""plots boxplots with the income distribution of each region on one plot for the input year"""
		
		#create array to hold income dataframe for each region
		data = []
		for region in self.getRegions():
			#filter data for the current region
			region_data = self.data_df.loc[self.data_df['Region'] == region]

			#drop index
			region_data = region_data.reset_index(drop=True)
			#get income data for the region
			region_income = region_data['Income']
			data.append(region_income)

		#create boxplots for each region in one plot
		plt.figure()
		plt.boxplot(data)

		#set xticks for each region, with the region name
		plt.xticks(np.arange(1,len(self.getRegions())+1),self.getRegions())

		#set axis labels and title
		plt.xlabel('Regions')
		plt.ylabel('Mean Income (per person)')
		plt.title('Income Distribution Per Capita by Region in '+str(self.year))

		#save plot
		plt.savefig('regions_boxplot_' + str(self.year) + '.pdf')





