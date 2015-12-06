import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Author: Kaiwen Liu
 # Q5.
 #This function will merge and create a new dataframe with columns 'Country','region', and 'income' 

def merge_by_year(income, countries, year):
    
    new_df = countries.join(income[year], how='inner') # countries joins
    new_df.reset_index(level=0, inplace=True)
    new_df.columns = ['Country', 'Region', 'Income'] # columns
    return new_df
