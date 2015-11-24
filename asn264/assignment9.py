'''
Author: Aditi Nair
Date: November 12 2015

Description: This is the main module from which the program is run. 
It loads the required data frames as necessary, formats them appropriately, 
and then allows the user to enter a year in order to display a histogram of
the income distribution. Once the user types "finish", it generates histograms
and boxplots of the income distribution by region for the years 2007-2012 into pdf files.
'''

from regionalGDP import *
import sys


def main():

	try:

		print "Loading data..."

		#Perform all necessary data processing and load into dataframes. Print as required.
		tCountries, tIncome = load_session()

		print "Income DataFrame looks like:\n", tIncome.head()

		#Until the user enters 'finish', asks for a year and displays a histogram using inc_by_year.
		get_display(tIncome)

		#Then use the regionalGDP class to generate graphs for the years 2007-2012
		for year in range(2007,2013):
			try:
				print "Generating graphs for the year", str(year), "..."
				yearly_data = regionalGDP(tCountries, tIncome, year)
				yearly_data.plot_hist()
				yearly_data.plot_boxplot()
		
			#Just in case some of the years are not in the income df. 
			except InvalidDistributionRequest:
				pass

	except (KeyboardInterrupt, EOFError):
		sys.exit()


def prompt():

	return raw_input("Please enter a year.")


def get_display(income):

	#Asks the user to enter a year. 
	input = prompt()

	#If the user enters "finish", do nothing. 
	if input.strip().lower() == "finish":
		pass

	else:
		#inc_by_year prints "Invalid input." if input is not in the year column of the income df. 
		#Otherwise, displays a histogram. 
		try:
			income_by_year(income, int(input))
		except ValueError:
			print "Invalid input."
		return get_display(income)


#Run the program
if __name__ == "__main__":
	main()