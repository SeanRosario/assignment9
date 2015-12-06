'''
Created on Nov 25, 2015

@author: ds-ga-1007
'''
import pandas as pd
import matplotlib.pyplot as plt

class Data_Analysis_tools():
    def __init__(self,year,merged_dataset):
        self.year=year
        self.merged_dataset=merged_dataset
        
    def plot_box(self):
        self.merged_dataset.boxplot('Income',by='Region')
        plt.ylabel('Income')
        plt.savefig('boxplot of income by region in '+str(self.year)+'.png')
    
    def plot_hist(self):
        region_array=self.merged_dataset.Region.unique()
        data_list=[]
        for region in region_array:
            data_list.append(self.merged_dataset[self.merged_dataset['Region']==region]['Income'])
        region_list=region_array.tolist()
        print type(region_list)
        plt.hist(data_list,stack=True,label=region_list)
        plt.ylabel('Income')
        plt.legend()
        plt.savefig('histogram of income by region in '+str(self.year)+'.png')
    