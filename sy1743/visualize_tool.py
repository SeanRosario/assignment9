import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from hw9_functions import merge_by_year

# DS-GA 1007
# HW9
# Author: Sida Ye
"""This class is going to generate boxplots and histograms of income based on region"""

class visualize_tool(object):
    def __init__(self, year):
        if year <= 2012 and year >= 1800:
            self.year = year
        else:
            raise KeyError('Invalid Year!')

    def plot_boxplot(self):
        plt.figure()
        data = merge_by_year(self.year) # use merge_by_year to get income by year
        data.boxplot('Income', by='Region')
        plt.ylabel('Income')
        plt.savefig('boxplot_by_region_in_{}.png'.format(self.year))

    def plot_hist(self):
        data = merge_by_year(self.year)
        reg_uniq = data['Region'].unique() # get a unique list of region
        income_by_reg = []  # calculate income by region
        for item in reg_uniq:
            income_by_reg.append(data[data['Region']==item].Income)

        cm = plt.get_cmap('coolwarm')   # select a map color
        colors = [cm(x) for x in [0.167, 0.333, 0.5, 0.666, 0.833, 1]]  # seperate the color into different levels for different region
        plt.figure()
        plt.hist(income_by_reg, stacked=True, bins=30, color=colors, label=list(reg_uniq))  # use stacked histogram to show the distribution of income by region
        plt.title('Distribution of Income per Person by Region in {}'.format(self.year))
        plt.legend()
        plt.savefig('dist_by_region_{}.png'.format(self.year))
