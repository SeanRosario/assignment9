'''
Varun D N, vdn207
DS-GA 1007 - Assignment 9
'''

'''Module containing the functions for specific questions about the dataframe'''

import custom_exceptions as cexcep
import matplotlib.pyplot as plt
import numpy as np 

def income_per_person_by_year(year, data_object):
	'''Plots the bar graph of income per person of all countries for a specific year'''

	plt.close("all")	# Clearing any existing plot data

	if year in data_object.indices():
		year = year - 1800 	# Adjusting to the index of the data frame
		year_income = data_object.get_row(year)	
		year_income.fillna(0, inplace=True)
	else:
		raise cexcep.YearNotFoundException("The data for the year is not available")

	plt.figure(figsize=(18, 14))
	plt.barh(np.arange(1, 4 * year_income.shape[0], 4), year_income.tolist())
	plt.xlabel('Income Per Person')
	plt.title('Bar Plot of income per person across countries in the year %d' % (int(year) + 1800))
	plt.yticks(np.arange(1, 4 * year_income.shape[0], 4) + 1.25, list(year_income.index))
	plt.show()
