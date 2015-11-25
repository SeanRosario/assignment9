'''
Created on Nov 24, 2015

@author: ds-ga-1007
'''
import pandas as pd
import numpy as np
from mergeby_year import *
from data_analysis_tools import *

def main():
    countries=pd.read_csv('countries.csv',sep=',')
    income=pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx',sheetname='Data',index_col=0)
    income_transpose=income.transpose()
    print 'The head of income dataset'
    print income_transpose.head()
    while True:
        year=raw_input('please enter a year from 1800 to 2012: ')
        if year=='finish':
            break
        else:
            year=int(year)
            display_income_by_year(year,income_transpose)   
        
    for year in range(2007,2013):
        merged_income_with_region=merge_by_year(year,countries,income_transpose)
        data_analysis_tool_instance=Data_Analysis_tools(year,merged_income_with_region)
        data_analysis_tool_instance.plot_box()
        data_analysis_tool_instance.plot_hist()

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "KeybordInterrupt"


