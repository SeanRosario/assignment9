'''
Created on Nov 17, 2015

@author: ams889

This program creates a class object to be used in exploratory data anlysis as well as a user defined exception class
'''
import pandas as pd
import matplotlib.pyplot as plt
from functions import *

class YearNotAnIntError(Exception):
    #Base class for yearError user defined exception
    pass

class dataAnalysisClass(object):
    #Class used to generate box and histogram plots for a given year
    def __init__(self, year):
        try:
            int(year)
        except:
            raise ValueError("Year must be specified in integer form")
        if year<1800 or year >2012:
            print("Year must be between 1800 and 2012")
        self.year=year
    
    def boxPlot(self):
        dataset = merge_by_year(self.year) #to merge region onto our dataset for the given year to establish our plot values
        dataset.boxplot('Income', by='Region')
        plt.title('Boxplot of Income per Person by Region in {}'.format(self.year))
        plt.ylabel('Income Per Person (Dollars)')
        plt.xlabel('Region')
        plt.savefig('regionBoxPlot{}.png'.format(self.year))
    
    def histPlot(self):
        plotYearIncome(self.year) #calls function we built in question 4
        plt.savefig('regionHistPlot{}.png'.format(self.year))