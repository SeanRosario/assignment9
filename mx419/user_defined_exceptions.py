"""this module define some user-defined exceptions"""

#author: Muhe Xie
#netID: mx419
#date: 11/16/2015



class Empty_Input_Error(Exception):
    # raised when user input is empty
    def __str__(self):
        return 'The input is empty\n'

class Invalid_Input_Error(Exception):
    # raised when user input  is not valid
    def __str__(self):
        return 'The input is not valid'
