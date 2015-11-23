"""This is the main body of the program for Assignment 9.  This program
loads data from files in parent directories into pandas dataframes,
manipulates them, and then visualizes them for the user by year and for
a range of years."""

#author: Matthew Dunn
#netID: mtd368
#date: 11/22/2015

import traceback
import re
import sys
import numpy as np
import pandas as pd
import dataloader
from dataloader import dataimporter, datatransformer, datasorter, datamerger
import visualizer
from visualizer import visualizationtool, histogrambuilder


if __name__ == '__main__':
    try:
        income, countries = dataimporter()
        transformedincome = datatransformer(income)
        print transformedincome.head()
        while True:
            print 'Input a year between 1800 and 2012 or enter finish to conclude the program and generat plots from 2007 to 2013.\n'
            print 'If you wish to end the program and not generate plots, enter quit.\n'
            year = raw_input('Please enter a year in the format YYYY to explore the Per Capita GDP across regions of the world\n')
            if year == 'finish':
                break
            elif year == 'quit':
                sys.exit()
            elif re.match(r'^[0-9]{4}$', year):
                year = int(year)
                try:
                    if year >= 1800 and year <= 2012:
                        sortedtlistForGivenYear = datasorter(transformedincome, year)
                        histogrambuilder(sortedtlistForGivenYear, year)
                except KeyError:
                    print '\n Invalid Year'
            else:
                print "\n Invalid Year."
        yearsToGeneratePlots = [2007,2008,2009,2010,2011,2012]
        for i in yearsToGeneratePlots:
            yearlyplot = visualizationtool(i)
            mergeddata = datamerger(transformedincome, countries, i)
            yearlyplot.regionshistogram(mergeddata)
            yearlyplot.boxploter(mergeddata)
        print "\n Plots have been saved. "
    except KeyboardInterrupt, ValueError:
        print "\n Interrupted!"
    except EOFError:
        print "\n Interrupted!"
    except ZeroDivisionError:
        print "\n Math Error"
    except TypeError:
        print "\n Type Wrong!"
    except OverflowError:
        print "\n OverflowError!"
