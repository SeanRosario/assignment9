# assignment9.py
# Author: Brian Karfunkel
# Date: 11/24/2015
#
# This program loads and visualizes GDP per capita data from countries
# for years requested by the user.
#
import pandas as pd
import numpy as np
from IncomeDataController import IncomeDataController
import os

#countries = pd.read_csv('countries.csv')
#income = pd.read_excel("indicator gapminder gdp_per_capita_ppp.xlsx", index_col=0).T

class UserTerminationException(Exception):
    '''Exception to raise if user asks for termination'''
    pass

TERMINATION_STRING = "finish"

def validate_year(yearstr):
    '''Test if input year string is a valid year. Raise UserTerminationException
    if user entered termination string.'''
    if str(yearstr).upper()==TERMINATION_STRING.upper():
        raise UserTerminationException()
    else:
        return int(yearstr)

def ask_for_year():
    '''Ask user to input a year, validate the input, and return it'''
    year = raw_input("Year: ")
    return validate_year(year)


def main():
    '''The main function'''

    directory, filename = os.path.split(os.path.realpath(__file__))
    print "Current directory", directory
    idc = IncomeDataController(os.path.join(directory, 'countries.csv'),
                os.path.join(directory, "indicator gapminder gdp_per_capita_ppp.xlsx"))

    # Main program loop
    while True:
        try:
            year = ask_for_year()
            data = idc.merge_by_year(year)
            idc.plot_income(year)
        except UserTerminationException:
            # If user type the termination string, break out of loop
            break
        except (ValueError, EOFError):
            print "Invalid year entered. To end, type 'finish'."
            continue
        except KeyError as e: # Year entered is valid, but not in the income data
            print "Year %d is not in data. Please try another year." % e.message
            continue

    # Now that user has finished, and we've broken out of the loop,
    # generate graphs for the years 2007-2012
    years = range(2007, 2013)
    idc.plot_years(years)

    return idc


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "Quitting..."
        exit()
