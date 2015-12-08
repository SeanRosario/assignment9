'''
Created on Nov 17, 2015

@author: Benjamin Jakubowski (buj201)
'''

from load_data import *
import matplotlib.pyplot as plt

def is_valid_year(year):
    '''Main input validation function- validates that the input year is in fact in the
    available in the income dataset.
    '''
    ## Get transposed income DataFrame
    income = transpose_income()

    ## Input validation for year:
    min_year = min(income.index)
    max_year = max(income.index)
    bad_input = 'Year must be between ' + str(min_year) + ' and ' + str(max_year) + '.'
    if year not in income.index:
        raise ValueError(bad_input)
    else:
        return True

def plot_income_by_year(year):
    '''Makes histogram showing distribution of median income for a given year.'''
    ## Input validation for year:
    if is_valid_year(year):
        pass
    
    ## Get transposed income DataFrame
    income = transpose_income()
       
    ## Determine the maximum per capita income for input year
    max_pp_income = int(1.2* max(income.loc[year,~(income.loc[year].isnull())]))
    
    ## Make histogram showing distribution for given year (with range from 0 to 1.2*max).
    title = 'Distribution of per capita income\nby country for year = ' + str(year)
    plt.figure()
    plt.hist(income.loc[year,~(income.loc[year].isnull())].values, bins=20, range=(0,max_pp_income*1.2))
    plt.xlabel('Per capita income by country')
    plt.ylabel('Frequency (count)')
    plt.title(title)
    plt.show()
    return