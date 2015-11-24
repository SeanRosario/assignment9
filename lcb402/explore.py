### Laura Buchanan ###
###     lcb402     ###

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import clean_and_merge as cnm


class explore_data_plots(object):
        def __init__(self,year):
		countries_data = cnm.load_countries_data('countries.csv')
		gdp_data = cnm.load_gdp_data('indicator gapminder gdp_per_capita_ppp/Data-Table 1.csv')
                self.data = cnm.merge_by_year(countries_data,gdp_data,year)
		self.year = year

def my_box_plot(self):
	plt.figure()
	plt.plot(self.data[['Income']])
	plt.title('Plot of Per Capita GDP in ' + str(year))
	plt.xlabel('Country Index')
	plt.ylabel('Per Capita GDP')
	plt.savefig('plot_{}.png'.format(self.year))



