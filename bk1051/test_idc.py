import unittest
# Don't show figures for testing
# From: http://stackoverflow.com/questions/19812818/how-to-test-that-matplotlibs-show-shows-a-figure-without-actually-showing-it
import matplotlib
matplotlib.use('Template')

from IncomeDataController import *


class idc_test_case(unittest.TestCase):

    def test_idc_create_ok(self):
        directory, filename = os.path.split(os.path.realpath(__file__))
        idc = IncomeDataController(os.path.join(directory, 'countries.csv'),
                os.path.join(directory, "indicator gapminder gdp_per_capita_ppp.xlsx"))

    def test_idc_bad_files_raise_exceptions(self):
        directory, filename = os.path.split(os.path.realpath(__file__))
        # Bad countries file
        with self.assertRaises(DataImportError):
            self.idc = IncomeDataController(os.path.join(directory, "indicator gapminder gdp_per_capita_ppp.xlsx"),
                    os.path.join(directory, "indicator gapminder gdp_per_capita_ppp.xlsx"))

        # Bad income file
        with self.assertRaises(DataImportError):
            idc = IncomeDataController(os.path.join(directory, 'countries.csv'),
                                os.path.join(directory, 'countries.csv'))

        # Bad file name
        with self.assertRaises(DataImportError):
            idc = IncomeDataController(os.path.join(directory, 'countries.csv'),
                    os.path.join(directory, "indicatorgapminder gdp_per_capita_ppp.xlsx"))

    def test_plot_income(self):
        directory, filename = os.path.split(os.path.realpath(__file__))
        idc = IncomeDataController(os.path.join(directory, 'countries.csv'),
                os.path.join(directory, "indicator gapminder gdp_per_capita_ppp.xlsx"))
        idc.plot_income(2000)
        idc.plot_income(1990)

        with self.assertRaises(KeyError):
            idc.plot_income(2200)
