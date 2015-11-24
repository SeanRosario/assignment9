"""
DSGA 1007 Assignment 9
Lanyu Shang
11/24/15
"""

import sys
from Income import *


class RangeError(Exception): pass


def get_user_input():
    '''This function will get the input of year from user.'''
    #Ask user for a year
    try:
        user_input = raw_input("Enter the year of income you would like to see."
                               "(Enter 'finish' to quit.) -->")
    except KeyboardInterrupt:
        sys.exit()
    return user_input


def read_year(user_input):
    '''This function will convert the user input to integer year and validate it.'''
    try:
        year = int(user_input)
    except ValueError:
        raise
    if 1800 <= year <= 2012:
        return year
    else:
        raise RangeError


def main():
    income_data = Income()
    #Ask user for a year and exit until 'finish' entered.
    user_input = get_user_input()
    while user_input != 'finish':
        year = 0
        while year == 0:
            try:
                year = read_year(user_input)
                income_data.income_dist(year)
                break
            except ValueError:
                print "Invalid input. Please enter again."
            except RangeError:
                print "The year you entered is not in [1800, 2012]. Please enter again."
            user_input = get_user_input()
        user_input = get_user_input()
    #plot income data from 2007 to 2015
    income_data.plot_2007_2012()


if __name__ =='__main__':
    main()
