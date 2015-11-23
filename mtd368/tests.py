# test case

"""This runs tests on the program to confirm intended functionality is occur."""

#author: Matthew Dunn
#netID: mtd368
#date: 11/23/2015

import os
import unittest
from unittest import TestCase
import dataloader
from dataloader import dataimporter, datatransformer, datamerger

"""test function in positionsimulator.py"""

class dailypositionanalyzer(unittest.TestCase):

    def setUp(self):
        pass

    # testing the data loading and manipulation functions

    def test_dataloader(self):
        returncount = dataimporter()                    #test the dataimporter
        self.assertEquals(len(returncount),2)           #confirming the returned array is the correct shape

    def test_datatransformer(self):                     #test the data tranformer to confirm the shape is correct
        income, countries = dataimporter()
        transformedvalues = datatransformer(income)
        self.assertEquals(transformedvalues.shape,(213, 230))

    def test_datamerger(self):                          #test the merger function to ensure the correct column headers are created
        income, countries = dataimporter()
        transformedvalues = datatransformer(income)
        year = 2000
        mergeddata = datamerger(transformedvalues, countries, year)
        mergedcolumnheaders = list(mergeddata.columns.values)
        self.assertEquals(mergedcolumnheaders,['Country', 'Region', 'Income'])

if __name__ == '__main__':
    unittest.main()
