### Laura Buchanan ###
###     lcb402     ###

import explore
import pandas as pd
import numpy as np
import re

if __name__ == '__main__':
	try:

while True:
	year = raw_input('What year would you like to explore? Enter a year between 1800 and 2012: ')
        try:
		if year == 'finish':
                	break
			#print info from years 2007-2012
        	elif re.match(r'^[0-9]{4}$', year): ###
                	year = int(year)
			if year >= 1800 and year <= 2012:
				# plot graphs for given year 
				my_data = explore_gdp_data(year)
				display_data(my_data)	 
	except IOError:
		print "IOError"
	else: 
		print "Invalid input: choose a year between 1800 and 2012 or type finish"
             



#plotter = explore_gdp_data('countries.csv','indicator gapminder gdp_per_capita_ppp/Data-Table 1.csv',2000)
#plot = plotter.plot1
