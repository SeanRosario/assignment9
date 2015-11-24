"""this is the main program of asssignment9 that interact with users and generates the result """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from user_defined_exceptions import *
import re
import data_analysis_tools
import data_process_functions


#author: Muhe Xie
#netID: mx419
#date: 11/16/2015

def generate_answers_hw9():
    '''this function will generate answers of assignment 9 '''
    #Q1
    countries = pd.read_csv('countries.csv',sep=',')
    #Q2 load the xlsx data and on the sheet 'Data'
    income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',sheetname='Data',index_col=0)
    #Q3
    income_new = income.transpose()#the transpose of the dataframe income
    print "The head of the data set:"
    print income_new.head() 
    print "The data has been loaded successfully!\n"
    #the user interaction part
    while True:
        try:
            print "Please Enter a year from 1800 to 2012 to check the income distribution (for example: 2003), enter 'finish' to stop checking"
            print "(Hint:Close the plot window to continue)"
            year_input = raw_input()
            if year_input == "finish": #quit the program
                print "the check process is finished"
                break
            if year_input == "": #test empty input 
                raise Empty_Input_Error

            if not re.match(r'^[1-9][0-9][0-9][0-9]$',year_input):
                raise Invalid_Input_Error
            
            else:
                year_number = int(year_input)
                if year_number in income_new.index:
                    #Q4 display the distribution of income per person across all countries for the given year 
                    data_process_functions.display_income_dist_by_year(year_number,income_new)
                else:
                    raise Invalid_Input_Error

        except Empty_Input_Error:
            print "Warning: The input is empty! please re-enter the list"
            
        except Invalid_Input_Error:
            print "Warning: The input number is not valid! please re-enter the year"

    #generate the plots from 2007 and 2012
    print "the program is generating graphs for the years 2007-2012..."
    for year_ind in range(2007,2013):
        merged_data = data_process_functions.merge_by_year(year_ind,countries,income_new) # Q5
        data_analysis_instance = data_analysis_tools.Data_Analysis_Tools(year_ind, merged_data) #Q6
        data_analysis_instance.plot_boxplots() #Q8
        data_analysis_instance.plot_histograms() #Q8 

    print "Congratulations! the results are saved succeffully, thanks for trying ,bye"


if __name__ == "__main__":
    try:
        generate_answers_hw9()    

    except KeyboardInterrupt:
        print "the program has been interrupted by KeyboardInterrupt, thanks for trying,Goodbye"

    except EOFError:
        print "the program has been interrupted by EOF Error, thanks for trying, Goodbye"

    except IOError:
        print "the program has been interrupted by IO Error, thanks for trying, Goodbye"

    except TypeError:
        print "the program has been interrupted by TypeError, thanks for trying, Goodbye"

    except OverflowError:
        print "the program has been interrupted by OverflowError, thanks for trying, Goodbye"

