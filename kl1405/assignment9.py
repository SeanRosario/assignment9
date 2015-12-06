import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plot import *
from merge import *

# author: Kaiwen Liu
'''This main function will import files, run the merge and plot functions and write short descriptions'''

def main():
    # load files to dataframe
    countries=pd.read_csv('countries.csv', index_col=0)
    countries=pd.DataFrame(countries)
    #show the head of countries
    print countries.head()
    
    income=pd.read_excel('indicator gapminder gdp_per_capita_ppp.xlsx', index_col=0)
    income=pd.DataFrame(income)
    print income.head()

    #transpose so that year as row and countries as column
    income_t=pd.DataFrame.transpose(income)
    
   
    # Q4, Q7. ask for input of year, then display the distribution
    # exception handling

    while True:
        try:
            year = raw_input('enter a year to view the distribution of income per person: ')
            if year == 'finish':
                break
            else:
                year = int(year)
                if year >2012 or year < 1800:
                    raise ValueError
        except (EOFError, KeyboardInterrupt, ValueError):
            print 'ByeBye!!'
            sys.exit()

        # plot the distribution of given year
        data = income[year]
        plt.figure()
        n, bins, patches = plt.hist(data.dropna(), bins=20, color= 'red')
        plt.title('Distribution of income per person across all countries in {}'.format(year))
        plt.xlabel('income per person $')
        plt.show()
    
    
    
    # plot box and stacked histograms for year 2007-2012

    for year_ in range(2007, 2013):
        df = merge_by_year(income, countries, year_)
        plots(df,year_).stackedhistogram()
        plots(df,year_).boxplot()

    # short descriptions 
    result=open('results.txt','w')
    result.write('According to the boxplots, I find that Africa, Europe, south America and North America have very few change over the 5 years.')
    result.write('Overall, Europe has the highest income per person on average and Africa has the lowest.Asia has noticeable increase in come per person.\n')
    result.write('\n')
    result.write('According to the stacked histograms, I find that overall there is very few change over the 5 years.\n')
    result.write('Europe is widely spread out between smaller than 20000 and over 70000 while having the majority at 30000-40000.')
    result.write('For Asia and Africa, a large number of low incomes shifted up a little.\nFor the remaining regions, the change is not noticeable.')
    result.close()
    
if __name__ == '__main__':
    main()