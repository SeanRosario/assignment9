'''
Author: Minqing Zhuang

This program will ask for user input to generate different plots.
'''

import sys
import warnings
import pandas as pd
from functions import *
from tools import *


def main():
    '''
    question 7 and 8
    this function asks for user input and generates corresponding plots
    '''
    functions.load_trans_excel('indicator gapminder gdp_per_capita_ppp.xlsx')       # show the head of this data
    while True:
        yr_input = raw_input('Please enter a year between 1800 and 2012 to see the graph \nPlease enter finish if you would like to finish and the program will keep generating graphs \nPlease enter quit if you would like to exit the program\n')
        if yr_input == 'finish':
            break                   # break the loop to generate plots for years from 2007 to 2012
        elif yr_input == 'quit':
            sys.exit()
        elif int(yr_input) >= 1800 and int(yr_input) <= 2012:
            functions.plot_hist_by_year(int(yr_input))
        else:
            print '\n\nPlease make sure that the year you enter is in the range [1800,2012] and there is no space or other characters in your input\n'
    for yr in range(2007,2013):     # generate plots for years from 2007 to 2012
        data = tools(yr)
        data.boxplot_by_region()
        data.plot_hist_by_region()

if __name__ == '__main__':
    try:
        warnings.filterwarnings("ignore")           # ignore runtime warning
        main()
    except KeyboardInterrupt:
        print 'Program terminated by keyboard interruption, please re-run the program if you would like to continue'
    except ValueError:
        print 'Invalid values, please re-run the program if you would like to continue'
    except TypeError:
        print 'Incorrect types, please re-run the program if you would like to continue'