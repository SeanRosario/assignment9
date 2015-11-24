#author Yichen Fan
#Q4 graphcially display the ditribution of income per person across all countires in the world for the given year 

import pandas as pd
import matplotlib.pyplot as plt
from Input_merge import *
from analyze_tool import *
import sys

def main():

	while True:
		try:
			year = raw_input('Choose a year from 1800 to 2012 to see the plot of distribution of income per person')
			if year == 'finish':
				break
			if int(year) >= 1800 and int(year)<=2012:#check if the input is in the right range
				income_dataframe = load_gdp_csv()
				plt.figure()
				income_dataframe.ix[year,:].dropna().hist(bins=20)	#select data by given year, drop not avaliable data and plot				
				plt.title('Distribution of income per person in {}'.format(year))
				plt.xlabel('Income per person')	
				plt.show()
			else:
				print("Please retype the year you want to see from 1800 to 2012")

		except KeyboardInterrupt:
				print 'Invalid Input'
		except ValueError:
				print 'Error Exist'
				sys.exit(1)

	for i in range(2007, 2013):#to display graphs in a given year range using class
		income = load_gdp_csv()
		countries = load_countries_csv()
		merged_dataframe = merge_by_year(income, countries, str(i))
		merged_distribution = analyze_tool(i, merged_dataframe)
		merged_distribution.hist_by_region()
		merged_distribution.by_boxplots()
   	print("Files saved, program finished")

		


   
if __name__ == '__main__':
	main()



