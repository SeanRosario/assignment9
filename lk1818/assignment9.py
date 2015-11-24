'''
Li Ke 
lk1818
11/24/2015
This is the main program. It loads two data sets from the files, modifies them into appropriate formats, saves plots of income distribution by region for 2007-2012. Lastly, it prompts the user for a year and generates graphs of income distribution for that year.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from data import *
from gdp_class import *
from interaction import *
from plot import *

def main():
    print "Start. Load Data."

    countries, income = load_data()

    print ("The head of income data set:\n", income.head()) #display the head of income data set
 
    get_year(income) #prompt the user for a year and displays a histogram of income distribution across all countries

    for year in range(2007, 2013): #generate and save histograms and boxplots of income distribution by region from 2007 to 2012
        year = str(year)
        print ('Saving graphs for Year ' + year + '...')
        annualGDP = AnnualGDP(countries, income, year)
        annualGDP.plot_region_hist()
        annualGDP.plot_region_boxplot()
        plt.close()

    print ('Saving complete. Quitting...')
        
      
    



if __name__ == "__main__":
    main()

    
    
    
