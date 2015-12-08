'''
Created on Nov 17, 2015

@author: Benjamin Jakubowski (buj201)
'''
from merge_by_year import *

class Explore_year(object):
    '''
    Takes 'year' as an argument to its constructor.
    Public attributes include:
    1. self.year- the year passed as an argument
    2. self.data- all complete records (country, region, income) for that year
    Public methods include:
    1. construct_histograms()- constructs and saves histograms summarizing
    median income distribution worldwide and by region for given year.
    2. construct_boxplotss()- constructs and saves boxplots summarizing
    median income distribution worldwide and by region for given year.
    '''

    def __init__(self, year):
        '''
        Argument: year (integer in [1800, 2012]
        Constructs attributes:
        1. self.year- year passed as argument
        2. self.data - DataFrame with all complete records (Country, Region, Income)
        for the given year
        '''
        self.year = year
        self._all_data = merge_by_year(year)
        self.data = self._all_data[~self._all_data.Income.isnull()]
        
    def construct_histograms(self, use_max = True):
        '''Constructs histograms summarizing median income distributions worldwide
        and by region for the given year. Saves histograms in directory 'plots_by_year'.
        If this directory doesn't exist, saves plot in parent directory.'''
        
        #Determine max_income to set xlims
        max_income = round(max(self.data.Income)/1000.0) * 1000
        
        fig1 = plt.figure()   
        fig1.subplots_adjust(hspace=.35)
        ## Top plot- aggregte across all regions:
        plt.subplot(3,1,1)
        plt.hist(self.data.Income, bins=20, label="All\ncountries")
        ###note we want to plot the histograms over a constant range regardless of region,
        ###but for the years 2007-2012 (i.e. question 8) we want to keep the range
        ###constant across all years
        if use_max:
            plt.xlim(0,max_income)
        else:
            plt.xlim(0,100000)
        title1 = 'Distribution of per capita income by country for the year ' + str(self.year)
        plt.title(title1)
        plt.legend()
        
        ## Plots 2-6- subplots for each region
        grouped = self.data.groupby('Region')
        i = 0
        for region, subset in grouped:
            plt.subplot(3,3,4+i)
            plt.hist(subset['Income'].values, bins=10)
            if use_max:
                plt.xlim(0,max_income)
            else:
                plt.xlim(0,100000)
            plt.title(str(region).title())
            plt.locator_params(nbins=3,axis='x')
            i +=1
        try:
            filepath = 'plots_by_year/histogram_year_' + str(self.year)
            fig1.savefig(filepath)
        except IOError:
            filepath = 'histogram_year_' + str(self.year)
            fig1.savefig(filepath)
        return
    
    def construct_boxplots(self):
        '''Constructs boxplots summarizing median income distributions worldwide
        and by region for the given year. Saves boxplots in directory 'plots_by_year'.
        If this directory doesn't exist, saves plot in parent directory.'''
        
        data_to_plot = {'Worldwide':self.data.Income.values}
        grouped = self.data.groupby('Region')
        for region, subset in grouped:
            data_to_plot[region]=subset['Income'].values
        fig1 = plt.figure()
        ax = fig1.add_subplot(111)
        ax.boxplot(data_to_plot.values())
        keys = [str(x).title().replace(' ', '\n') for x in data_to_plot.keys()]
        ax.set_xticklabels(keys)
        ax.set_xlabel('Region')
        ax.set_ylabel('Median per capita income')
        ax.set_ylim(0,100000)
        title = 'Comparison of median per capita income distribution in ' + str(self.year)
        ax.set_title(title)
        try:
            filepath = 'plots_by_year/boxplot_year_' + str(self.year)
            fig1.savefig(filepath)
        except IOError:
            filepath = 'boxplot_year_' + str(self.year)
            fig1.savefig(filepath)
        return