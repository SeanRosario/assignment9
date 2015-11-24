"""Author: Akash Shah (ass502)

This module contains the main loop for interacting with the user. 
The user is prompted for an input year, upon which the income distribution
for that year is displayed. This loop is repeated until the user 
types finish. Then, for each year specified in the years array, 
region income distribution is graphically saved to pdf files"""

from helper import *
from explore_year import ExploreYear
import sys
import numpy as np

years = np.arange(2007,2013)

def loop(income,countries):
	"""main loop that interacts with user"""

	yearInput=raw_input("Enter a year: ")

	if yearInput=="finish": #exit loop
		plotGraphs(income,countries)
	else:
		if yearInput.isdigit(): #check if the input is a positive integer
			try:
				plot_income_by_year(income,int(yearInput))
				loop(income,countries)
			except KeyError: #catch error if the year is not in the dataframe
				print "The year must be between 1800 and 2012"
				loop(income,countries)
		else:
			print "The year must be a positive integer"
			loop(income,countries)

def plotGraphs(income,countries):
	"""plots histograms and boxplots for each year in the array years"""

	for year in years:
		try:
			current_year = ExploreYear(income,countries,year)
			current_year.plotRegionHistograms()
			current_year.plotRegionsBoxplot()
		except KeyError: #catch error if the year is not in the dataframe
			pass


if __name__=="__main__":
	try:
		income, countries = load_data()
		loop(income,countries)
	except (KeyboardInterrupt,EOFError):
		sys.exit()



