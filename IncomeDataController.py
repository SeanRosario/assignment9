import pandas as pd
import numpy as np
import xlrd
import matplotlib.pyplot as plt
import DataExplorer as de
import os

class DataImportError(Exception):
    '''Raised when data cannot be imported correctly'''
    pass

class IncomeDataController(object):
    '''Load and visualize income data'''

    def __init__(self, country_datafile, income_datafile, output_dir = "output/"):
        '''Constructor. Load data on countries and income,
        and store them as dataframes.'''
        # If output directory can't be made, we want to throw the normal error
        self.output_dir = output_dir
        try:
            os.makedirs(self.output_dir)
        except OSError:
            pass # Means output folder already exists


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
        fig, ax = plt.subplots()

        xticks = np.arange(2, 5.5, 0.25)
        #xtick_labels = [100, 500, 1000, 5000, 7500, 10000, 25000, 50000, 75000, 100000]
        xtick_labels = (10**xticks).astype('int')

        np.log10(self.income[year]).hist(ax=ax, bins=xticks)
        plt.title("Distribution of Countries' GDP per Capita, %s" % year)
        plt.xlabel("Income (Log Scale)")
        #xtick_labels = [100, 500, 1000, 5000, 7500, 10000, 25000, 50000, 75000, 100000]

        plt.xticks(xticks, xtick_labels, rotation=90)
        #plt.xticks(np.log10(xtick_labels), xtick_labels)
        plt.yticks(np.arange(0, 55, 5))
        plt.show()

    def merge_by_year(self, year):
        '''Merge income data for a given year with country/region data,
        returning the merged data frame'''
        merged =  self.countries.merge(pd.DataFrame(self.income[year]),
                                left_index=True, right_index=True)
        merged.reset_index(inplace=True) # Change country from index to column
        merged.columns = ["Country", "Region", "Income"]
        return merged

    def plot_years(self, years):
        '''Loop through years and plot each one, saving results to files'''
        for year in years:
            merged = self.merge_by_year(year)
            explorer = de.DataExplorer(merged, year)
            explorer.save_plots(
                os.path.join(self.output_dir, 'hist%d.png' % year),
                os.path.join(self.output_dir, 'boxplot%d.png' % year)
            )
