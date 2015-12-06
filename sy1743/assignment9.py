import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import re
from hw9_functions import import_csv, import_and_transform, plot_income_by_yr, merge_by_year
import visualize_tool as vs

# DS-GA 1007
# HW9
# Author: Sida Ye
"""
This is the main program. Users have three options of input. 
First is to enter a year between 1800 and 2012. It will return a histogram about income by year 
Second is to enter 'finish'. It will generate boxplots and histograms from 2007-2012
Thrid, user can enter 'quit' tp exit this program.
"""

def main():
# Q7
	import_and_transform('../indicator gapminder gdp_per_capita_ppp.xlsx')
	try:
		while True:
			print '\n You have three options'
			print '\n 1. Please input a year between 1800 and 2012 to generate plots'
			print '\n 2. Please enter finish to exit plotting and generate graphs for the years 2007-2012'
			print '\n 3. Please enter quit to exit this program\n'
			x = raw_input()
			if x == 'finish':
				break

			elif x == 'quit':
				sys.exit()

			elif re.match(r"^[0-9]{4}$", x):
				try:
					plot_income_by_yr(int(x))
				except KeyError:
					print '\n Input Error: Invalid Year!\n'

			else:
				print "\n Input Error: Please a valid year!\n"

	# Q8
		print '\n Generating plots......'
		yr_list = range(2007, 2013)
		for yr in yr_list:
			result = vs.visualize_tool(yr)	# use visulize tool class to generate plot
			result.plot_boxplot()
			result.plot_hist()
		print '\n Plots are saved at current dictionary'

	except KeyboardInterrupt, ValueError:
		print "\n Interrupted!"
	except ArithmeticError, OverflowError:
		print "\n Math Error"
	except ZeroDivisionError:
		print "\n Math Error"
	except TypeError:
		print "\n Type Wrong!"
	except EOFError:
		print "\n Interrupted!"

	
# Q9



if __name__ == '__main__':
	main()




