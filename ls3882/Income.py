import pandas as pd
import matplotlib.pyplot as plt


class Income:
    '''This class will process the income data and generate relative plots'''
    def __init__(self):
        '''This function will load the data to Dataframe'''
        #Load countries information
        self.countries = pd.read_csv('countries.csv', index_col=0)
        #self.countries = self.countries.set_index('Country')
        self.countries.index.name = None
        self.countries.columns.name = 'Country'
        #Load and transform the income data to have years as the rows and countries as the columns
        temp = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx', sheetname='Data', index_col=0)
        self.income = temp.transpose()
        self.merged = self.countries
        print 'Head of merged data:'
        print self.income.head()
	


    def income_dist(self, year):
        '''This function will generate a histogram showing
        the distribution of income per capita for the year given.'''
        plt.figure()
        data = self.income.loc[[year]]
        data = data.dropna(axis=1)
        data = data.as_matrix().T
        plt.hist(data)
        plt.xlabel('Income')
        plt.ylabel('Number of Countries')
        plt.title("Income per Capita " + str(year))
        plt.show()

    def merge_by_year(self, year):
        '''This function will merge the income data for the given year with countries information. '''
        data = self.income.loc[[year]].transpose()
        self.merged.loc[:, 'Income'] = data.loc[:,year]
	

    def region_income_dist(self, year):
        '''This function will generate a histogram and a boxplot of the income data grouped by region.'''
        #histogram
        self.merged.hist(column='Income', by=self.merged['Region'], xrot=45, xlabelsize=8)
        plt.savefig('Income_Hist_' + str(year) + '.jpg')
        #boxplot
        self.merged.boxplot(column='Income', by='Region', fontsize=10)
        plt.suptitle('')
        plt.savefig('Income_Box_' + str(year) + '.jpg')

    def plot_2007_2012(self):
        '''This function will generate histograms and boxplots of the income data from 2007 to 2012. '''
        years = [2007,2008,2009,2010,2011,2012]
        for i in years:
            self.merge_by_year(i)
            self.region_income_dist(i)
