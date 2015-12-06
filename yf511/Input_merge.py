import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
#%matplotlib inline

#author Yichen Fan
#Q1 load file into a pandas Dataframe called countries
def load_countries_csv():
	countries=pd.read_csv('countries.csv',header=0)
	countries=pd.DataFrame(countries)
	print countries.head(3)
	return countries
#Q2 load file into a pandas Dataframe called income and transformed
def load_gdp_csv():
	income=pd.read_csv('indicator gapminder gdp_per_capita_ppp.csv', index_col='gdp pc test')
	income_trans = income.T
	print income_trans.head()
	return income_trans
#Q5 merge countries and income data sets for any given year
def merge_by_year(income, countries, year):
	in_in = income.ix[year,:]
	in_in.name='Income'
	in_in.index.name='Country'
	merged_df = pd.merge(pd.DataFrame(in_in),countries, left_index = True, right_on ='Country', how = 'inner')
	return merged_df
    