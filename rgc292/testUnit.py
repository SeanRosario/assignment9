'''
Created on Nov 13, 2015

@author: Rafael Garcia (rgc292)
'''
import unittest
import validation as val
import load_data as ld
import pandas as pd

"""This class is intended to check if methods within the program are 
    working properly"""
    
class Test(unittest.TestCase):


    def testName(self):
        pass
    
    
    #Test the validate_input method
    def test_validate_input(self):
        self.valid = val.Validation()
        
        for i in range(1800, 2013):
            self.result = self.valid.validate_input(i)
            self.assert_(self.result == False)
         
         
    #Test the load method    
    def test_load_file(self):
        self.raised = False
        self.load = ld.Load_data()
        self.frame = pd.DataFrame()
        
        try:
            self.frame = self.load.read_csv_file('countries.cs')
            self.frame = self.load.read_xlsx_file('income.xls')
        except IOError:
            self.raised = True
            self.assertFalse(self.raised == False)             

if __name__ == "__main__":
    unittest.main()