'''
Created on Nov 17, 2015

@author: ams889

This program tests the functionality of my assignment 9 modules
'''
import unittest
import random
from functions import *
from dataAnalysisClass import *

class Test(unittest.TestCase):
    #testing class for the two main components of this assignments
    
    def testingClass(self):
        #Testing valid inputs for dataAnalysisClass
        year = random.randint(1800,2013)
        self.assertIsInstance(dataAnalysisClass(year),dataAnalysisClass)
        #Testing invalid inputs
        self.assertRaises(ValueError, dataAnalysisClass, "This isn't a number")
        
    def testingMerge(self):
        #Testing that the merge function creates a dataframe
        year = random.randint(1800,2013)
        self.assertIsInstance(merge_by_year(year),pd.DataFrame)
    
if __name__ == "__main__":
    unittest.main()