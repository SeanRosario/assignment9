import pandas as pd
import numpy as np
import xlrd

class DataImportError(Exception):
    '''Raised when data cannot be imported correctly'''
    pass

class IncomeDataController(object):
    '''Load and visualize income data'''

    def __init__(self, country_data, income_datafile):
        '''Constructor'''
        try:
            self.countries = pd.read_csv(country_datafile)
            self.income = pd.read_excel(income_datafile, index_col=0).T
        except IOError, xlrd.XLRDError:
            raise DataImportError("Could not read datafiles")

    
