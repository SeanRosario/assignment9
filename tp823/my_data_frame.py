'''
Created on Nov 16, 2015

@author: Taurean Parker
'''

import pandas as pd


class data_frame:
    'Store a csv file into a Dataframe'
    def __init__(self, data_frame):
            self.data_frame= pd.read_csv(data_frame)
    
    def view(self):
        'Return the contents of the Dataframe'
        data_frame= self.data_frame
        return data_frame
    
    def transpose(self):
        'Return a transpose of the dataframe'
        transpose= self.data_frame.transpose()
        return transpose.head()
   


    