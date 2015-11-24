'''
Created on Nov 24, 2015

@author: ds-ga-1007
'''
import matplotlib.pyplot as plt

class Data_Analysis_Tools():
    def __init__(self,year,merged_data_set):
        self.year = year
        self.merged_data_year = merged_data_set
        
    def plot_box(self):
        self.merged_data_year.boxplot('Income', by='Region')) 
        plt.savefig(str(self.year)+' boxplot_of_income_distribution_by_region' +'.png')
        
    def plot_histogram(self):
        region_array = self.merged_data_year.Region.unique()
        data_list = []
        for region in region_array:
            data_list.append(self.merged_data_year[self.merged_data_year['Region'] == region]['Income'])
        region_list = region_array.tolist()
        plt.figure(1)
        plt.hist(data_list,bins =15,stacked=True,label=region_list)
        plt.xlabel('Income')
        plt.title(str(self.year)+' histogram of income distribution by region')
        plt.savefig(str(self.year)+' histogram_of_income_distribution_by_region' +'.png')
        
        
        
        
        
        
        