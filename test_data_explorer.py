import unittest
# Don't show figures for testing
# From: http://stackoverflow.com/questions/19812818/how-to-test-that-matplotlibs-show-shows-a-figure-without-actually-showing-it
import matplotlib
#matplotlib.use('Template')

from IncomeDataController import *
from DataExplorer import *

class data_explorer_test_case(unittest.TestCase):

    def setUp(self):
        self.idc = IncomeDataController('countries.csv', "indicator gapminder gdp_per_capita_ppp.xlsx")

    def test_plots(self):
        data = self.idc.merge_by_year(2000)
        de = DataExplorer(data)
        de.plot()
