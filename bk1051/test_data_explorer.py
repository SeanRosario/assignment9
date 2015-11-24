import unittest
# Don't show figures for testing
# From: http://stackoverflow.com/questions/19812818/how-to-test-that-matplotlibs-show-shows-a-figure-without-actually-showing-it
import matplotlib
#matplotlib.use('Template')

from IncomeDataController import *
from DataExplorer import *
import os

class data_explorer_test_case(unittest.TestCase):

    def setUp(self):
        directory, filename = os.path.split(os.path.realpath(__file__))
        self.idc = IncomeDataController(os.path.join(directory, 'countries.csv'),
                os.path.join(directory, "indicator gapminder gdp_per_capita_ppp.xlsx"))

    def test_plots(self):
        data = self.idc.merge_by_year(2000)
        de = DataExplorer(data)
        hist_fig, box_fig = de.plot()
        hist_fig.show()
        box_fig.show()

    def test_hist(self):
        data = self.idc.merge_by_year(2000)
        de = DataExplorer(data, year=2000, by="Region")
        de.income_histogram()

    def test_hist_noby(self):
        data = self.idc.merge_by_year(2000)
        de = DataExplorer(data, year=2000, by=None)
        de.income_histogram()
