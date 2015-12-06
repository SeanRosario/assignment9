__author__ = 'ktc312'

import pandas as pd

'''import data'''

countries = pd.read_csv('/Users/Leo/PycharmProjects/assignment/assignment9/countries.csv')
income = pd.read_excel('/Users/Leo/PycharmProjects/assignment/assignment9/indicator gapminder gdp_per_capita_ppp.xlsx').T

def merge_by_year(year):
    # merge the countries and income data sets for any given year.
    left = countries
    right = pd.DataFrame({'Country': income.T['gdp pc test'],'Income': income.T[year]})
    country_income_df = pd.merge(left, right, on = 'Country', how = 'inner')
    return country_income_df