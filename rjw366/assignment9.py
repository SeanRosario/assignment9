'''
Created on Nov 22, 2015

@author: rjw366
'''
import pandas as pd
import numpy as np
import graphHelper as gh
import sys

if __name__ == '__main__':
    #Read in data
    countries = pd.read_csv("../countries.csv")
    income = pd.read_excel("../indicator gapminder gdp_per_capita_ppp.xlsx",sheetname=0)
    income = income.set_index('gdp pc test').T
    print('The head of the newly loaded income dataset:')
    #Print as per the assignment
    print(income.head())
    while True:
        #Loop through until finish
        try:
            yearInput = raw_input('Enter year:')
            if(yearInput == 'finish'):
                break
            year = int(yearInput)
            gh.distOfIncomesByCountry(income,year)
        except ValueError as e:
            print 'There was an error with your input: ' + str(e)
        except KeyboardInterrupt:
            print "Program ended via keyboard"
            sys.exit(1)
    for i in range(5):
        joined = gh.merge_by_year(income, countries, int(2007+i))
        gh.exploringJoined(joined, int(2007+i))
    print("Files saved, program completed")
        