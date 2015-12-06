'''
Created on Nov 24, 2015
@author: Urjit Patel - up276
'''

import numpy as np
import matplotlib.pyplot as plt

class Region_Exception(Exception):
    '''
    User defined exception for the region class
    '''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Region:

    def __init__(self,name,data):
        """
        Constructor for the class Region. It will be called at the time of object intialization
        """
        try:
            self.name = name
            self.data = data
            self.region_income = self.data['income'].values
            self.region_countries = self.data['Country'].values

        except:
            raise Region_Exception(" Initialization error ")

    @staticmethod
    def plot_BoxPlots(region_names,list_of_region_income_data,user_input,directory_name):
        '''
        This function receives the list of lists having all regions data and plots the Box Plot
        '''
        try:
            plot_name = directory_name+'/Box_plot_'+user_input
            plt.figure(figsize=(8,15))
            bp = plt.boxplot(list_of_region_income_data,patch_artist=True)

            for box in bp['boxes']:
                clr = (np.random.rand(), np.random.rand(), np.random.rand())
                box.set(color=clr, linewidth=2)
                clr = (np.random.rand(), np.random.rand(), np.random.rand())
                box.set(facecolor = clr)


            plt.xlabel('Region')
            plt.ylabel('Income')
            plt.title('Box Plots grouped by REGION')
            plt.xticks(np.arange(1,7),region_names,rotation='vertical')
            plt.savefig(plot_name)
            plt.clf()
        except KeyboardInterrupt:
            print "Program Interrupted...!!!"
        except:
            raise Region_Exception(" While plotting and saving Box Plot for the year",user_input)

    @staticmethod
    def plot_Hist_Graphs(region_object,user_input,directory_name):
        '''
        This function plots the Histograms for the region object using which it has been called
        '''
        try:
            plot_name = directory_name+'/Histogram_'+region_object.name+'_'+user_input
            plt.figure(figsize=(8,15))
            region_object.data.hist(bins=10)
            plt.savefig(plot_name)
            plt.clf()
        except KeyboardInterrupt:
            print "Program Interrupted...!!!"
        except:
            raise Region_Exception(" While plotting and saving Histograms for the year",user_input)

