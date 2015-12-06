import unittest
from IncomeDataController import *


class idc_test_case(unittest.TestCase):

    def test_idc_create_ok(self):
        '''Test creating an IDC'''
        directory, filename = os.path.split(os.path.realpath(__file__))
        idc = IncomeDataController(os.path.join(directory, 'countries.csv'),
                os.path.join(directory, "indicator gapminder gdp_per_capita_ppp.xlsx"))

    def test_idc_bad_files_raise_exceptions(self):
        '''Bad files should raise exceptions'''
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
        '''Plot some incomes for years'''
        directory, filename = os.path.split(os.path.realpath(__file__))
        idc = IncomeDataController(os.path.join(directory, 'countries.csv'),
                os.path.join(directory, "indicator gapminder gdp_per_capita_ppp.xlsx"))
        idc.plot_income(2000)
        idc.plot_income(1990)

        with self.assertRaises(KeyError):
            idc.plot_income(2200)
