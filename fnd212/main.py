#Author: fnd212

# The program asks the user for a year and shows an histogram of the 
# of the number of countries in a certain GDP range.
# After that it saves the exploratory plots generated by DataExploration.save_boxplots
# and save_histogram to ./figures


import sys
import defined_exceptions
import utils
from utils import merge_by_year, year_gdp_histogram,load_dataframes
import data_exploration
from data_exploration import DataExploration



def get_year_from_user():

	try:
		year = raw_input('Please enter a year to explore: ')
	except EOFError:
		raise defined_exceptions.InvalidUserInput()





if __name__ == '__main__':

	year_min = min(DataExploration.income.index)
	year_max = max(DataExploration.income.index)

	try:

		while 1:

			try:
				year = raw_input('Please enter a year to explore (finish to end): ')
			except EOFError:
				#Go to the top of thw while
				print('Invalid input, please try again')
				continue

			if year == 'finish':
				break

			try:
				year = int(year)
			except ValueError:
				# Year is not a string representation of an int
				print('\nInvalid input, please try again')
				continue

			try:
				year_gdp_histogram(DataExploration.income, year)
			except ValueError:
				print('Invalid year, please try again with an year between {} and {}'.format(year_min,year_max))
				continue


		years = range(2007,2013)
		for year in years:
			DataExploration(year).save_boxplots()
			DataExploration(year).save_histogram()



	except (defined_exceptions.FatalError), exception:
		print(exception.message)
		print('Error encountered: Program will exit now')
		sys.exit(1)