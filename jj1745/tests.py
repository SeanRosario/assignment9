'''
Created on Nov 24, 2015

@author: jj1745
'''

import unittest
from yearly_plots import checkYear

class Test(unittest.TestCase):
    '''
    test functions that help handle user inputs in this assignment.
    specifically, the function checkYear yearly_plots.py
    '''

    def testCheckYear(self):
        
        self.assertTrue(checkYear('1800'))
        
        self.assertTrue(checkYear('2000'))
        
        self.assertFalse(checkYear('2014'))
        
        self.assertFalse(checkYear('abcd'))
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()