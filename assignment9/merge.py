'''
Created on Nov 23, 2015

@author: Xu Xu
'''
#The function aims to merge and columns of data frame are 'Country', 'Region', and 'Income'

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def merge_by_year(income, countries, year):
   
    new_df = countries.join(income[year], how = 'inner')
    new_df.reset_index(level=0, inplace=True)
    new_df.columns = ['Country', 'Region', 'Income']
    
    
    return new_df
