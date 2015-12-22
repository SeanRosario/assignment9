### Laura Buchanan 
### lcb402

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# This class organizes and analyzes the country and gdp data
class country_gdp(object):
	
	def __init__(self,year):
		self.year = year		

	# Functions to load data
	def load_countries(self):
		self.countries = pd.read_csv('../countries.csv',sep=',',header=0)
		return self.countries

	def load_income(self):
        	income = pd.read_csv('../indicator gapminder gdp_per_capita_ppp.csv',sep=',',header=0,index_col='gdp pc test')
		income = income.transpose()
		self.income = income.dropna(axis=1)
#		print self.income.head(n=5)
		return self.income 


	# Function to plot income per person across all countries in a given year 
	def plot_gdp_data(self):
    		data = self.income.loc[str(self.year)]
    		plot = plt.hist(data,bins=50)
   	 	plt.title('Income Per Person in ' + str(self.year))
    		plt.xlabel('Income Per Person in $')
    		plt.ylabel('# of Countries')
#    		plt.savefig('./income_per_person_in_' + str(self.year) + '.pdf')
		plt.close()

	# Function to merge countries and gdp data by year
	def merge_by_year(self):
    		income = self.income.loc[str(self.year)]
		income = pd.DataFrame(income)
    		income.reset_index(level=0, inplace=True)
    		income.rename(columns={'gdp pc test': 'Country',str(self.year):'Income'},inplace=True)
    		merged_data = pd.merge(self.countries,income,on='Country',how='outer')
    		self.merged_data = merged_data.dropna()
    		return self.merged_data

	# Function to explore gdp/region in a year with a histogram
	def hist_merged_data(self):
		income_data = self.merged_data['Income']
		regions = np.unique(self.merged_data[['Region']])
		income_list = []
		for i in regions:
			income_list.append(self.merged_data[self.merged_data['Region']==i]['Income'])
		plt.hist(income_list,stacked=True, bins=50, label=list(regions))
		plt.ylim(0,50)
		plt.ylabel('# Countries by Region')
		plt.xlabel('Per Captia GDP')
		plt.title('Per Capita GDP in %d' %self.year)
		plt.legend()
		plt.savefig('hist_gdp_by_region_{}.pdf'.format(self.year))
		plt.close()

        # Function to explore gdp/region in a year with a boxplot
	def boxplot_merged_data(self):
		self.merged_data.boxplot(column='Income', by='Region', rot='10', figsize=(10,8))
		plt.title('Per Capita GDP by Region in {}'.format(self.year))
		plt.ylabel('GDP (Mean and STD)')
		plt.xlabel('Region')
		plt.title('Per Capita GDP in %d' %self.year)
		plt.ylim(0,55000)
		plt.savefig('box_gdp_by_region_{}.png'.format(self.year))
		plt.close()
