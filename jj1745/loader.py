'''
Created on Nov 23, 2015

@author: jj1745

This module contains functions for loading and processing data
'''

import pandas as p

def loadCountries():
    '''
    load the file countries.csv from the parent folder since files are located there
    '''
    try:
        countries = p.read_csv('../countries.csv')
        return countries
    except IOError:
        # the case where the file is not in the correct folder
        print 'No file in directory. Please place the file in the correct folder'
        

def loadIncome():
    '''
    load the file indicator gapminder gdp_per_capita_ppp.xlsx
    '''
    try:
        income = p.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx', sheetname = 0, index_col = 0)
        return income
    except IOError:
        # the case where the file is not in the correct folder
        print 'No file in directory. Please place the file in the correct folder'
        

def transformIncome():
    '''
    transform the data so that rows are years and columns are countries
    '''
    income = loadIncome()
    
    # transpose the data
    income = income.T
    return income
