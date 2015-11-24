"""
This part generates the results, it launches an small interfase where the user has to write what to do, whenever a result
is launched, it returns to the main window.
Exception handling and input validation is done for each part.
"""
import InitialCharge as IC
import  DescriptiveAnalysisTool as DAT
from matplotlib import  pyplot as plt
import  pandas as pd


__author__ = 'lqo202'


##### Previous functions to validate input, handle exceptions and launch the result####

#Validating and Handlding exceptions for the plot of Income distribution per year#
def printTotalPlotByYear(year):
    print 'Income Plot by year'
    try:
        if isinstance(year,int):
            if year>=1800 and year<=2012:
                IC.UtilsFunctions.plotDistributionIncomePerson(year)
                plt.show()
                print "Printed, close to continue"
                loop()
            else:
                raise LookupError
        else:
            raise LookupError
    except ValueError:
        print "Oops!  That was no valid input.  Try again!"
    except KeyboardInterrupt:
        print 'Keyboard interrupted, try again!'
    except ArithmeticError:
        print 'ArithmeticError ocurred'
    except LookupError:
        print 'Year must be between 1800 and 2012'
    except AttributeError:
        print 'Attribute error. Values inputted not of the type specified, try again!'

#Validating and Handlding exceptions for the plot of Income distribution per region between 2007 and 2012#
def printSixYearPlots():
    print 'Generating Income Exploratory Data Analysis by Regions between 2007 and 2012'
    try:
        for year in range(2007,2013):
            DAT.DescriptiveAnalysisTool(year).plotHistogramBoxPlot()
            print "PDF files with graphs of year  "+str(year)+' were generated'
        loop()
    except KeyboardInterrupt:
        print 'Keyboard interrupted, try again!'
    except ArithmeticError:
        print 'ArithmeticError ocurred'
    except LookupError:
        print 'LookupError ocurred'
    except DAT.DescriptiveException as messageerror:
        print messageerror


############## Final screening of results #########

#Function to captue the answer and launch the appropiate result
def captureanswer(answer, year=2007):
    try:
        if answer==1:  printTotalPlotByYear(year)
        if answer==2:  printSixYearPlots()
        else:
            raise ValueError
    except ValueError:
        print "Oops!  That was no valid input.  Try again!"
    except KeyboardInterrupt:
        print 'Keyboard interrupted, try again!'


#Function to do the loop of asking an input from the user
def loop():
    while True:
        try:
             optionuser = raw_input('Menu: Enter a year to display its income distribution or write finish to go to next process, q to quit')
             if optionuser == 'finish':
                 captureanswer(2)
             elif optionuser == 'q': break
             else:
                 optionuser = int(optionuser)
                 captureanswer(1,optionuser)
        except ValueError:
            print "Oops!  That was no valid input.  Try again!"
        except KeyboardInterrupt:
            print 'Keyboard interrupted, try again!'
        except DAT.DescriptiveException as messageerror:
            print messageerror


def mainwindow():
    print 'Historic Income Data Analysis Tool Assignment 9 - Programming for Data Science'
    print 'First result: Header of income Dataset'
    print IC.UtilsFunctions.getDataIncome().head()
    loop()


if __name__ == "__main__":
    try:
        mainwindow()
    except EOFError:
        pass

