'''
Created on Nov 23, 2015

@author: Xu Xu
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from plot import *
from merge import *

# the main function can import csv file, merge and plot the information

def main():
    #load the countries.csv into pandas DataFrame
    countries = pd.read_csv('countries.csv', index_col=0)
    countries = pd.DataFrame(countries)
    print countries.head() #output the head of countries file
    
    income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx', index_col = 'gdp pc test', sheetname = 'Data')
    income = pd.DataFrame(income) 
    income_t = pd.DataFrame(income).transpose() #transpose year as rows and countries as columns
    
    print income_t.head() #output the head of income
    

    while True:
        try:
            year = raw_input('enter a year for details:')
            if year == 'finish':
                break
            else:
                year = int(year)
                if year < 1800 or year > 2012:
                    raise ValueError
                
                    
        except (KeyboardInterrupt, ValueError):
            print "See you"
            sys.exit()
         #generate the distribution of given year    
        data = income[year]
        plt.figure()
        plt.hist(data.dropna(), bins = 20, color = 'red')
        plt.title('Distribution of income aross countries in {}'.format(year))
        plt.xlabel('$ income per person')
        plt.show()
        
        
        for year_ in range(2007, 2013):
            df = merge_by_year(income, countries, year_)
            
            plots(df, year_).stackedhistogram()
            plots(df, year_).boxplot()
            
        
        
        
if __name__ == '__main__':
    main()
    
    
    