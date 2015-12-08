'''
Created on Nov 17, 2015

@author: ams889

This program contains the functions used for assignment 9
'''
import pandas as pd
import matplotlib.pyplot as plt

countries = pd.read_csv('../countries.csv')
income = pd.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx', sheetname='Data')

new_columns = income.columns.values
new_columns[0] = 'Country'  #providing a better (in my opinion) name for the index to be used
income.columns = new_columns
income=income.T     #Transposing the dataset
income.head()
income.columns = income.ix[0] 
income=income[1:]    #Using the correct index and headers

def plotYearIncome(year):
    plt.figure();
    n, bins, _ = plt.hist(income.T[year].dropna(), bins=25); #build a histogram using buckets to reduce noise and give a better feel of distribution
    plt.title('Distribution of Income Per Person in {}'.format(year))
    plt.xlabel('Income Per Person (Dollars)')
    plt.ylabel('Frequency (Countries)')
    
def merge_by_year(year):
    mergedIncome=pd.merge(pd.DataFrame(income.T[year]), countries,left_index=True, right_on='Country') #Using the income country index to merge region on from countries dataset
    cols = mergedIncome.columns.tolist()
    cols = cols[1:] + cols[:1]  #Reordering the columns to fit the assignment
    mergedIncome=mergedIncome[cols]
    mergedIncome.columns = ['Country', 'Region', 'Income']   #Renaming the columns to fit the assignment
    return mergedIncome 