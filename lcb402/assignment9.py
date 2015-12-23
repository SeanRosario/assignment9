### Laura Buchanan 
### lcb402

from country_gdp import *
import sys

if __name__ == "__main__":

	# Function to group together analysis that's computed for several different years
	def do_it_all(year):
        	# Load data
        	explore = country_gdp(year)
        	countries = explore.load_countries()
        	income = explore.load_income()

        	# Plot income per person across all countries in a given year
        	explore.plot_gdp_data()

        	# Plot distribution of income per person by region with histogram and boxplot
        	explore.merge_by_year()
        	explore.hist_merged_data()
        	explore.boxplot_merged_data()

	# Interact with user: get year of interest or 'finish' and make graphs 
	valid_years = range(1800,2013)
	valid_years = map(str,valid_years)
	year_check = 0 
	try:
		while year_check == 0:
			print "What year would you like to explore?"
			year = raw_input("Choose a year between 1800 and 2012: ")
			if year == 'finish':
                		year_check = 1
			elif year in valid_years:
				year = int(year)
				do_it_all(year)
			else:
				print "Sorry, I don't understand."

		extra_years = range(2007,2013)
		print "Making graphs for the years 2007 through 2012..."
		for year in extra_years:
			do_it_all(year)
		print "All done!"
		sys.exit(1)

	except KeyboardInterrupt:
		print "\nProgram ended by user."
		sys.exit(1)
