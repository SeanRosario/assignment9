'''
Author: Aditi Nair
Date: November 12 2015
Resources: 
- http://stackoverflow.com/questions/6986986/bin-size-in-matplotlib-histogram
- http://stackoverflow.com/questions/28931224/adding-value-labels-on-a-matplotlib-bar-chart
- http://stackoverflow.com/questions/16090241/pandas-dataframe-as-input-for-matplotlib-pyplot-boxplot

TO DO:
- Format the second histaogram function more nicely: add title and work out font-sizing and layout
- Write Test cases
- results.txt
'''

from regionalGDP import *
import sys


def main():

	#Until the user enters 'finish', asks for a year and displays a histogram using inc_by_year.
	get_display()

	#Then use the regionalGDP class to generate graphs for the years 2007-2012
	for year in range(2007,2013):
		try:
			print "Generating graphs for the year", str(year), "..."
			yearly_data = regionalGDP(year)
			yearly_data.plot_hist()
			yearly_data.plot_boxplot()
		
		#Just in case some of the years are not in the income df. 
		except InvalidDistributionRequest:
			pass


def prompt():
	try:
		return raw_input("Please enter a year.")
	except (KeyboardInterrupt, EOFError):
		sys.exit()


def get_display():

	#Asks the user to enter a year. Also accepts Ctrl+C and Ctrl+D.
	input = prompt()

	#If the user enters "finish", do nothing. 
	if input.strip().lower() == "finish":
		pass

	else:
		#inc_by_year prints "Invalid input." if input is not in the year column of the income df. 
		#Otherwise, displays a histogram. 
		if input.isdigit():
			inc_by_year(int(input))
		else:
			print "Invalid input."
		return get_display()


#Run the program
if __name__ == "__main__":
	main()