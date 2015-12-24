'''
Created on Nov 21, 2015
This program returns graphical representations of Income Per Person. To end program, please enter finish.
@author: Taurean Parker
'''

import sys
import matplotlib.pyplot as plt
from my_data_frame import data_frame
from plot import plot
import pandas as pd

countries=data_frame('countries.csv')
income=data_frame('indicator gapminder gdp_per_capita_ppp.csv')
income_year= income.view().drop('gdp pc test',1).columns.values.tolist() # List of Valid Years


def plot_income_gpb(year):
    'Plot a histogram of the worldwide distribution of Income'
    plot= income.view()[[str(year)]]
    plot.hist()
    
def merge_by_year(year):
    'Merge Country and Income DataFrames by Year'
    new_data=pd.merge(countries.view(), income.view(), left_on = 'Country', right_on = 'gdp pc test') # Merge Countries and Income
    new_data=new_data.rename(columns = {str(year):'Income'})
    return new_data[['Country','Region', 'Income']]

if __name__ == "__main__":
    while True:
        try:
            year = raw_input("Please enter a year to return  a Graphical Analysis of Distribution of Income Per Person:")
           
            if year in income_year:      
                transpose= income.view().transpose() #View contents of the DataFrame
                print transpose.head()
                
                
                merge_sets=merge_by_year(year) # Merge Income and Country datframes
                
                # Plot a barplot by Income and Region
                barplot_by_region=plot(merge_sets).barplot()
                plt.ylabel('Income(US Dollars)')
                plt.title('Distribution Of Income Per Person By Region In '+ str(year))
                path='GDP_barplot_by_region_in_%s.pdf' %year
                plt.savefig(path) 
                
                # Plot a histogram by Income and Region
                histogram_by_region=plot(merge_sets).histogram()
                plt.figtext(.45,.95,'Distribution Of Income Per Person By Region In '+ str(year), fontsize=18, ha='center')
                path='GDP_histogram_by_region_in_%s.pdf' %year
                plt.savefig(path) 
                
                # Plot Historgram by Distrubtuion of Income Worldwide
                plot_gpc_country= plot_income_gpb(year) # Return a plot gpc by year 
                plt.xlabel('Income(US Dollars)')
                plt.ylabel('Frequency')
                plt.title('Worldwide Distribution Of Income Per Person  In '+ str(year)) 
                path='GDP_Worldwide_Income_in_%s.pdf' %year
                plt.savefig(path) 
                
                
                plt.show()
            
            elif year == 'finish':
                print 'You have ended the program'
                break

            else:
                print 'Not a Valid entry. Please enter a valid year'
        except KeyboardInterrupt:
            print 'Keyboard Interrupt. Please enter a valid year'
            
      
      
      




         



