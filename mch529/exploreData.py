'''
This class contains 3 functions for making boxplots and histograms.

'''
#author:Michael Higgins
#netid:mch529

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
from assignment9 import *
from dataLoad import *
import matplotlib.patches as mpatches

class Explore(int):
	fontsize=15

	def __init__(self,year):
		self.year=year
		getData=Data()
		self.df = getData.mergeByYear(self.year)
		print "mergeByYear" , self.df.columns.values
		self.regions = self.df['Region'].unique()
		
	def graphBoxPlotByYearAndRegion(self):
		'''
		make a seperate box and whiskers for each region according to the class year.
		'''
		boxes=[]
		for region in self.regions:
		     boxes.append( self.df.loc[self.df['Region'] == region] )
		
		myPlot = plt.boxplot([box['Income'] for box in boxes], positions=range(len(boxes)) )
		#http://stackoverflow.com/questions/16592222/matplotlib-group-boxplots
	    # set colors for each individual region
		colors = "bgrcmykw"
		color_index = 0
		for i in range(len(self.regions)) :  #set colors
			plt.setp(myPlot['boxes'][i], color =colors[i] )
		plt.xticks(range(len(self.regions)),[name for name in self.regions], rotation= 15, ha='right')
		plt.title("Distribution of Income by Region in " +str(self.year),fontsize=18)
		plt.ylabel("GDP Per Capita", fontsize=12)
		#legends

		#plt.legend([r,g,r,c,m,y],self.regions)
		#plt.legend(loc='upper center', labels=regions)   #fix later set label
		#plt.show()
		plt.savefig('Box and Whiskers for ' + str(self.year) + '.png')
		plt.close()
	
	def generate_hist(self):
		boxes=[]
		for region in self.regions:
		     boxes.append( self.df.loc[self.df['Region'] == region] )
		plt.figure()
		plt.hist([box['Income'] for box in boxes], bins = 30, stacked=True,color = ['b', 'g', 'r', 'c', 'm', 'y'], label = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America'])
		plt.title('Distribution of Income by Region in year ' + str(self.year) )
		plt.legend()

		plt.savefig('Histogram for Year ' + str(self.year) + '.png')
		#plt.show()
		plt.close()



	def graphByYearForAllCountries(self):
		''' input is a valid year, output is a histogram of countries according
			to their mean income.  Y -axis is number of countries , X-axis is income/person
		'''
		plt2.hist(self.df["Income"], bins=30)
		plt2.xlabel('Average Income per Person')
		plt2.ylabel('Number Of Countries')
		plt2.title('Distribution of Income in ' + str(self.year) + ' for Every Country')
		plt2.show()

if __name__=='__main__':	
	x=Explore(2000)
	x.graphByYearForAllCountries()

