'''
Created on Nov 17, 2015

@author: Benjamin Jakubowski (buj201)
'''

if __name__ == '__main__':
    pass

from exploratory_analysis_class import *

## Answer question 3 by loading transposed income DataFrame 

print 'Question 3: Print head for tranposed income DataFrame.\n'
show_transposed_income_head()

## Answer question 7 

def get_year_from_user():
    ''' User inputs a year between 1800 and 2012. If value input, produces a plot showing the
    distribution of median income for that year. To quit, enter 'finish'.'''
    while True:
        try:
            year = raw_input('Enter a year (to plot per capita income by country for input year):\n')
            if year == 'finish':
                break
            else:
                try:
                    year = int(year)
                    plot_income_by_year(year)
                except ValueError:
                    print "Year must be between 1800 and 2012."
        except KeyboardInterrupt:
            print "If you're trying to quit enter 'finish'"
    return
    
#Call function so it runs on bash call 'python assignment9.py'
get_year_from_user()

## Answer question 8- generate graphs for 2007-2012

def generate_graphs_2007_2012():
    '''Generates boxplots and histograms summarizing distribution of median incomes
    by region for the years 2007-2012.'''
    for year in range(2007,2013):
        year_data = Explore_year(year)
        year_data.construct_histograms(use_max = False)
        year_data.construct_boxplots()
        
generate_graphs_2007_2012()