import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from datafunc import *
import Input_Test

def program():
	# This main program start with asking for a valid input of year from the user, if
	# the input year is between 1800 to 2012, the first couple of rows of the income data
	# will show on the console and a histogram of the income distribution for the corresponding
	# year will be saved. If 'Finish' or 'finish' is entered, the program will atutomatically 
	# generate histograms and boxplot for years between 2007 to 2012.

	start = True
	while start:
		year_input = raw_input("Please enter a year between 1800 and 2012, or enter 'finish' to end program \n")
		countries = pd.read_csv('countries.csv')
		income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx').T
		print income.head()
		
		if year_input in ['finish', 'Finish']:
			for year in range(2007, 2013, 1):
				income_plot = AnalysisTools(year)
				income_plot.histogram()
				income_plot.box_plot()
			print 'Program ends. Please see saved files for correspondng plots between 2007 - 2012 \n'
			start = False
			return
		elif int(year_input) >= 1800 and int(year_input) <= 2012:
			plt.close('all')
			year = int(year_input)
			print 'A histogram of the income distribution of the year %s is saved. Please check.\n' %(year)
			distribution_of_income_per_capita(year, income)
		else:
			print 'Invalid year'

if __name__ == '__main__':
	try:
		program()
	except ValueError:
			print 'Programs ends due to invalid inputs. Input can only be integer or string "finish"'
	except KeyboardInterrupt:
		print 'Prgram ends due to Keyboard Interruption'
	except EOFError:
		print 'Program ends due to EOFError'










