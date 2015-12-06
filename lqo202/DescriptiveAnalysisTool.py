"""
This script creates the class DescriptiveAnalysisTool and its corresponding Exception.
The class is generated using the charged dataframes of InitialCharge.py. It validates the year and raises and exception
if the argument does not fulfill the conditions.
The class also has a function that generates PDF-s of each region given the year inputted.
"""

__author__ = 'luisa'

import pandas as pd
from matplotlib import  pyplot as plt
import InitialCharge as ic

import warnings
warnings.simplefilter(action = "ignore", category = FutureWarning)

class DescriptiveException():
    def __init__(self, msg):
        self.msg = msg


class DescriptiveAnalysisTool:

    def __init__(self,year):
        if isinstance(year,int):
            if year>=1800 and year<=2012:
                data = ic.UtilsFunctions.merge_by_year(year)
                self.datamerged = data
                self.year = year
            else:
                raise DescriptiveException("Year is not in the interval of the data")
        else:
            raise DescriptiveException("Inputted value is not a number")


    def plotHistogramBoxPlot(self):
        data = self.datamerged
        TotalRegions = list(pd.unique(ic.UtilsFunctions.getDataCountries().Region.ravel()))
        for region in TotalRegions:
            datatoplot = data[data['Region'] == region]
            datatoplot = datatoplot.dropna()
            fig = plt.figure()
            fig.suptitle('Descriptive Plots for Income in '+region+' Year '+str(self.year)+' ' , fontsize=16)

            #Plotting the histogram
            axis1 = fig.add_subplot(211)
            datatoplot['Income'].hist()


            #Plotting the BoxPlot
            axis2 = fig.add_subplot(212)
            axis2.set_title= 'BoxPlot'
            datatoplot.boxplot('Income')
            fig.savefig('Exploratory_Analysis_'+region+'_'+str(self.year)+'.pdf')

        return  fig
