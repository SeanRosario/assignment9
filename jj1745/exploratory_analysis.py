'''
Created on Nov 23, 2015

@author: jj1745

The class that we merge years and perform exploratory data analysis
'''
from loader import loadCountries, transformIncome
import matplotlib.pyplot as plt

def merge_by_year(year):
    '''
    The required funtion for question 5
    '''
    income = transformIncome()
    countries = loadCountries()
    
    # get the income of a particular year
    income_year = income.loc[[year]]
    #transpose the dataframe back
    income_year = income_year.T
    income_year.index.name = 'Country'
    merged = countries.join(income_year, on = 'Country', how = 'right')
    merged.rename(columns = {year: 'Income'}, inplace = True)
    return merged
    

class ExploreYearlyData(object):
    '''
    For any given year, merge the data and perform data analysis.
    Specifically, boxplots and histograms are provided
    '''

    def __init__(self,year):
        '''
        Constructor
        '''
        self.year = year
        self.data = merge_by_year(year)
        
        # get rid of the NA entries
        self.data = self.data[~self.data.Income.isnull()]
    
    def plotHisto(self):
        '''
        plot the histogram based on data
        '''
        self.data['Income'].hist(by = self.data['Region'], xlabelsize = 8)
        plt.savefig('Histogram_Income_Year_' + str(self.year))
        
    def plotBox(self):
        '''
        boxplot of the data
        '''
        self.data.boxplot(by = 'Region', fontsize = 10)
        plt.savefig('Boxplots_IncomeBy_Region_Year_' + str(self.year))
        
        