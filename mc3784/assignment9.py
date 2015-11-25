'''
Created on Nov 18, 2015

@author: micheleceru
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

from  dataAnalysis import dataAnalysis

class framesLoader():
    countries = 0
    income = 0
    incomeTransposed = 0
    
    def __init__(self):
        """
            This method load the data contained in the two files:
            ../countries.csv 
            ../indicator gapminder gdp_per_capita_ppp.xlsx 
            into two dataframe.
            It than transposes the data from the second file and displais the head of the Dataframe  
        """
        self.countries = pd.DataFrame.from_csv('../countries.csv')
        self.income = pd.read_excel('../indicator gapminder gdp_per_capita_ppp.xlsx') 
        self.incomeTransposed = self.income.transpose()
        print "Head of the Dataset"
        print self.income.head()        
     
    def getHistForYear(self,year,safe=False):
        """
            This function plot the histogram for a given year.
        """
        incomeTransposed = self.incomeTransposed.loc[year]
        incomeTransposed=incomeTransposed.fillna(0)
        bins = np.linspace(1, max(incomeTransposed), 100)
        plt.title(year)
        plt.hist(incomeTransposed,bins)
        plt.xlabel('Income')
        plt.ylabel('Number of countries')
        if safe:
            fileName="histagram_"+str(year)+".pdf"
            plt.savefig(fileName)
        else:
            plt.show()   
        plt.clf()
        
    def merge_by_year(self,year,savePlot=False):
        """
            This function merge the two data frame.
        """
        incomeColumns = self.income[['gdp pc test',year]]
        mergedDf = pd.merge(incomeColumns, self.countries, left_on='gdp pc test', right_on=self.countries.index.values, how='outer')
        dtAnalysis = dataAnalysis(mergedDf.dropna(axis=1,how='all'))
        dtAnalysis.plotBox(year,savePlot)


def manageUserFlow():
    """
        This function drive the flow of the program. There is a while loop that keep askint to the user to insert a year until the user type finish.
        Than the funcion safe the required plots and the program terminate.
    """
    keepGoing=True
    fmLoader=0
    try:
        while(keepGoing==True): 
            userinput = raw_input("Write a year: ") 
            if userinput=="finish":
                if fmLoader == 0:
                    fmLoader=framesLoader() 
                year=2007
                for i in range(6):
                    fmLoader.getHistForYear(year,True)
                    fmLoader.merge_by_year(year,True)
                    year+=1
                keepGoing=False
            elif userinput.isdigit()==False: 
                print "This is not a year"
            elif int(userinput)<1800 or int(userinput)>2012:
                print "Please enter a year between 1800 and 2012"
            else:
                fmLoader=framesLoader() 
                fmLoader.getHistForYear(int(userinput))
                fmLoader.merge_by_year(int(userinput))
                
        sys.exit()
    except KeyboardInterrupt:
        print "\nYou have pressed Control-C: The program is going to terminate" 
    
        
if __name__=="__main__":
    manageUserFlow()
    
    