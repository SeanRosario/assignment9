import unittest
from IncomeDataController import *
from DataExplorer import *
import os

class data_explorer_test_case(unittest.TestCase):

    def setUp(self):
        '''Set up an IDC to use throughout test case.'''
        directory, filename = os.path.split(os.path.realpath(__file__))
        self.idc = IncomeDataController(os.path.join(directory, 'countries.csv'),
                os.path.join(directory, "indicator gapminder gdp_per_capita_ppp.xlsx"))

    def test_plots(self):
        '''Test that plots are correct'''
        data = self.idc.merge_by_year(2000)
        de = DataExplorer(data)
        hist_fig, box_fig = de.plot()
        hist_fig.show()
        box_fig.show()

    def test_hist(self):
        '''Test histogram with by variable'''
        data = self.idc.merge_by_year(2000)
        de = DataExplorer(data, year=2000, by="Region")
        de.income_histogram()

    def test_hist_noby(self):
        '''Test histogram without by variable'''
        data = self.idc.merge_by_year(2000)
        de = DataExplorer(data, year=2000, by=None)
        de.income_histogram()
