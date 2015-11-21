import pandas as pd
import numpy as np
import xlrd
import matplotlib.pyplot as plt

class DataImportError(Exception):
    '''Raised when data cannot be imported correctly'''
    pass

class IncomeDataController(object):
    '''Load and visualize income data'''

    def __init__(self, country_datafile, income_datafile):
        '''Constructor'''
        try:
            self.countries = pd.read_csv(country_datafile, index_col=0)
            self.income = pd.read_excel(income_datafile, index_col=0)
            # Set the index name to something more sensible
            self.countries.index.name = "Country"
            self.income.index.name = "Country"

            print "Loaded income data:\n", self.income.T.head()

        except (IOError, xlrd.XLRDError, pd.parser.CParserError):
            raise DataImportError("Could not read datafiles")

    def plot_income(self, year):
        '''Plot a historgram of the income distributions for a given year'''
        self.income[year].hist()
        plt.title("Distribution of Countries' GDP per Capita, %d" % year)
        plt.show()

    def merge_by_year(self, year):
        '''Merge income data for a given year with country/region data,
        returning the merged data frame'''
        merged =  self.countries.merge(pd.DataFrame(self.income[year]),
                                left_index=True, right_index=True)
        merged.reset_index(inplace=True)
        merged.columns = ["Country", "Region", "Income"]
        return merged
