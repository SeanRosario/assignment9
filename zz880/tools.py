from functions import *
import pandas as pd
import matplotlib.pyplot as plt

class tools():
    # check if year is between 1800 and 2012
    def __init__(self,year):
        if year >=1800 and year <= 2012:
            self.year = year
        else:
            print("input must be a year betweem 1800 and 2012")

    # function to plot and save histogram
    def plot_hist(self):
        data = merge_by_year(self.year)
        plt.figure()
        data.hist("Income", by = "Region", xlabelsize = 7, bins = 30)
        plt.xlabel("Income per Person")
        plt.ylabel("Frequent")
        plt.savefig("Income_histograms_by_region_for_year_{0}.png".format(self.year))
        plt.close()

    # function to plot and save boxplot
    def plot_boxplot(self):
        data = merge_by_year(self.year)
        plt.figure()
        data.boxplot("Income", by = "Region", fontsize = 10)
        plt.xlabel("Region")
        plt.ylabel("Income per Person")
        plt.title("Income per person by regions for year {0}".format(self.year))
        plt.savefig("Income_boxplots_by_region_for_year_{0}.png" .format(self.year))
        plt.close()

