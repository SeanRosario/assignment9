import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataExplorer(object):
    '''Manage exploratory data analysis'''

    def __init__(self, dataframe):
        self.data = dataframe

    def plot(self):
        self.data.hist(by="Region", sharex=True, figsize=(10, 8), layout=(2, 3))
        hist_fig = plt.gcf() # Get current figure

        self.data.boxplot(by="Region", showmeans=True)
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
