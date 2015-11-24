'''
This module provides a class that uses exploratory data analysis tools (histograms and boxplots) to graphically explore the distribution of the income per person by region data set for a given year. Save these graphs to individual files.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from data import *

class AnnualGDP():

    def __init__(self, countries, income, year):
        self.year = year
        self.countries = countries
        self.income = income
        self.df = merge_by_year(countries, income, year)


    def plot_region_hist(self):
        cleaned = self.df.dropna()
        cleaned['Income'].hist(by=cleaned['Region'], xlabelsize=10, ylabelsize=10, bins=20, figsize=[10,10])
        plt.suptitle('Income per Person by Region in Year' + self.year)
        plt.savefig('Histogram_Individual_Income_by_Region_' + self.year + '.pdf') 
      
    
    def plot_region_boxplot(self):
        cleaned = self.df.dropna()
        cleaned.boxplot('Income', by='Region')
        plt.ylabel('Income per person')
        plt.xlabel('Region')
        plt.savefig('Boxplot_Individual_Income_by_Region_' + self.year + '.pdf')

  
