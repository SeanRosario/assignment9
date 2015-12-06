class invalid_input(Exception):
	'''user-defined exception for invalid input of year'''

	def __str__(self):
		return 'input is not valid'

class invalid_year(Exception):
	'''user-defined exception for input of year out of range'''

	def __str__(self):
		return 'year out of range'