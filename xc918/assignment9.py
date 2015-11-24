#Author: Xing Cui
#NetID: xc918
#Data: 11/16


import pandas as pd
import numpy as np
import matplotlib as plot
import sys
import re
from assignment9_function import *
import visualization as v


"""mail program fro assignment9."""
#Question7
def main():
	try:
		while True:
			print '\n Please follow the instruction.'
			print '\n Please enter a year between 1800 and 2012 to plot or you can enter \'quit\' to exit the program..'

			var1 = raw_input()
			if var1 == re.search(r'^[0-9]{4}', var1).group():
				try:
					data_in_given_year(int(var1)).annual_income()
				except KeyError:
					print 'Invalid input of selecting a year between 1800 and 2012.'

			elif var1 == 'quit':
				sys.exit()
			

			print '\n You can enter \'next\' to stop to get specific plots for 2007 to 2012, or you can enter \'quit\' to exit the program.'
			var1 = raw_input()
			
			
			if var1 == 'next':
				break
		year_list = range(2007,2013)#Question8

		for year in year_list:
			output = v.visualization(year)
			output.histogram_plotting()
			output.boxplot_plotting()

		print '\n Figures have saved at current directory.'
	except KeyboardInterrupt:
		print 'Oops, interruption.'
	except TypeError:
		print 'Oops, invalid type.'
	except ValueError:
		print 'Oops, invalid value.'
	except KeyError:
		print 'Opps, invalid year.'







if __name__ == '__main__':
	main()