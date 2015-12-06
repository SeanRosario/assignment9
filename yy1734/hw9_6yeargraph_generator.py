# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 11:44:02 2015

@author: YY
"""

#generate graphs for the years 2007-2012.

from hw9functions import *
from hw9input import *
import sys

def six_year_graph_generator():
    income, countries = data_setup()
   
    for yr in range(2007,2013):   
        print str(yr)        
        output = analysis(income, countries, yr)
        output.boxplot()
        output.hist()
        
six_year_graph_generator()

