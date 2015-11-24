import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataExplorer(object):
    '''Manage exploratory data analysis'''

    def __init__(self, dataframe, year=None, by="Region"):
        '''Constructor. Sets the object's year (for titles) and data'''
        self.year = year
        self.data = dataframe
        self.by_var = by
        self.data['logged_income'] = np.log10(self.data["Income"])

    def income_histogram(self):
        '''Construct an array of histograms of income'''
        xticks = np.arange(2, 5.5, 0.25)
        xtick_labels = (10**xticks).astype('int')

        subplots = self.data.hist(column="logged_income", by=self.by_var, sharex=True, figsize=(10, 8),
                                    bins=xticks)

        fig = plt.gcf()
        fig.suptitle("Distribution of Countries' GDP per Capita, %s" % self.year)
        fig.subplots_adjust(bottom=0.15)

        yticks = np.arange(0, int(50. / len(subplots.flatten())**.35), 5)
        for subplot in subplots.flatten():
            # Set x scale to be log but show unlogged values
            subplot.set_xlabel("Income (Log Scale)")
            subplot.set_xticks(xticks)
            subplot.set_xticklabels(xtick_labels)

            #Set y scale
            subplot.set_yticks(yticks)
        return fig

    def income_boxplot(self):
        '''Create boxplot by by_var and return result'''
        # BOXPLOT
        self.data.boxplot(by=self.by_var, showmeans=True)
        box_fig = plt.gcf()
        # Clean labels
        locs, labels = plt.xticks()
        # Convert labels to title case, split on space, join on newline
        clean_labels = ["\n".join(lab.get_text().title().split(" ")) for lab in labels]
        plt.xticks(locs, clean_labels)
        return box_fig

    def plot(self):
        '''Construct an array of histograms and a box plot by region, returning
        each.'''
        return self.income_histogram(), self.income_boxplot()

    def save_plots(self, hist_file="hist.png", box_file="boxplot.png"):
        '''Save plots to files'''
        hist_fig, box_fig = self.plot()
        hist_fig.savefig(hist_file)
        box_fig.savefig(box_file)
