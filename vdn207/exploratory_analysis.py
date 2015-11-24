'''
Varun D N, vdn207
DS-GA 1007 - Assignment 9
'''

'''Exploratory analysis class'''

import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd 

class ExploratoryAnalysis:
	'''Graphically explores the given data'''

	def __init__(self, start_year, end_year, countries_obj, income_obj):
		'''Constructor'''

		self.year_range = range(start_year, end_year + 1)
		self.countries = countries_obj
		self.income = income_obj

	def generate_histogram_plots_by_region(self):
		'''Generates all the plots based on region for every year in the range asked'''

		for year in self.year_range:
			merged_data = merge_by_year(year, self.countries, self.income)
			regions = set(merged_data.Region.values)

			for region in regions:
				region_data = merged_data.loc[merged_data.Region == region, ]

				region_data["Income"] = region_data["Income"].convert_objects(convert_numeric=True)

				plt.close("all")
				plt.figure(figsize=(12, 9))
				plt.barh(np.arange(1, 4 * region_data.shape[0], 4), region_data["Income"].tolist())
				plt.xlabel('Income Per Person')
				plt.title('Bar Plot of income per person across countries in the region %s for the year %d' % (region, year))
				plt.yticks(np.arange(1, 4 * region_data.shape[0], 4) + 1.25, list(region_data.Country.values))
				plt.savefig("outputs/" + region + "_" + str(year) + ".png")


def merge_by_year(year, countries_obj, income_obj):
	'''Merges the country specific income based on the year and returns the new data frame'''

	if year in income_obj.indices():
		year_income = income_obj.get_row(year - 1800)
		year_income.fillna(0, inplace=True)
	else:
		raise cexcep.YearNotFoundException("The data for the year is not available")

	countries = countries_obj.get_dataframe()
	countries["Income"] = ""

	for country in income_obj.column_names():
		try:
			countries.loc[countries["Country"].values == country, "Income"] = year_income[country]

		except KeyError:
			continue

	return countries