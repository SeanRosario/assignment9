'''this is the functions for data process'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# question 4
def display_income_distribution(year, income_data):
    '''this is to graphically display the distribution of income per person across all countries in the world for the given year'''
    income_distribution = income_data.ix[year]
    plt.figure()
    plt.title('Distribution of income per person across all countries in the world for the year of ' + str(year))
    plt.hist(income_distribution.dropna())
    plt.xlabel('income per person')
    plt.ylabel('frequency')
    plt.show()

# question 5
def merge_by_year(year, countries, income_data):
    '''this is to merge countries and income data sets for a given year'''
    income_year = income_data.ix[year]
    income_year = pd.DataFrame(income_year)
    income_year['Country'] = income_year.index
    result = pd.merge(countries, income_year, how = 'inner')
    result = result.rename(columns = {year: 'Income'})
    return result



