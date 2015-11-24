import unittest
# Don't show figures for testing
# From: http://stackoverflow.com/questions/19812818/how-to-test-that-matplotlibs-show-shows-a-figure-without-actually-showing-it
import matplotlib
matplotlib.use('Template')

from IncomeDataController import *


class idc_test_case(unittest.TestCase):

    def test_idc_create_ok(self):
        idc = IncomeDataController('countries.csv', "indicator gapminder gdp_per_capita_ppp.xlsx")

    def test_idc_bad_files_raise_exceptions(self):
        # Bad countries file
        with self.assertRaises(DataImportError):
            idc = IncomeDataController("indicator gapminder gdp_per_capita_ppp.xlsx", "indicator gapminder gdp_per_capita_ppp.xlsx")

        # Bad income file
        with self.assertRaises(DataImportError):
            idc = IncomeDataController('countries.csv', 'countries.csv')

        # Bad file name
        with self.assertRaises(DataImportError):
            idc = IncomeDataController('countries.csv', "indicatorgapminder gdp_per_capita_ppp.xlsx")

    def test_plot_income(self):
        idc = IncomeDataController('countries.csv', "indicator gapminder gdp_per_capita_ppp.xlsx")
        idc.plot_income(2000)
        idc.plot_income(1990)

        with self.assertRaises(KeyError):
            idc.plot_income(2200)
