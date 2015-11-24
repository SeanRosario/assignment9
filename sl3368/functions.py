import pandas as pd
import matplotlib.pyplot as plt 

countries = pd.read_csv('/Users/apple/Desktop/assignment9/countries.csv', index_col = 0)
income = pd.read_excel('/Users/apple/Desktop/assignment9/indicator gapminder gdp_per_capita_ppp.xlsx', index_col = 0)

income_trans = income.T 

# function used to show the head of the data set 
def showHead():

	income_head = income_trans.head()

	return income_head

# Q4: function used to display histogram
def plotDistribution(year):

	if year >= 1800 and year <= 2012:

		year_income = income_trans.ix[year].dropna()

		plt.figure()
		year_income.hist(bins = 60)
		plt.xlabel('Income per Person')
		plt.ylabel('Number of Countries')
		plt.title('Income per Person in year {}'.format(year))
		plt.show()

	else:
		raise ValueError('Sorry! You should input a year between 1800 and 2012')

# Q5: function used to merge data frames 
def merge_by_year(year):

	merge_countries = pd.read_csv('/Users/apple/Desktop/assignment9/countries.csv')
	merge_income = pd.read_excel('/Users/apple/Desktop/assignment9/indicator gapminder gdp_per_capita_ppp.xlsx')

	merge_year_income = merge_income[['gdp pc test', year]]
	merge_year_income = merge_year_income.rename(columns = {'gdp pc test':'Country'})
	merge_year_income = merge_year_income.rename(columns = {year:'Income'})
	merged_dataframe = pd.merge(merge_countries, merge_year_income, on = 'Country', how = 'right')

	return merged_dataframe

