from unittest import TestCase
from dataframefunctions import *
from areaincomegraphs import AreaIncomeGraphs
import os

__author__ = 'obr214'


class Test(TestCase):

    def test_open_files(self):
        """
        Passing wrong filenames to load_dataframes function

        Result: It should raise IO exception
        """
        countries_filename = 'wrong_countries_file.csv'
        income_filename = ['wrong_income_file.csv', 'Data']

        with self.assertRaises(IOError):
            load_dataframes(countries_filename, income_filename)

    def test_wrong_format_incomefile(self):
        """
        Passing a wrong income file format (It should include a filename and the name of the Sheet

        Result: It should raise Lookup Error
        """
        countries_filename = 'countries.csv'
        income_filename = ['indicator gapminder gdp_per_capita_ppp.xlsx']

        with self.assertRaises(LookupError):
            load_dataframes(countries_filename, income_filename)

    def test_get_hist_income_per_year_year_is_not_int(self):
        """
        Passing a year that is not an int

        Result: It should raise ValueError
        """
        with self.assertRaises(ValueError):
            countries_filename = 'countries.csv'
            income_filename = ['indicator gapminder gdp_per_capita_ppp.xlsx', 'Data']
            countries, income = load_dataframes(countries_filename, income_filename)
            get_hist_income_per_year(income, 'bad_error')

    def test_merge_by_year_year_is_not_int(self):
        """
        Passing a year that is not an int

        Result: It should raise ValueError
        """
        with self.assertRaises(ValueError):
            countries_filename = 'countries.csv'
            income_filename = ['indicator gapminder gdp_per_capita_ppp.xlsx', 'Data']
            countries, income = load_dataframes(countries_filename, income_filename)
            merge_by_year(income, countries, 'bad_error')

    def test_create_plots_files(self):
        """
        Creates the plots for the 2007 year

        Result: Should create 7 plots
        """
        try:
            os.remove('2007_WORLD_boxplot.pdf')
            os.remove('AFRICA_2007_income_per_person.pdf')
            os.remove('ASIA_2007_income_per_person.pdf')
            os.remove('EUROPE_2007_income_per_person.pdf')
            os.remove('NORTH AMERICA_2007_income_per_person.pdf')
            os.remove('OCEANIA_2007_income_per_person.pdf')
            os.remove('SOUTH AMERICA_2007_income_per_person.pdf')
        except IOError:
            pass

        year = 2007

        countries_filename = 'countries.csv'
        income_filename = ['indicator gapminder gdp_per_capita_ppp.xlsx', 'Data']
        countries, income = load_dataframes(countries_filename, income_filename)

        #Creates the merged file
        countries_merged_df = merge_by_year(income, countries, year)
        #Creates the object
        plotting = AreaIncomeGraphs(year, countries_merged_df)
        plotting.create_plots()

        self.assertTrue(os.path.isfile('2007_WORLD_boxplot.pdf'))
        self.assertTrue(os.path.isfile('AFRICA_2007_income_per_person.pdf'))
        self.assertTrue(os.path.isfile('ASIA_2007_income_per_person.pdf'))
        self.assertTrue(os.path.isfile('EUROPE_2007_income_per_person.pdf'))
        self.assertTrue(os.path.isfile('NORTH AMERICA_2007_income_per_person.pdf'))
        self.assertTrue(os.path.isfile('OCEANIA_2007_income_per_person.pdf'))
        self.assertTrue(os.path.isfile('SOUTH AMERICA_2007_income_per_person.pdf'))

