'''
Created on Nov 23, 2015

@author: jj1745

The main program of assignment 9 where we read and process data, and perform data analysis
'''


from yearly_plots import provideYearlyPlot
from exploratory_analysis import ExploreYearlyData
 
if __name__ == '__main__':
    
    # keep asking for year input and display distributions
    provideYearlyPlot()
    
    # for question 8, where we use the class to generate graphs
    years = [2007, 2008, 2009, 2010, 2011, 2012]
    
    for y in years:
        analysis_y = ExploreYearlyData(y)
        analysis_y.plotHisto()
        analysis_y.plotBox()
    
    print 'Graphs for 2007-2012 have been saved. Thanks!'   
    
    
    