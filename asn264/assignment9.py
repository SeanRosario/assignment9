'''
Author: Aditi Nair
Date: November 12 2015
Resources: http://stackoverflow.com/questions/6986986/bin-size-in-matplotlib-histogram

TO DO:
- Write Test Cases
- Fix histogram in inc_by_year
- Do histogram in class
- Do boxplot in class
'''

from regionalGDP import *
import sys


def main():

	#Until the user enters 'finish', asks for a year and displays a histogram using inc_by_year.
	get_display()

	#The use the class from problem 6 to generate graphs for the years 2007-2012


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
		inc_by_year(input)
		return get_display()


#Run the program
if __name__ == "__main__":
	main()