# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 21:24:55 2015

@author: YY
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def data_setup():
    countries = pd.read_csv("countries.csv",header=0, sep=',')
    income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx', sheetname='Data')
    
    # data setup
    income2 = income.transpose()
    income2.columns = income2.iloc[0]
    income3 = income2.ix[1:]
    return income3, countries
    
def merge_by_year(df,countries, year):
    graph0 = df.loc[year]
    graph1 = graph0.to_frame()
    graph1.reset_index(level=0, inplace=True)
    graph1.columns=['Country','Income']
    graph1[['Income']] = graph1[['Income']].astype(float)
    region_dic = dict(zip(countries['Country'], countries['Region'])) 
    graph1['region'] = graph1['Country'].map(region_dic.get)
    return graph1

class analysis(object):
    def __init__(self, income,countries, year):
        self.year = year
        self.df = merge_by_year(income,countries, year)
    
    def boxplot(self):
        self.df.boxplot(column='Income', by = 'region',rot='15', fontsize=9 )
        plt.title('Per Capita GDP by Region ' + str(self.year))
        plt.suptitle("")
        plt.ylabel('GDP')
        plt.xlabel('Region')
        plt.savefig('GDP_by_Region_Boxplot_'+ str(self.year))
        
    def hist(self):
        df2 = self.df[self.df.region.notnull()]
        df2['Income'].hist(by=df2['region'], range=(0,df2['Income'].max()), xlabelsize=8,rot='20',ylabelsize=9 )
        plt.suptitle('GDP by Region '+ str(self.year), fontsize = 18 )
        plt.savefig('GDP_by_Region_Histogram _'+ str(self.year))

        