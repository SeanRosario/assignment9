'''
Created on Nov 23, 2015

@author: jj1745

This module contains functions that read in year and plot the distribution
'''

from loader import transformIncome
import matplotlib.pyplot as plt
import sys

def checkYear(input):
    '''
    check if the input year exists in the data
    '''
    income = transformIncome()
    
    # create a list of years appearing in the data
    year_list = list(income.index)
    
    if input.isdigit():
        year = int(input)
        if year in year_list:
            return True
        else:
            return False
    else:
        return False
    
        
    
def plotIncome(input):
    '''
    given a valid input, plot the distribution of the income
    '''
    income = transformIncome()
    
    title = 'Distribution of income per capita in ' + input
    
    # columns not included in our plot
    year = int(input)
    null_idx = income.loc[year].isnull()
    values = income.loc[year, ~null_idx].values
    plt.figure()
    
    # plot the histogram
    plt.hist(values, bins = 20)
    plt.title(title)
    plt.ylabel('Frequency')
    plt.xlabel('Income per capita')
    plt.show()

def provideYearlyPlot():
    '''
    The function that gets user inputs and plots
    '''
    while True:
        # keep asking for inputs
        plt.close()
        try:
            input = raw_input('Please enter a valid year, e.g. from 1800 to 2012. Enter finish if you want to exit.')
            if input == 'finish':
                # break if 'finish' is entered
                break
            if checkYear(input):
                plotIncome(input)
            else:
                # when the input is not valid
                print 'Your input is not valid. Please re-enter!'
        except KeyboardInterrupt:
            sys.exit()
            