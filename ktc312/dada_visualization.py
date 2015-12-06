__author__ = 'ktc312'
import matplotlib.pyplot as plt
from read_file import *

def histogram(year, income):
    # Provide a function to graphically display the distribution of income
    # per person across all countries in the world for the given year.
    plt.hist(income.loc[year].dropna().values, 100)
    plt.xlabel('Income per person across all countries')
    plt.ylabel('Number of counts')
    plt.title('Distribution of income {}'.format(year))
    plt.savefig('Distribution_of_income_{}.png'.format(year))
    plt.clf()

class exploratory_tools(object):
    # a class that uses exploratory data analysis tools (histograms and boxplots)
    # to graphically explore the distribution of the income per person by region
    # data set from question 5 for a given year.
    def __init__(self, year):
        self.year = year
        self.merged_income = merge_by_year(self.year)
        self.merged_income = self.merged_income.convert_objects(convert_numeric = True)

    def histogram(self):
        plt.figure()
        self.merged_income.hist(column = 'Income', by = 'Region', figsize = (10,8), bins =20,
                                sharex = True, sharey =True)
        plt.suptitle('Distribution of income in {}'.format(self.year))
        plt.savefig('Histogram_of_income_in_{}.png'.format(self.year))
        plt.clf()

    def boxplot(self):
        plt.figure()
        self.merged_income.boxplot(column = 'Income', by = 'Region', figsize = (10,8), rot = 25)
        plt.title('Per Capita GDP by Region in {}'.format(self.year))
        plt.savefig('Boxplot_{}.png'.format(self.year))
        plt.clf()
