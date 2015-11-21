import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataExplorer(object):
    '''Manage exploratory data analysis'''

    def __init__(self, dataframe):
        self.data = dataframe

    def plot(self):
        self.data.hist(by="Region", sharex=True, figsize=(10, 8), layout=(2, 3))
        self.data.boxplot(by="Region")
        plt.show()
