"""this is for the user-defined exceptions"""

class Empty_Input_Error(Exception):
      # this is for the empty input from user
      def __str__(self):
	  return 'The input is empty\n'

class Invalid_Input_Error(Exception):
      # this is for the unproper input from user
      def __str__(self):
	  return 'The input is invalid'
