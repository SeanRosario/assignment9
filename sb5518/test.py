__author__ = 'sb5518'

from unittest import TestCase
import loaderandmerger
import plot_income_by_region
from loaderandmerger import MyError as loader_Error
import os

class all_tests(TestCase):

    def test_graphical_explorer(self):
        try:
            os.remove('./histogram_SOUTH AMERICA_2008.png')
            os.remove('./histogram_NORTH AMERICA_2009.png')
            os.remove('./boxplot_NORTH AMERICA_2010.png')
        except OSError:
            pass

        plot_income_by_region.graphical_explorer(2008)
        plot_income_by_region.graphical_explorer(2009)
        plot_income_by_region.graphical_explorer(2010)


        self.assertTrue(os.path.isfile('./histogram_SOUTH AMERICA_2008.png'))
        self.assertTrue(os.path.isfile('./histogram_NORTH AMERICA_2009.png'))
        self.assertTrue(os.path.isfile('./boxplot_NORTH AMERICA_2010.png'))


    def test_load_indicators_IO(self):
        with self.assertRaises(IOError):
            loaderandmerger.loader_merger_histogram.load_data('sdjasd.csv', 'countrieeees.xls')

    def test_load_indicators_TypeE(self):
        with self.assertRaises(TypeError):
            loaderandmerger.loader_merger_histogram.load_data('countries.csv')


    def test_income_distribution_hist_invalid_year(self):
        with self.assertRaises(loader_Error):
            loaderandmerger.loader_merger_histogram.income_distribution_hist(1799)

    def test_income_distribution_hist_string(self):
        with self.assertRaises(loader_Error):
            loaderandmerger.loader_merger_histogram.income_distribution_hist('1799')


    def test_merge_by_year(self):
        with self.assertRaises(loader_Error):
            loaderandmerger.loader_merger_histogram.merge_by_year(1799)
    def test_merge_by_year(self):
        with self.assertRaises(loader_Error):
            loaderandmerger.loader_merger_histogram.merge_by_year('1799')
