'''
Created on Nov 13, 2015

@author: Rafael Garcia (rgc292)
'''

import pandas as pd
import numpy as np

'''This class is intended to read .xlsx and .csv files'''

class Load_data(object):

    def __init__(self):
        pass
    
    
    #Reads .csv file into a pandas data frame
    def read_csv_file(self, file):
        self.frame = pd.DataFrame()
        
        try:
            self.frame = pd.read_csv(file)
            
        except IOError:
            print '.csv file not available!'
            
        return self.frame
     
    
    #Reads .xlsx file into a pandas data frame    
    def read_xlsx_file(self, file):
        self.frame = pd.DataFrame()
        
        try:
            self.frame = pd.read_excel(file)
            
        except IOError:
            print '.xlsx file not available!'
            
        return self.frame
    
    
    
        