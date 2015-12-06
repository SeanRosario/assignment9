'''
Varun D N, vdn207
DS-GA 1007 - Assignment 9
'''


'''Class corresponding to data frame details'''

import pandas as pd 
import custom_exceptions as cexcep 

class Dataframe:
	'''Handles a pandas dataframe'''

	def __init__(self, dataframe, transpose = False):	# Accepts only a pandas dataframe
		if isinstance(dataframe, pd.core.frame.DataFrame):
			self.dataframe = dataframe
			if transpose:
				self.dataframe = dataframe.transpose()
				self.dataframe.columns = self.dataframe.ix[0]
		else:
			raise cexcep.NotADataFrameException("The input is not a Pandas dataframe")

	def get_shape(self):
		'''Returns the shape of the dataframe'''

		return self.dataframe.shape 

	def get_dataframe(self):
		'''Returns the dataframe pertaiing to the class'''

		return self.dataframe

	def head_of_dataframe(self, x):
		'''Returns the head of this dataset'''

		return self.dataframe.head(n=x)

	def column_names(self):
		'''Returns the column names'''

		return self.dataframe.columns.values

	def indices(self):
		'''Returns the indices of the dataframe'''

		return self.dataframe.index

	def get_row(self, row_number):
		'''Returns a specific row number'''

		return self.dataframe.ix[row_number]