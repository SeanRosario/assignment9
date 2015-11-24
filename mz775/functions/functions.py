import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
'''
This program contains answer of first 5 questions
'''
def load_csv(file_path):
    '''
    question 1
    this function loads the csv file into python as data frame
    '''
    df = pd.read_csv(file_path,index_col=0)             # df stands for data frame
    return df

def load_trans_excel(file_path):
    '''
    question 2 and 3
    this function loads and transpose the excel file into data frame
    '''
    df = pd.read_excel(file_path,index_col=0)
    print df.T.head()
    return df.T                                         # return the transposed result

def plot_hist_by_year(year):
    '''
    question 4
    this function plots the histogram by years
    '''
    df = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',index_col=0).dropna()  # drop NaN values
    df.T.ix[year].hist(bins=30)
    plt.title('Distribution of income per person in year %d' % (year))
    plt.show()

def merge_by_year(year):
    '''
    question 5
    this function creates a new data frame that merges from the other two data frame
    '''
    income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',index_col=0).T
    countries = pd.read_csv('countries.csv',index_col=0)
    country_region_to_merge = countries.reset_index()
    income_to_merge = pd.DataFrame(income.ix[year].dropna(),index=None).reset_index()
    income_to_merge.columns = ['Country','Income']
    final_df = pd.merge(country_region_to_merge,income_to_merge,how='left')
    return final_df.dropna()
