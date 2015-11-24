import pandas as pd
import numpy as np
from pandas import ExcelFile
from pandas import DataFrame
import matplotlib.pyplot as plt

'''First, read the given data into separate dataframes'''
countries = pd.read_csv('countries.csv', index_col = 'Country')
income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx', sheetname = 'Data', index_col = 'gdp pc test')


def switch_rows_columns(data):
    '''Function that takes in a dataframe and returns the transpose,
    along with printing the header of the transpose'''
    transpose = pd.DataFrame.transpose(data)
    print list(transpose.columns.values)  
    return transpose


def income_by_year(year):
    '''Function that takes in a year between 1803 and 2012, and plots a
    histogram of the distribution of income per person across all countries
    (on which we have data)'''
    #test if the input is a valid year
    try:
        year = int(year)
        if year<1803 or year>2012:
            raise ValueError
    except ValueError:
        pass
          
    else:
        #drop all NA values in income for the given year
        data = income[year].dropna()
        #plot the histogram
        plt.hist(data, bins = 30)
        plt.xlabel('Average Income Per Person in year ' + str(year))
        plt.ylabel('Number of Countries')
        plt.title('Distribution of Income Across All Countries in ' + str(year))
        plt.show()


def merge_by_year(year):
    '''Function that takes in a year, merges the dataframes countries and income
    according to that year, and returns a merged dataframe'''
    #test if the input is a valid year
    try:
        year = int(year)
        if year<1803 or year>2012:
            raise ValueError
    except ValueError:
        pass
    else:
        #create the dataframe
        df = pd.DataFrame.join(countries, income[year], how = 'left')
        df = df.rename(columns = {year : 'Income'})
        df = df.dropna(how = 'any')
        return df
    





    
