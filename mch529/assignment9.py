'''
Input is taken from the user  in the form of a year between 1800 and 2012.  A histogram is then made for that year.  At the end a series of graphs are made from the years between 2007 and 2012
'''
#author: Michael Higgins , collaborated with Nora Barry
#netid: mch529

import pandas as pd
from pandas import ExcelFile
from pandas import DataFrame
import matplotlib.pyplot as plt2
import numpy as np
from exploreData import *
from dataLoad import *
import sys


def takeInput():
	''' 
	valid input is a year between 1800 and 2010 or "finish"
	Will keep on prompting user to enter a year until they "finish"
	Then will save box and whiskers and histogram plots for years 2007-2012
	'''
	print "Enter a year between 1800 and 2012 in the form XXXX."
	print "Type finish to quit"
	inputYear=raw_input("Pick a year:  ")
	if inputYear == ('finish' or "exit"):
		makeGraphs =raw_input( "Do you want to generate graphs from 2007-20012?  ")
		if makeGraphs == "y" or makeGraphs == "yes" or makeGraphs == "Y" :
			generateGraphs()
		print "Done!"
		sys.exit()
	if isValidInteger(inputYear):

		x=Explore(int(inputYear))
		x.graphByYearForAllCountries()		

		takeInput()
	else:
		print "Not a valid Year, must be between 1800 and 2012!"
		takeInput()
		

def isValidInteger(yr):
		try:
			int(yr)

		except ValueError:
			return False	
		
		if int(yr) < 1800 or int(yr)>2012:
			return False
		else:
			return True

def generateGraphs():
	print "Generating graphs for 2007 to 2012..."
	for i in range(2007,2013):
		x=Explore(i)
		x.graphBoxPlotByYearAndRegion()
		x.generate_hist()
	


if __name__ == '__main__':
	try:
		takeInput()
	except KeyboardInterrupt:
		print "Interupted Command Entered."
	except ValueError:
		print "Value Error"
	except ZeroDivisionError:
		print "Math Error"
	except TypeError:
		print "Type Error"
 

