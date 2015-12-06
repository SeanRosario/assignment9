'''
Created on Nov 13, 2015

@author: Rafael Garcia (rgc292)
'''

import sys
import validation as val
import load_data as ld
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import actions as ac

"""This main file is intended to run the whole program for the user"""

if __name__ == '__main__':
    pass

#Variables used within the main file
valid = val.Validation()
iteration = True
load = ld.Load_data()
countries = pd.DataFrame()
income = pd.DataFrame()
action = ac.Action()
merged_datasets = pd.DataFrame()
year = 0


#Main loop keeping the program running
while iteration:
    #Attempt to catch possible exceptions
    try:
        #Output for the validation process and the year value from input
        output, year  = valid.validate_input(raw_input('Please, type a year from' + 
                       ' 1800 to 2012 inclusive like this format: >>> '))
        countries = load.read_csv_file('countries.csv') 
        income = load.read_xlsx_file('indicator' + 
                                       ' gapminder gdp_per_capita_ppp.xlsx')
        income_transposed = pd.DataFrame.transpose(income)
        
        if (output == False and len(countries) != 0 and len(income) != 0):
            print income_transposed.head()
            action.plot_income_distribution(year, income)
            merged_datasets = action.merge_by_year(countries, income, year) 
            action.plot_histogram(merged_datasets, '')
            action.plot_box(merged_datasets, '')
            
        elif output == True:
            iteration = False
            action.graph_2007_2012 = True
            print 'Printing graphs...'
            continue     
        
    except (EOFError, SystemExit, KeyboardInterrupt):
        print "Good Bye!"
        sys.exit(1)
        
        
#Attempt to catch possible exceptions
try:     
    #Print graphs from 2007 to 2012 after 'finish' as input   
    for i in range(2007,2013):
        merged_datasets = action.merge_by_year(countries, income, i) 
        action.plot_histogram(merged_datasets, i)
        action.plot_box(merged_datasets, i)
        
except (EOFError, SystemExit, KeyboardInterrupt):
    print "Good Bye!"
    sys.exit(1)
    




   