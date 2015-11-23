"""This is the class that visualizes """

#author: Matthew Dunn
#netID: mtd368
#date: 11/22/2015

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class visualizationtool(object):
    def __init__(self, year):
        self.year = year

    def boxploter(self, sortedlist):
        sortedlist[['Income']] = sortedlist[['Income']].astype(float)
        plt.figure()
        sortedlist.boxplot(column='Income', by='Region', rot='10', figsize=(10,8))
        plt.title('Per Capita GDP by Region in {}'.format(self.year))
        plt.suptitle("")
        plt.ylabel('Per Capita GDP')
        plt.ylim([0,100000])
        plt.savefig('Boxplot_by_Region_for_{}.png'.format(self.year))

    def regionshistogram(self, sortedlist):
        perCapitaGDPList, uniqueRegions = self.regionarraylistbuilder(sortedlist)
        plt.figure()
        plt.hist(perCapitaGDPList, stacked=True, bins=30, label=list(uniqueRegions))
        plt.legend()
        plt.ylabel('Number of Countries')
        plt.xlabel('United States Dollars')
        plt.xlim([0,100000])
        plt.title('Per Capita GDP by Region in {}'.format(self.year))
        plt.savefig('Dist_by_Region_for_{}.png'.format(self.year))

    def regionarraylistbuilder(self, sortedlist):
        uniqueRegions = sortedlist['Region'].unique()
        uniqueRegions = np.sort(uniqueRegions)
        incomelist = []
        for i in uniqueRegions:
            incomelist.append(sortedlist[sortedlist['Region']==i].Income)
        return incomelist, uniqueRegions

def histogrambuilder(sortedlist, year):

    """This is a public function that takes a sorted series object with the index set to country name and
    column 0 set to the gross domestic product per capita for the country for one year."""

    filterdCountryNameList = ylabelmanufacturer(sortedlist)
    y_pos = np.arange(len(sortedlist))
    ymax = len(sortedlist)
    gdpgivenyear = sortedlist
    fig = plt.figure(figsize=(8, 12))
    plt.barh(y_pos, gdpgivenyear, height=1, alpha=0.4)
    plt.yticks(y_pos, filterdCountryNameList.values, verticalalignment='bottom', fontsize=10)
    plt.ylim(0.0, ymax)
    ymin, ymax = plt.ylim()
    plt.ylabel('Every Three Countries Filterd List')
    plt.xlabel('Amount Per Capita (USD)')
    plt.title('GDP Per Capita for %d' %year)
    fig.set_tight_layout(True)
    plt.show()

def ylabelmanufacturer(sortedlist):

    """helper function to organize the y label values into a list with blank spaces"""

    namemanager = pd.DataFrame(sortedlist)
    countrynames = sortedlist.index.values
    everythreenames = countrynames[::3]
    everythreenames = pd.DataFrame(everythreenames)
    everythreenames.columns = ['Countries']
    everythreenames['Countries2'] = everythreenames['Countries']
    mergedbacktocreatespaces = pd.merge(namemanager, everythreenames, how='left', left_index=True, right_on='Countries')
    df1 = mergedbacktocreatespaces['Countries2'].replace(np.nan,' ', regex=True)
    return df1
