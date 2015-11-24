import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

# author: Kaiwen Liu
''' These two functions will plot the distribution'''

class plots:

    def __init__(self, new_df, year):

        self.new_df = new_df
        self.year = year
        
    # boxplot
    def boxplot(self):
        plt.figure()
        self.new_df.boxplot('Income', by='Region')
        plt.title('Boxplot of Income per Person by Region in {}'.format(self.year))
        plt.ylabel('income per person $')
        plt.ylim(0, 100000)
        plt.savefig('boxplot_by_region_{}.png'.format(self.year))
    
    # i used the stacked distribution histogram as the second plot to display the distribution 
    def stackedhistogram(self):
        regions = self.new_df['Region'].unique() # returns an array of values in regions
        data = []
        for region in regions:
            data.append(self.new_df[self.new_df['Region']==region].Income)
    
        plt.figure()
        plt.hist(data, bins=20, stacked=True, label=list(regions))
        plt.title('Stacked Distribution of Income per Person by Region in {}'.format(self.year))
        plt.legend()
        plt.savefig('stacked_distribution_by_region_{}.png'.format(self.year))


