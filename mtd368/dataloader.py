"""This is the class that visualizes """

#author: Matthew Dunn
#netID: mtd368
#date: 11/22/2015

import os
import numpy as np
import pandas as pd

def dataimporter():
    yourpath = os.getcwd()
    countriesfilename = os.path.join(os.path.dirname(__file__), os.pardir, 'countries.csv')
    countries = pd.read_csv(countriesfilename)
    gdpfilename = os.path.join(os.path.dirname(__file__), os.pardir, 'indicator gapminder gdp_per_capita_ppp.xlsx')
    income = pd.read_excel(gdpfilename)
    return income, countries

def datatransformer(income):
    income.set_index(['gdp pc test'],inplace=True)
    incometransposed = income.transpose()
    incometransposed.dropna(axis=1, how='all', inplace=True) #drop all columns that are completely NaN
    incometransposed.index.name = 'Year'
    return incometransposed

def datamerger(transformedincome, countries, year):
    oneyeargdps = transformedincome.ix[year]
    oneyeargdps = oneyeargdps.dropna()
    oneyeargdps = pd.DataFrame(oneyeargdps)
    oneyeargdps = oneyeargdps.reset_index()
    oneyeargdps.columns = ['Country','Region']
    merged = pd.merge(countries, oneyeargdps, how='left', on=['Country','Country'])
    merged.columns = ['Country','Region','Income']
    sortedlist2 = merged
    sortedlist2 = sortedlist2.dropna()
    sortedlist2 = sortedlist2.sort_values('Income')
    return sortedlist2

def datasorter(transformedincome, year):
    oneyeargdps = transformedincome.ix[year]
    oneyeargdps = oneyeargdps.dropna()
    sortedlist = oneyeargdps.sort_values(ascending=True)
    return sortedlist
