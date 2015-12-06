'''
This module is for data importing, transforming, and merging.
'''

import pandas as pd
import numpy as np


def load_data(): #this function reads the files and creates two data frames: countries and income in desired format.
    
    countries = pd.DataFrame(pd.read_csv('./countries.csv'))
    income = pd.DataFrame(pd.read_csv('./indicator_gapminder_gdp_per_capita_ppp.csv'))
    income = income.transpose() #transpose income data set so that row indexes are years
    return [countries, income]




def merge_by_year(countries, income, year):
    '''
    Provide a function called merge_by_year(year) to merge the countries and income data sets for any given year. The result is a DataFrame with three columns titled Country, Region, and Income.
    '''
    try:
        int(year)

    except KeyError:
       print ('Invalid input type.')

    else:
        try:
            merged_income = countries.join(income.ix[str(year)], how='inner')
        except KeyError:
            print ('Invalid year.')
        else: 
            merged_income.columns = ['Country', 'Region', 'Income']
            return merged_income



