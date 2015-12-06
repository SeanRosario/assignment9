import sys
import numpy as np 
import pandas as pd 
from pandas import Series, DataFrame
import load_csv
from user_exceptions import invalid_input, invalid_year 
from visual_analysis import data_visulization

'''
The program:
1. load the data and show the head of the dataframe.
2. User's input to generate plots for Question 4.
3. save the defaulted histograms and boxplots for year 2007-2012.
$$ changes can easily been done to have user's input to generate certain histograms and boxplots for a certain year.
'''

def main():
	
	Countries = pd.read_csv('countries.csv')
	income = pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx', index_col='gdp pc test').T
	print Countries.head()	 #show the head of this data set when it is loaded
	print income.head()
	

	try:
		while True:
			print 'Enter quit or q to exit the program.'
			year = raw_input('Input the year you want to explore:(input next or n to skip this step!)\n')
			if str.lower(year) == 'quit' or str.lower(year) == 'q':   #enter quit or q to exit the program
				sys.exit()
			elif str.lower(year) == 'next' or str.lower(year) == 'n':   #enter next or n to skip this step
				break
			try:
				load_csv.display_distribution(year, income)
			except invalid_input:
				print 'invalid input!'
			except invalid_year:
				print 'year out of range[1800, 2012]'
			is_continue = raw_input('Do you want to enter another year? Enter ''finish'' to stop, otherwise continue:\n')
			if str.lower(is_continue) == 'finish':
				break
			elif str.lower(is_continue) == 'quit' or str.lower(is_continue) == 'q':
				sys.exit()

		# generate the defaulted plots
		print 'Now histograms and boxplots of year 2007-2012 will be generated and saved individually and we will exit the program, bye!'
		for year in range(2007, 2013):
			data_analysis = data_visulization(year, load_csv.merge_by_year(income, Countries, year))
			data_analysis.data_histograms()
			data_analysis.data_boxplots()


	except KeyboardInterrupt:
		print 'Terminate abnormally'

if __name__ == '__main__':
	try:
		main()
	except EOFError:
		pass
