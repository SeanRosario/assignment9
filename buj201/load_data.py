'''
Created on Nov 17, 2015

@author: Benjamin Jakubowski (buj201)
'''
import pandas as pd

def load_countries():
    '''Reads in countries.csv from parent directory.'''
    try:
        countries = pd.read_csv('../countries.csv', header=0)
    except IOError:
        print "File not found- 'countries.csv' should be in the parent directory."
        countries = None
    return countries

def load_income():
    '''Reads in indicator gapminder gdp_per_capita_ppp.xlsx from parent directory.'''
    try: 
        income = pd.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx', sheetname=0, index_col=0)
    except IOError:
        print "File not found- 'indicator gapminder gdp_per_capita_ppp.xlsx' should be in the parent directory."
        income = None
    return income

def transpose_income():
    '''Transposes income dataframe.'''
    income = load_income()
    income = income.T
    return income

def show_transposed_income_head():
    '''Transposes income dataframe, then prints first 6 rows.'''
    income = transpose_income()
    print income.head(6)
    return income