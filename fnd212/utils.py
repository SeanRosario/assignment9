# Author: fnd212
# Functions to be usede by the rest of the program. 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import defined_exceptions

COUNTRIES_FILE = '../countries.csv'
INCOME_FILE = '../indicator gapminder gdp_per_capita_ppp.xlsx'

def merge_by_year(year, df1, df2):
	'''First filters df1 by year and then merges df1 and df2 by index and returns'''

# merge_by_year function was defined to receive 2 dataframes to avoid
# the use of global variables, which is usually not recommended in the
# literature
	try:
		merged = pd.merge(pd.DataFrame(df1[year]),df2,
							left_index=True,right_index=True,how='left')
		#how='left' used to preserve the entries in df1 even though there is 
		#no region to which associate the country. Nan will be placed if that is 
		#the case. 

		merged.index.name = 'Country'

	except KeyError:
		raise KeyError('Year not in df1 DataFrame')
		print df1
	except:
		raise defined_exceptions.FatalError('Dataframes can not be merged')

	return merged



def year_gdp_histogram(data, year ,region='World', save_path=''):
	''' Takes a dataframe, a year and a region, and saves a gdp_histogram
	of the number of countries in a certain GDP range. 
	If a save_path is provided, the figure is saved there instead of plotted
	interactively.
	To specify the region, the dataframe provided has to have a column named Region
	Function will look for the value of year either on the columns of the DataFrame
	or in its indexes, if not found ValueError will be returned.'''

	is_year_index = data.index.name == 'Year'
	are_regions = 'Region' in data.columns

	if (year not in data.index) and (year not in data.columns):
		raise ValueError('Year not valid for the dataframe provided')
	

	plt.figure(figsize=(15,10))

	if region == 'World':
		if is_year_index:
			patches = plt.hist(data.ix[year].dropna(),bins=35,color='lightblue')
		else:
			patches = plt.hist(data[year].dropna(), bins=35,color='lightblue')

	else:
		if 'Region' not in data.columns:
			raise ValueError('If region is specified, the dataframe has to have a column named Region')

		data_region = data[data.Region == region]
		
		if len(data_region) == 0: 
				raise ValueError('Invalid region requested')
		
		patches = plt.hist(data_region[year].dropna(),bins=35,color='lightblue')



	plt.title('Distribution of Income Per Person in {} ({})'.format(year,region))
	plt.xlabel('Income Per Person (USD)')
	plt.ylabel('# of countries')
	plt.xticks(patches[1],rotation=90)
	plt.grid()
	if not save_path:
		plt.show()
	else:
		plt.savefig('./figures/gdp_histogram_{}_{}.png'.format(year,region),format='png')

	plt.close()


def year_gdp_boxplot(data, year, save_path=''):
	''' Takes a dataframe, and a year and saves a boxplot of the GDP per region,. 
	of the number of countries in a certain GDP range. 
	If a save_path is provided, the figure is saved there instead of plotted
	interactively.'''	
	
	plt.figure(figsize=(15,10));

	data.dropna().boxplot(year, by='Region')
	plt.title('Boxplot of GDP by region in {}'.format(year))
	plt.ylabel('Income Per Person (USD)')
	plt.xlabel('Region')

	if not save_path:
		plt.show()
	else:
		plt.savefig('./figures/gdp_histogram_{}.png'.format(year),format='png')

	plt.close()





def load_dataframes():
	''' Load the dataframes in the required format and return them '''
	try:
		countries = pd.read_csv(COUNTRIES_FILE,index_col=0)
		
	except IOError:
		raise defined_exceptions.FatalError('Countries database not found in {}'.format(COUNTRIES_FILE))

	try: 
		income = pd.read_excel(INCOME_FILE, sheetname='Data',index_col=0)
		income = income.transpose()
		income.index.name = 'Year'
	except IOError: 
		raise defined_exceptions.FatalError('Income database not found in {}'.format(INCOME_FILE))		

	# Transpose income to set the columns as countries
	# and years as rows before returning
	return countries, income