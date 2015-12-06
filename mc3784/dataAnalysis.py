'''
Created on Nov 24, 2015

@author: micheleceru
'''
import matplotlib.pyplot as plt
class dataAnalysis():
    
    df = 0
    def __init__(self,df):
        self.df=df.dropna()

    def plotBox(self,year,savePlot=False):      
        """
        This function print the Boxplots of the df DataFrame. If the parameter savePlot=true the plot is saved to a file.
        """  
        self.df.boxplot(year, by='Region')
        plt.xlabel('Region')
        plt.ylabel('Income')
        if savePlot:
            fileName="boxPlot_"+str(year)+".pdf"
            plt.savefig(fileName)
        else:
            plt.show()   
        plt.clf()
