'''
Created on Nov 17, 2015

@author: Benjamin Jakubowski (buj201)
'''
from global_income_pp_by_year import *

def merge_by_year(year):
    '''
    Merges the country and income dataframes for an input year between 1800 and 2012.
    Returns merged dataframe.
    '''
    ##Validate input year
    if is_valid_year(year):
        pass
    
    ##Load income data and extract two desired features
    income = load_income()
    income['Country'] = income.index
    income = income.reset_index()
    income = income[['Country', year]]
    income.columns = ['Country','Income']
    
    #Load countries data
    countries = load_countries()
    
    #Merge income and countries
    merged = pd.merge(countries, income, how='inner', on='Country')
    return merged


    
    
    