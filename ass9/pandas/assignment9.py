'''
Created on Nov 24, 2015

@author: ds-ga-1007
'''
import pandas as pd
import numpy as np
from income_dist_per_person import *
from exploratory_data_analysis_tool import *
countries=pd.read_cvs('countries.csv')
income=pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx')
income_transpose=income.transpose()
print income_transpose.head()
year=raw_input('Please Enter a year from 1800 to 2012 to check the income distribution:')
if year=='finish':
    break
else:
    year=int(year)
    if year in income.transpose.index:
        display_income_per_person(year,income_transpose)
        
print 'generating graphs for the year 2007-2012'
for year in range(2007,2013):
    merged_data=merge_by_year(year,countries,income_transpose)
    instance=Data_Analysis_Tools(year,merged_data)
    instance.plot_box()
    instance.plot_histogram()
    















