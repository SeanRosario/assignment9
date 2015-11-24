'''
Created on Nov 17, 2015

@author: ams889

This program builds plots using country and region income data based on user input of year
'''
import pandas as pd
import matplotlib.pyplot as plt
from functions import *
from dataAnalysisClass import *
import sys

if __name__ == "__main__": 
    try:
        while True:
            yearInput = raw_input("Please enter a year (or 'Finish' to quit): \n")
            if yearInput.lower() == "finish":
                for yr in range(2007, 2013):
                    data=dataAnalysisClass(yr)
                    data.boxPlot()
                    plt.close()
                    data.histPlot()
                    plt.close()
                break;
            try: 
                year = int(yearInput)
                if year>=1800 and year<=2012:
                    plotYearIncome(year)
                    plt.show()
                else:
                    print("Year must be between 1800 and 2012")
            except:
                raise YearNotAnIntError("Year must be specified in integer form")
    except ValueError:
        print 'Incorrect Input'
    
    except KeyboardInterrupt:
        print "Program Terminated"
        sys.exit(1)
