"""
this module include 2 functions to answer Q4 and Q5 
1. display the distribution of income per person across all countries 2. merge_by_year 
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#author: Muhe Xie
#netID: mx419
#date: 11/16/2015

def display_income_dist_by_year(year,income_data_set):
    '''Q4 This function will display the distribution of income per person across all countries for the given year '''
    dist_data_year =income_data_set.ix[year]
    plt.figure(figsize=(18,10))
    plt.title('Distribution of Income per person across all countries in ' + str(year)+' (x axis is income, y axis is frequence)')
    plt.hist(dist_data_year.dropna(),bins=15)
    plt.xlabel ('income')
    plt.show()

def merge_by_year(year, df_countries,income_all):
    '''Q5 This function will merge countries and income data sets for any given year '''
    income_year = income_all.ix[year]
    df_income = pd.DataFrame(income_year)
    df_income['Country'] = df_income.index
    df_result = pd.merge(df_countries,df_income,how='inner')
    df_result = df_result.rename(columns= {year:'Income'})
    # print df_result
    return df_result
