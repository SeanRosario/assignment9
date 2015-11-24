'''
Created on Nov 24, 2015

@author: ds-ga-1007
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def display_income_per_person(year,income_dataset):
    dist_data_year =income_dataset.ix[year]
    plt.figure(1)
    plt.title('Distribution of Income per person across all countries in ' + str(year))
    plt.hist(dist_data_year.dropna(),bins=15)
    plt.xlabel ('income')
    plt.show()

def merge_by_year(year, df_countries,income_dataset):
    income_year = income_dataset.ix[year]
    df_income = pd.DataFrame(income_year)
    df_income['Country'] = df_income.index
    df_result = pd.merge(df_countries,df_income,how='inner')
    df_result = df_result.rename(columns= {year:'Income'})
    return df_result





