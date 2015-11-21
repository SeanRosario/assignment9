# assignment9.py
# Author: Brian Karfunkel
# Date: 11/24/2015
#
# This program loads and visualizes GDP per capita data from countries
# for years requested by the user.
#
import pandas as pd
import numpy as np

countries = pd.read_csv('countries.csv')
income = pd.read_excel("indicator gapminder gdp_per_capita_ppp.xlsx", index_col=0).T


def main:
    '''The main function'''
    # Load data
    # handle input
    # explore


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "Quitting..."
        exit()
