#Author: Xing Cui
#NetID: xc918
#Data: 11/16


import pandas as pd
import numpy as np
import matplotlib as plot

"""loading csv file and excel file."""

#Question1
def import_csv(filePath):
	"""importing csv files"""

	data_csv = pd.read_csv(filePath, sep = ',')

	return data_csv

#Question2
def import_excel(filePath):
	"""importing excel files"""

	data_excel = pd.read_excel(filePath, index_col = 0)
	data_clean1 = data_excel.T
	print data_clean1.head()#Question3
	return data_clean1










