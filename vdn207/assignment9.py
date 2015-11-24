'''
The main program for assignment 9

Varun D N, vdn207@nyu.edu
'''

import pandas as pd 
import numpy as np 
import data_frame_class as df_class
import custom_exceptions as cexcep
import question_specific_module as qspec
import matplotlib.pyplot as plt
import exploratory_analysis as ea 

if __name__ == '__main__':

	countries = pd.read_csv("data/countries.csv")
	income = pd.read_excel("data/indicator gapminder gdp_per_capita_ppp.xlsx")

	try:
		countries_obj = df_class.Dataframe(countries)
	except cexcep.NotADataFrameException as e:
		print str(e)

	# Question 3 - Printing the head of the dataset
	print countries_obj.head_of_dataframe(5)

	try:
		income_obj = df_class.Dataframe(income, True)
	except cexcep.NotADataFrameException as e:
		print str(e)

	# Question 3 - Printing the head of the dataset
	print income_obj.get_shape()

	print income_obj.head_of_dataframe(5)

	# Question 7 - Accepting the year from the user until 'finish' is entered

	print "----------------------------------------------------------------------------"
	print "Enter a year to explore or 'finish' to exit from this plotting"

	while True:
		try:
			year = raw_input("Enter a year: ")
			
			if year == "finish":
				break

			if isinstance(int(year), int):
				qspec.income_per_person_by_year(int(year), income_obj)
			else:
				print "Please enter a valid year (integer)"
				continue

		except (NameError, KeyboardInterrupt, ValueError):
			continue
			
	exploratory_obj = ea.ExploratoryAnalysis(2007, 2012, countries_obj, income_obj)
	exploratory_obj.generate_histogram_plots_by_region()