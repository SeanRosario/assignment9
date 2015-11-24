'''
Created on Nov 13, 2015

@author: Rafael Garcia (rgc292)
'''

import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



"""This class is intended to do exploratory analysis"""

class Action(object):
    
    #This turns into True when user confirms 'finish' as input to print graph from 2007 to 2012 
    graph_2007_2012 = False

    def __init__(self):
        pass
        
    #Plot a bar graph for income distribution across countries for a given year    
    def plot_income_distribution(self, year, dataframe):
        self.year = year
        self.df = pd.DataFrame()
        self.df = dataframe
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        plt.title('Income Per Person Distribution Across Countries For ' + str(year), fontsize=90)
        plt.xlabel('Countries', fontsize=80)
        plt.ylabel('Income Per Person', fontsize=80)
        self.df.iloc[:][self.year].plot(kind='bar')
        ax.set_xticklabels(self.df.iloc[:]['gdp pc test'], rotation=85)
        fig.set_size_inches(100, 40, forward=True)
        fig.savefig('question4.pdf')
        plt.close('all')
        plt.clf()
        return
    
    #Merge indicator and countries datasets by year
    def merge_by_year(self, country, income, year):
        self.country = pd.DataFrame()
        self.income = pd.DataFrame() 
        self.merged = pd.DataFrame()
        self.renamed = pd.DataFrame()
        self.country = country
        self.income = income
        self.income.rename(columns={'gdp pc test': 'Country'}, inplace=True)
        self.merged = pd.merge(self.income[['Country', year]], self.country, on='Country', how='left') 
        return self.merged
    
    #Plot histogram having income per person per region for a given year
    def plot_histogram(self, dataframe, graph_year):
        global graph_2007_2012
        self.question_number = ''
        self.frame = pd.DataFrame()
        self.frame = dataframe
        self.frame = self.frame.dropna()
        self.regions = pd.unique(self.frame.Region)
        
        #It labels .pdf graphs based on the question it is addressing 
        if self.graph_2007_2012 == False:
            self.question_number = '6'
            
        else:
            self.question_number = '8'
        
        #It plots figures per region        
        for i in range(len(self.regions)):
            self.frame.loc[self.frame['Region'] == self.regions[i]]
            plt.figure()
            self.frame.plot(kind='hist', alpha=0.5)
            plt.ylabel('Number Of Countries Per Range', fontsize=10)
            plt.xlabel('Range Of Income Per Person', fontsize=10)
            plt.title('Distribution Of Countries Per Income Per Person '+'In ' + self.regions[i] + 
                                   ' For a Given Year', fontsize=11)
            self.file_name = 'histquestion' + self.question_number + self.regions[i] + str(graph_year) + '.pdf'
            plt.savefig(self.file_name)
            plt.close('all')
            plt.clf()
        return
    
    
    #Plot box plot having the frequency of countries per income per person per region for a given year
    def plot_box(self, dataframe, graph_year):
        global graph_2007_2012
        self.question_number = ''
        self.frame = pd.DataFrame()
        self.frame = dataframe
        self.frame = self.frame.dropna()
        self.regions = pd.unique(self.frame.Region)
        
        #It labels .pdf graphs based on the question it is addressing 
        if self.graph_2007_2012 == False:
            self.question_number = '6'
            
        else:
            self.question_number = '8'
        
        #It plots figures per region        
        for i in range(len(self.regions)):
            self.frame.loc[self.frame['Region'] == self.regions[i]]
            plt.figure()
            self.frame.plot(kind='box')
            plt.ylabel('Range of Income Per Person In The Region', fontsize=10)
            plt.xlabel('Year', fontsize=10)
            plt.title('Distribution Of Countries Per Income Per Person '+'In ' + self.regions[i] + 
                                   ' For a Given Year', fontsize=11)
            self.file_name = 'boxquestion' + self.question_number + self.regions[i] + str(graph_year) + '.pdf'
            plt.savefig(self.file_name)
            plt.close('all')
            plt.clf()
        return
    
    
        
        
        
        
        
           