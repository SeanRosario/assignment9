from functions import *
from tools import *
import pandas as pd
import matplotlib.pyplot as plt
import sys

def main():
    # read in data and print the head of income
    # file path should be modified
    income = read_xlsx("//Users/zhaoyinzhu/Dropbox/NYU/GA 1007 Data Science/python/assignment9/indicator gapminder gdp_per_capita_ppp.xlsx")

    while True:
        input_year = raw_input("Enter a year between 1800 and 2012 \n Enter finish the program will create histograms and boxplots for the years 2007-2012 \n Enter quit to exit\n")

        if input_year == "quit":
            sys.exit()

        elif input_year == "finish":
            break

        else:
            hist_plot(income,int(input_year))

    # Create histograms and boxplots for the years 2007-2012
    for year in range(2007,2013):
        data = tools(year)
        data.plot_hist()
        data.plot_boxplot()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print ("Accidently stopped by keyboard interrupt")
    except ValueError:
        print("Accidently stopped by invalid value")
    except TypeError:
        print("Accidently stopped by invalid types")
