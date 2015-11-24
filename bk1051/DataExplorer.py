import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataExplorer(object):
    '''Manage exploratory data analysis'''

    def __init__(self, dataframe, year=None):
        self.year = year
        self.data = dataframe

    def plot(self):
        self.data.hist(by="Region", sharex=True, figsize=(10, 8), layout=(2, 3))
        plt.title("Distribution of Countries' GDP per Capita, %s" % self.year)
        plt.xlabel("Income (Log Scale)")
        xticks = np.arange(2, 5.5, 0.25)
        #xtick_labels = [100, 500, 1000, 5000, 7500, 10000, 25000, 50000, 75000, 100000]
        xtick_labels = (10**xticks).astype('int')
        plt.xticks(xticks, xtick_labels)
        plt.yticks(np.arange(0, 55, 5))
        hist_fig = plt.gcf() # Get current figure

        self.data.boxplot(by="Region", showmeans=True)
        plt.yticks([100, 500, 1000, 5000, 7500, 10000, 25000, 50000, 75000, 100000])
        box_fig = plt.gcf()
        # Clean labels
        locs, labels = plt.xticks()
        # Convert labels to title case, split on space, join on newline
        clean_labels = ["\n".join(lab.get_text().title().split(" ")) for lab in labels]
        plt.xticks(locs, clean_labels)
        return hist_fig, box_fig

    def save_plots(self, hist_file="hist.png", box_file="boxplot.png"):
        hist_fig, box_fig = self.plot()
        hist_fig.savefig(hist_file)
        box_fig.savefig(box_file)
