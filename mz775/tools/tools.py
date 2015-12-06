from functions import *
import pandas as pd
import matplotlib.pyplot as plt

class tools ():
    '''
    question 6
    This class will generate histograms and boxplots for different years
    '''
    def __init__(self,year):
        if year <= 2012 and year >= 1800:
            self.year = year
        else:
            raise ValueError ('year out of range')              # raise error if year is not in the range [1800,2012]

    def plot_hist_by_region(self):
        '''
        this function plots histogram for different regions in the year
        '''
        df = functions.merge_by_year(self.year)
        plt.figure()
        df.hist('Income',by = df['Region'],xrot = 90, bins = 30,figsize=(15,15))
        plt.savefig('income_by_region_hist_%d.png' %(self.year))

    def boxplot_by_region(self):
        '''
        this function plots boxplots for different regions in the year
        '''
        df = functions.merge_by_year(self.year)
        plt.figure()
        df.boxplot('Income',by = 'Region',rot=45)
        plt.title('Distribution of income per person by region in year %d' %(self.year))
        plt.savefig('income_by_region_boxplot_%d.png' %(self.year))