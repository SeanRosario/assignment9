import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

# DS-GA 1007
# HW9
# Author: Sida Ye

"""This file contains functions from Question 1 to Question 5"""

# Q1
def import_csv(file_path):
    """ import data from csv """
    
    data = pd.read_csv(file_path, index_col=0)
    
    return data


# Q2 & Q3
def import_and_transform(file_path):
    """ import data from xlsx and transform rows and columns """

    data = pd.read_excel(file_path, index_col=0)
    data_trans = data.transpose()
    print data_trans.head()
    return data_trans


# Q4
def plot_income_by_yr(yr):
    """ generate histogram of income by year """

    data = pd.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx', index_col=0)
    if yr <= 2012 and yr >= 1800:
        result = data[yr]
        plt.figure()
        plt.hist(result.dropna(), bins=20)
        plt.title('Distribution of income per person in {}'.format(yr))
        plt.show()
    else:
        raise KeyError('Invalid Year!')


# Q5
def merge_by_year(year):
    """ This function is going to merge the countries and income for any given year.
        It will return a dataframe with three columns titled country, region and Income.
    """

    countries = pd.read_csv('../countries.csv', index_col=0)   
    income = pd.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx', index_col=0)
    income_year = income[year].to_frame()
    income_year.reset_index(level=0, inplace=True)
    income_year.columns = ['Country', 'income']
    countries.reset_index(level=0, inplace=True)
    countries.columns = ['Country', 'Region'] 
    result = pd.merge(countries, income_year, how='left')
    result.columns=['Country', 'Region', 'Income']
    return result





