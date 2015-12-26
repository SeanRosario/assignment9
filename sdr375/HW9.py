__author__ = 'Sean D Rosario'
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():

	global countries
	countries = pd.read_csv("countries.csv")
	countries = countries.dropna()
	global income
	income = pd.read_excel("indicator gapminder gdp_per_capita_ppp.xlsx")
	income = income.dropna()
	income = income.T

	income.columns = (income.iloc[0]).tolist()
	income = income.drop('gdp pc test')
	

	input_from_user()

def one_year_plot(input_year):
	"""Plots a histogram of incomes for a given year in 20 bins"""
	list_of_countries = income.columns.values
	y_pos = np.arange(len(list_of_countries))
	incomes = income.loc[input_year]
	plt.hist(incomes,bins = 20)
	plt.show()
	plt.close()
	

def merge_by_year(year):
	"""Merges the two dataFrames"""
	columns = ('Country','Income')
	list_of_countries = income.columns.values
	df= pd.DataFrame(columns= columns)
	df['Income']=income.loc[year]
	df['Country']= list_of_countries
	df = df.merge(countries)
	return df


def income_per_region(year):
	df = merge_by_year(year)
	my_dict = {}
	Regions = df['Region'].unique()
	for i in Regions:
	    my_dict[i] = []
	
	for i in range(len(df)):
		my_dict[df.loc[i]['Region']].append(float(df.loc[i]['Income']))

	data =[]
	for key in my_dict:
		data.append(my_dict[key])
	plt.boxplot(data)
	list_of_x_labels = []
	for i in my_dict:
		list_of_x_labels.append(i)
	plt.xlabel(list_of_x_labels)
	plt.savefig('boxplot by regions for the year {0}.png'.format(year))
	

def generate_graphs():
	"""Generating the plots for the years 2007-2012"""
	for i in np.arange(2007,2013):
		one_year_plot(i)
		income_per_region(i)





def input_from_user():
	"""Takes input from user and generates the plots"""
	
	try:
		year = 0
		while(True):
			year = str(raw_input('Enter a year: '))
			if str(year) == "finish":
				break
			if int(year)>=1800 and int(year)<=2012:
				year = int(year)
				one_year_plot(year)
				income_per_region(year)
			else:
				print "Not a valid input"
	except IOError:
		print "Fatal input."
	generate_graphs()


if __name__ == "__main__":
	try:
		main()
	except:
		print "Error"







