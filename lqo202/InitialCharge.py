"""
This script charges the files into Python and creates some functions that will be useful as a static methods
The files have to be in the same folder
"""

__author__ = 'lqo202'


import pandas as pd
class UtilsFunctions:

    @staticmethod
    def getDataIncome(file = 'indicator gapminder gdp_per_capita_ppp.xlsx'):
        try:
            income = pd.read_excel(file, 'Data', index_col='gdp pc test').transpose()
            return  income
        except IOError:
            raise IOError('No archive Income found!')

    @staticmethod
    def getDataCountries(file = "countries.csv"):
        try:
            countries=pd.read_csv(file, index_col='Country')
            return countries
        except IOError:
            raise IOError("No archive Countries found!")

    @staticmethod
    def plotDistributionIncomePerson(year):
        '''
        In order to plot the histogram, the function locates the data from the given year, drops rows with missing values
        and trnasposes. With that database, the histogram is shown
        :param year: integer to be inputted
        :return: theplot of the distribution in an histogram
        '''
        income = UtilsFunctions.getDataIncome()

        #Localizing the year and dropping rows with NaN values
        dataToPlot=pd.DataFrame(income.loc[[year]]).transpose().dropna()
        #Plotting the histogram
        histogramYear = dataToPlot.hist()
        return histogramYear

    @staticmethod
    def merge_by_year(year):
        """
        First it locates the data from the given year in the income dataset and transposes it. Then it generates indexes
        and column names, in order to make the join easier with the countries dataframe. Finally does the join, adds the country column
        and creates the index as the range of its length.
        :param year: integer to the the input parameter
        :return: a pandas dataframe with merged data of income and countries databases (columns: Region, Country, Income)
        """
        income = UtilsFunctions.getDataIncome()
        countries =  UtilsFunctions.getDataCountries()

        #Selecting the year
        dataSelectedYear = pd.DataFrame(income.loc[[year]]).transpose()
        #Setting the index to join by them (index name Country)
        dataSelectedYear.index.names=['Country']
        dataSelectedYear.columns=['Income']
        mergedData= countries.join(dataSelectedYear)
        #Creating the column Countries and setting a new index
        mergedData['Country'] = mergedData.index
        mergedData.index = range(len(mergedData))
        return mergedData

