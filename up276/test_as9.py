'''
Created on Nov 24, 2015
@author: Urjit Patel - up276
'''

from unittest import TestCase
import assignment9
import os

__author__ = 'up276'

class Test(TestCase):
    '''
    This Test class has one test which tests whether or not our program generates the necessary files
    It manually performs the test for the year '2010'
    '''

    def test_existance_of_generated_files(self):
        try:
            assignment9.remove_old_directories()  #first remove all files which are already presented
        except IOError:
            pass

        year_str = '2010'
        directory_name = 'Plots_for_year_' + year_str

        #Run the plot_graphs_for_year function
        assignment9.plot_graphs_for_year(year_str)

        #Filenames to check the existance
        filename_1 = directory_name+'/Box_plot_2010.png'
        filename_2 = directory_name+'/Histogram_AFRICA_2010.png'
        filename_3 = directory_name+'/Histogram_ASIA_2010.png'
        filename_4 = directory_name+'/Histogram_EUROPE_2010.png'
        filename_5 = directory_name+'/Histogram_NORTH AMERICA_2010.png'
        filename_6 = directory_name+'/Histogram_OCEANIA_2010.png'
        filename_7 = directory_name+'/Histogram_SOUTH AMERICA_2010.png'

        #it returns true if the file is available
        self.assertTrue(os.path.isfile(filename_1))
        self.assertTrue(os.path.isfile(filename_2))
        self.assertTrue(os.path.isfile(filename_3))
        self.assertTrue(os.path.isfile(filename_4))
        self.assertTrue(os.path.isfile(filename_5))
        self.assertTrue(os.path.isfile(filename_6))
        self.assertTrue(os.path.isfile(filename_7))