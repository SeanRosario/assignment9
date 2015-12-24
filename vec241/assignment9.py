'''
This program enables to display various graphs based on data representing the average income per country / region,
in the year chosen by the user.
'''

import pandas as pd
import functions
#%matplotlib

__author__ = 'vec241'

# Loads the required data and sets the data frame into the right format
countries = pd.read_csv("../data/countries.csv")
income = pd.read_excel("../data/indicator gapminder gdp_per_capita_ppp.xlsx")
income_transpose = functions.transformDataframe(income)


# User interaction code
try:

    #Keeps asking the user for a year until the string 'finish' is entered
    continue_flag = True
    while continue_flag:
        year = raw_input('Year ? (enter "finish" to quit) : ')

        if year == 'finish':
            continue_flag = False

        elif type(year) != 'int':
            print "Please provide a valid year in range [1800, 2012]"

        elif int(year) in range(1800, 2013, 1):
            year = int(year)
            functions.plotIncomeDistribution(income_transpose, year)

        else:
            print "Please provide a valid year in range [1800, 2012]"

except ValueError:
    print "This is not a valid year"

#Code for generating boxplots for question 8
'''
for year in range(2007, 2013, 1):
    functions.boxPlotPerRegion(year, income, countries)
'''
