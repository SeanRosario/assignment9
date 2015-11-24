# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 10:45:26 2015

@author: YY
"""

import unittest
from unittest import TestCase
from hw9functions import *
from hw9input import *

class CommandTest(TestCase):

    def test_input_year(self):
        self.assertEqual(yearValidation('1999'),1999)
        
    def test_merge_by_year(self):
        income, countries = data_setup()
        self.assertGreater(merge_by_year(income,countries, 1999).size, 1)
        

if __name__ == '__main__':
    unittest.main()