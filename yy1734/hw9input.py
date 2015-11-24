# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24: Cloudy

@author: YY
"""

import sys

def inputYear():
    
    try: 
        input = raw_input("Please enter a year between 1800 to 2012 or enter finish to quit:\n")
    except(KeyboardInterrupt, EOFError):
        sys.exit()
        
    if input.lower() == "quit":
        sys.exit()
        
    elif input.lower() == "finish":
        sys.exit()
        
    else:
        try:
            year  = yearValidation(input)
            return year
        except yearException:
            print("Invalid Year! ")
            return inputYear()
        


#Validate input value: positive and integer        
def yearValidation(s):

    if s.isdigit()  and int(s) != 0:
        year = int(s)
        if year < 1800 or year > 2012:
            raise yearException()
        else:
            return year
    else:
        raise yearException()


class yearException(Exception):
    def __str__(self):
        return "Invalid Year"
        

 
       
