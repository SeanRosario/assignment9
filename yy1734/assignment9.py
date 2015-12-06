# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 

@author: YY
"""

from hw9functions import *
from hw9input import *
import sys

if __name__ == '__main__':
    print 'loading...'

    # load data
    income, countries = data_setup()
    
    print '\n Income Overview:'
    print income.head()
    
    while True:
        
        yr = inputYear()            
        output = analysis(income, countries, yr)
        output.boxplot()
        output.hist()
        print 'Histogram and Boxplot are saved'
        

        
    
    
    
    


