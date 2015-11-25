'''
Created on Nov 23, 2015

@author: Xu Xu
'''
import unittest
from unittest import TestCase
from merge import *
from plot import *
import pandas as pd


class Test(unittest.TestCase):


    def setUp(self):
        pass
    
    def input_year_1750(self):
        self.assertRaises(KeyError, year = 1700)
        
    def input_year_2017(self):
        self.assertRaises(KeyError, year = 2017)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()