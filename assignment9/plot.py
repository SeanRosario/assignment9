'''
Created on Nov 23, 2015

@author: Xu Xu
'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys


class plots:
    def __init__(self, new_df, year):
        self.new_df = new_df
        self.year = year
            
    def boxplot(self):
        plt.figure()
        self.new_df.boxplot('Income', by='Region')
        plt.title('Boxplot of Income per capita by Region in {}'.format(self.year))
        plt.ylabel('$ Income per capita')
        plt.ylim(0, 10000)
        plt.savefig('Boxplot_by_region_{}.png'.format(self.year))
        
    def stackedhistogram(self):
        regions = self.new_df['Region'].unique()
        data = []
        for region in regions:
            data.append(self.new_df[self.new_df['Region']== region].Income)
            
        plt.figure()
        plt.hist(data, bins = 20, stacked=True, label=list(regions))
        plt.title('Stacked Distribution of Income per capita by Regions in {}'.format(self.year))
        plt.legend()
        plt.savefig('StackedDistribution_by_Region{}.png'.format(self.year))