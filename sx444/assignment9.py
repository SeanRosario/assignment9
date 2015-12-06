'''Homework 9'''
'''Siyi Xie(sx444)'''
'''This is the main program to generate the results of assignment9'''
   
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import data_analysis_tools
import data_process_functions
from user_defined_exceptions import *

def generate_answers():
    '''this is to generate the answers'''
    # question 1
    countries = pd.read_csv('./countries.csv', sep= ',') 
    # question 2
    income = pd.read_excel('./indicator gapminder gdp_per_capita_ppp.xlsx', sheetname='Data', index_col=0) 
    # question 3
    income2 = income.transpose() 
    print "The head of the data set is:"
    print income2.head()

    while True:
          try:
             print "Please Enter a year from 1800 to 2012 to check the income distribution (hint: enter 'finish' to stop displaying)"
             year_input = raw_input()
             if year_input == "finish": 
                break
             if year_input == "": 
                raise Empty_Input_Error
             if not re.match(r'^[1-9][0-9][0-9][0-9]$',year_input):
                raise Invalid_Input_Error
             else:
  	        year_number = int(year_input)
             if year_number in income2.index:
               # question4: display the distribution of income per person across all countries for the given year
                data_process_functions.display_income_distribution(year_number,income2)
             else:
                raise Invalid_Input_Error
          except Empty_Input_Error:
 	         pass
          except Invalid_Input_Error:
                 pass

    # question 8: generate graphs for the years of 2007-2012
    print "The graphs for 2007-2012 are generating..."
    for year_i in range(2007,2013):
        merged_data = data_process_functions.merge_by_year(year_i, countries, income2)
        graph_data = data_analysis_tools.data_analysis(year_i, merged_data)
        graph_data.plot_histograms()
	graph_data.plot_boxplots()
    print "The graphs for 2007-2012 have been successfully generated. Please check the directory. Thanks!"

if __name__ == "__main__":
   try:
      generate_answers()
   except KeyboardInterrupt:
          pass
   except EOFError:
          pass
   except IOError:
          pass
   except TypeError:
          pass
   except OverflowError:
          pass

