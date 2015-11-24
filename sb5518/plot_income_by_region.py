__author__ = 'sb5518'


""" This class takes as input the merged table created the merge_by_year function of the loaderandmerger class
and an integer representing a year.
The class creates individual histograms and boxplots for that particular year and for each region in the globle,
to show income per capita distribution.
"""

import loaderandmerger
import matplotlib.pyplot as plt
from loaderandmerger import MyError as loader_Error


class graphical_explorer:
    def __init__(self, year):
        try:
            income_by_country_region = loaderandmerger.merge_by_year(year)
            for region in income_by_country_region['Region'].unique():
                    plt.close()
                    to_plot_df = income_by_country_region[income_by_country_region['Region'] == region]
                    to_plot_df.hist()
                    plt.xlabel("Distribution of Income per capita")
                    plt.savefig("histogram_" + str(region) + "_" + str(year))
                    to_plot_df.boxplot()
                    plt.xlabel("Distribution of Income per capita")
                    plt.savefig("boxplot_" + str(region) + "_" + str(year))

        except IOError as e:
            print "Error, IOError " + str(e)
        except loader_Error as e:
            print str(e)



