'''
Author: Shixin Li 

This is the main program that first displays graphs for the year that user entered.
After entering finish, the program will then generate and save histograms and
boxplots for the years 2007-2012.
'''

from functions import *
from data_analysis import *
import sys 
import re 

# main function 
def main():

	print showHead()

	# print instructions
	print '\nPlease enter a year between 1800 and 2012 to display a graph'
	print 'for the year you entered.\n'		
	print 'You can keep entering different years to display different graphs.'
	print 'New graph will be displayed once you close the previous one.\n'
	print 'Please enter finish to stop the program.\n'
	print 'After entering finish, the program will generate and save graphs for the years 2007-2012\n'
	print 'Please enter quit to exit the program\n'

	while True:

		input = raw_input()

		if input == 'quit':
			sys.exit()

		elif re.match(r'^[0-9]{4}$', input):
			plotDistribution(int(input))

		elif input == 'finish':
			break

		else:
			print 'Please enter a valid input next time!'
			sys.exit()

	# for loop to generate and save 6 boxplots and 6 histograms
	for year in range(2007, 2013):
		graphs = dataAnalysis(year)
		graphs.plot_boxplots()
		graphs.plot_histograms()

	print 'Plots will be saved'


if __name__ == "__main__":

	try:
		main()
	except EOFError:
		pass
	except TypeError:
		pass
	except ZeroDivisionError:
		pass
	except ArithmeticError, OverflowError:
		pass
	except KeyboardInterrupt, ValueError:
		pass 




