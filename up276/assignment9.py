'''
Created on Nov 24, 2015
@author: Urjit Patel - up276
'''

import re
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from regions import Region, Region_Exception
import os, glob, shutil

def main_function():
    '''
    Body of main_function from where all necessary execution of the program starts
    This program keeps asking the user to enter the year and shows the income distribution for the entered year untill user enteres 'finish'
    Then program will generate plots for years [2007,2012] as below,
    This program generates 7 plots for each year,
    1. 6 histograms based on each region
    2. 1 Box plot to compare income distribution across all regions
    Please Note : for the first iteration it may give you some copy warning, but it will not affect the functionality of the program
    '''
    try:

        print "Program to analyze the income per person for any given year !!!"
        print
        print "*****************INSTRUCTIONS*********************"
        print "Please enter only four digit year value in range [1800,2012] as we only have income data for thiese years. In case of other cases appropriate error message will be thrown."
        print "Please enter finish/FINISH/Finish to exit from the program...!!!"
        print "**************************************************"
        quit_flag = False  # to check whether user wants to quit the game or not
        year_value_pattern = '^\d{4}$'  # pattern to compare year value
        year_list = ['2007','2008','2009','2010','2011','2012'] #
        remove_old_directories()
        countries = pd.read_csv('../countries.csv', sep=',')
        income = pd.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx', index_col=0)
        income = income.transpose()
        print
        print "first 2 lines ( with the header ) of the 'income' dataframe is as below,"
        print income.head(n=2)
        print

        while not quit_flag:
            user_input = raw_input("please enter the year in four digits ( or enter 'finish' when you are done with analysis) : ")
            user_input = user_input.strip().replace(' ', '')  # removes all white spaces from user input
            year_value = re.match(year_value_pattern, user_input)  # to match the entered year value with pattern

            if user_input in ('finish', 'FINISH', 'Finish'):
                quit_flag = True
            elif year_value and int(user_input) not in range(1800, 2013):
                print "We dont have the income data for the entered year... Please enter the year in the range [1800,2012]."
            elif year_value:                    #If the entered year is valid then perform all plotting tasks
                year = int(user_input)
                print
                print "------------------------------------------------------------------------------------------------------"
                print
                print "Analysis for the year ", user_input, " started ..."
                print

                print "Plotting and saving graphs for income distribution across all countries ...In Progress..."
                plot_income_distribution(year,income)
                print "Graphs for income distribution across all countries are plotted and saved successfully...Completed !!!"
                print
                print "Analysis for the year ", user_input, " Completed !!!"

            else:
                print "Bad user input... Please enter the year in correct format"

        if quit_flag:
            print "You entered 'finish', so now program will go ahead with the plotting the graphs for years [2007,2012]..."
            for year_str in year_list:  #below for loop will plot graphs for [2007,2012]
                plot_graphs_for_year(year_str)


        else:
            print "Bad user input... Please enter the year ini correct format"

    except KeyboardInterrupt:
        print "Program Interrupted...Plz run the program again !!!"
    except Region_Exception as exception:
        print "Error:", exception
        sys.exit()

def plot_graphs_for_year(year_str):
    '''
    This function will create 7 plots for the input year which includes 1 box plot for that year and 6 hostograms for each region
    '''
    #try:
    countries = pd.read_csv('../countries.csv', sep=',')
    income = pd.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx', index_col=0)
    income = income.transpose()
    list_region_objects = []
    list_of_region_income_data = []
    year = int(year_str)
    directory_name = create_new_directory(year_str)
    print
    print "------------------------------------------------------------------------------------------------------"
    print
    print "Analysis for the year ", year_str, " started ..."
    print
    regions_data = merge_by_year(year, income, countries)
    grouped_region_data = regions_data.groupby('Region')
    region_names = regions_data['Region'].unique()

    #below for loop will create Region type objects for each individual region
    for region_name in region_names:
        region_data = grouped_region_data.get_group(region_name)
        region_object = Region(region_name, region_data)            # Instance creation of Region class
        list_region_objects.append(region_object)

    #creating list of lists having data of each region income for the Box Plot
    for i in range(len(list_region_objects)):
        list_of_region_income_data.append(list_region_objects[i].region_income)


    print "Plotting and saving histograms for each region ...In Progress..."
    for i in range(len(list_region_objects)):
        Region.plot_Hist_Graphs(list_region_objects[i], year_str, directory_name)
    print "Histograms for each region are plotted and saved successfully ...Completed !!!"
    print


    print "Plotting and saving Box Plot ...In Progress..."
    Region.plot_BoxPlots(region_names, list_of_region_income_data, year_str, directory_name)
    print "Box Plt is plotted and saved successfully ...Completed !!!"
    print
    #except KeyboardInterrupt:
    #    print "Program Interrupted...!!!"
    #except:
    #    raise Region_Exception("While plotting the graphs for [2007,2012]")

def plot_income_distribution(year, income_df):
    '''
    This function creats two plots which are,
    1. Histogram for income distribution across all countries over the world
    2. Bar graph to show the GDP for each country individually
    '''
    try:
        df_to_plot = pd.Series.to_frame(income_df.ix[year])
        df_to_plot = df_to_plot.dropna(axis=0)
        df_to_plot = df_to_plot.sort(columns=year, ascending=True)
        df_to_plot.hist(bins=10)
        plt.show()

    except KeyboardInterrupt:
        print "Program Interrupted...!!!"
    except:
        raise Region_Exception("While plotting the income distribution for the year")


def merge_by_year(year, income_df, countries_df):
    '''
    This function merges the 'countries' and 'income' dataframes with respect to year entered by the user
    It returns the group of all region data as a list
    '''
    try:
        regions_data = countries_df
        regions_data.insert(2, 'income', np.nan, allow_duplicates=False)
        for i in range(0, len(regions_data.index)):

            try:
                cn = regions_data['Country'][i]
                incm = income_df[cn].ix[year]
                regions_data['income'][i] = incm
            except KeyError:
                incm = np.nan
                regions_data['income'][i] = incm
        return regions_data
    except KeyboardInterrupt:
        print "Program Interrupted...!!!"
    except:
        raise Region_Exception("While calculating merge_by_year function")


def remove_old_directories():
    '''
    This function removes the old directories generated in past iterations
    '''
    try:
        for path in glob.glob("Plots_*"):
            shutil.rmtree(path)
    except KeyboardInterrupt:
        print "Program Interrupted...!!!"
    except:
        raise Region_Exception("While removing old directories")


def create_new_directory(year_string):
    '''
    This function creates new directory for the entered year to store the result plots
    '''
    try:
        directory_name = 'Plots_for_year_' + year_string
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
        return directory_name
    except KeyboardInterrupt:
        print "Program Interrupted...!!!"
    except:
        raise Region_Exception("While creating new directory")


if __name__ == "__main__":
    try:
        main_function()  # call to main_function()
    except KeyboardInterrupt:
        print "Program Interrupted...Plz run the program again...Thanks!!!"

