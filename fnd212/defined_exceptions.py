#Author: fnd212

class FatalError(Exception):
	def __init__(self,message):
		self.message = message

class InvalidUserInput(Exception):
	pass