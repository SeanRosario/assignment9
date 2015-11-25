__author__ = 'sb5518'


"""
The loader_merger_histogram class in this module contains three Functions:

- load_data receives the names of two files with the variables file_countries_dict, file_income_data

        It is important to clarify that these files are expected to be 'countries.csv', 'income gapminder gdp_per_capita_ppp.xlsx'
        which were provided in HomeWork 9, or files with similar structure.

        This function puts the data into a pandas dataframe, transposes it, and prints the head.

- income_distribution receives an integer between 1800 and 2012 which corresponds to an year, and plots the distribution of income
    for that particular year. It uses the load_income function to load data.

- merge_by_year receives a similar integer as income_distribution_hist. It merges the two files and creates a new table as required by
    Homework 9

"""

import pandas as pd
import matplotlib.pyplot as plt


list_valid_years = list()   #Create a list of valid years for the functions
for i in range(1800, 2013):
    list_valid_years.append(i)

class MyError(Exception):  #This class is used to raise errors in the loaderandmerger module
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)


class loader_merger_histogram:

    @staticmethod
    def load_data(file_countries_dict, file_income_data):  #this function loads the countries and income datasets
                                                             # into pandas dataframes, transposes the income dataframe
                                                             # and prints the head of this data
        try:
            countries = pd.read_csv(file_countries_dict)
            income = pd.read_excel(file_income_data, sheetname=0, index_col=0).T
            print income.head()

        except IOError:
            raise IOError("At least one of the files was not found. Please be sure that  'countries.csv' and income 'gapminder gdp_per_capita_ppp.xlsx' are in the parent directory.")
        except TypeError:
            raise TypeError("Error: Make sure that required files are in the directory ")

        return countries, income

    @staticmethod
    def income_distribution_hist(year): #This function displays graphically the distribution of income per person across
                                        # all countries for a given year. I chose to plot it like a histogram
        try:
            if year in list_valid_years:
                _, income_per_capita = loader_merger_histogram.load_data('countries.csv', 'indicator gapminder gdp_per_capita_ppp.xlsx')
                income_per_capita = pd.DataFrame(income_per_capita, index = [year])
                income_per_capita = income_per_capita.T

                plt.close()
                income_per_capita.dropna().hist()
                plt.xlabel("Distribution of Income per capita")
                plt.show()
            else:
                raise MyError("Introduced integer was not between 1800 and 2012 which are the valid years")

        except IOError as e:
            print str(e)
        except TypeError as e:
            print str(e)

    @staticmethod
    def merge_by_year(year):  #This function merges the countries and income data sets for any given year. The result is
                              # a dataframe with three columns: Country, Region and Income.
        try:

            if year in list_valid_years:
                countries, income = loader_merger_histogram.load_data('countries.csv', 'indicator gapminder gdp_per_capita_ppp.xlsx')
                income = income.T
                income['Country'] = income.index
                income.set_index('Country')
                income = income[['Country', year]]
                merged_df = pd.merge(countries, income, how='inner', on='Country')
                merged_df.columns = ['Country', 'Region', 'Income']
                return merged_df
            else:
                raise MyError("Introduced integer was not between 1800 and 2012 which are the valid years")

        except IOError as e:
            print str(e)
        except TypeError as e:
            print str(e)


