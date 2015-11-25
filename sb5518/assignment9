
__author__ = 'sb5518'

""" This program is meant to provide insights about income per capita distribution for each region in the globe by year.
Data is available from 1800 to 2012.

First, the program will ask user to input a year in that range. Spaces are not allowed, and any input other than a number
in the range 1800-2012 will be considered invalid. In case the input is invalid, the program will ask for input again.

When a valid year is introduced, the program will plot an histrogram to show the distribution of income per capita across the
globe for that particular year.

When the user closes the histogram window, the program will ask for input again, and repeat the process until the user
enters the work "finish"

After that, the program will plot histograms and boxplots to show income per capita and save them in individual files.
The charts will be plotted by region and by year.

Please make sure that the files 'countries.csv' and 'indicator gapminder gdp_per_capita_ppp.xlsx' are in the same directory as this program """

import loaderandmerger
import plot_income_by_region
from loaderandmerger import MyError as loader_Error


list_of_valid_years = list() #generate a list of valid strings that represent the available data.
for i in range(1800, 2013):
    list_of_valid_years.append(str(i))

is_input_correct = False

while is_input_correct == False:    #Loop until we get a valid input year

    try:
        user_input = raw_input("Please enter a year from 1800 to 2012. No spaces are allowed ")

        if user_input in list_of_valid_years:
                is_input_correct = True
                year = int(user_input)
                loaderandmerger.loader_merger_histogram.income_distribution_hist(year)
        else:
                print "Please enter a valid year from 1800 to 2012"

    except (KeyboardInterrupt, EOFError): #avoid interrupting the program
        continue
    except loader_Error as e:
        print str(e)

user_input_2 = "hey"

while user_input_2 <> "finish":  #Loop until user inputs 'finish'

    try:
        user_input_2 = raw_input('Please enter another year from 1800 to 2012.  '
                                 'If you do not want to enter more years, please write "finish". '
                                 'No spaces are allowed.')

        if user_input_2 in  list_of_valid_years:
            year = int(user_input_2)
            loaderandmerger.loader_merger_histogram.income_distribution_hist(year)

        elif ((user_input_2 not in list_of_valid_years) and (user_input_2!="finish")):
            print "Please enter a valid year from 1800 to 2012"

    except (KeyboardInterrupt, EOFError): #avoid interrupting the program
        continue
    except loader_Error as e:
            print str(e)


for year in range(2007, 2013):   #plot histograms and boxplots from years 2007-2012
    try:
        plot_income_by_region.graphical_explorer(year)
    except loader_Error as e:
        print str(e)