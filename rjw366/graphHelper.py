'''
Created on Nov 22, 2015

@author: rjw366
'''

import matplotlib.pyplot as plt


def distOfIncomesByCountry(income,yearGDP):
    '''
    Takes in the income dataset and year
    Provides bar graph of incomes for that year
    '''
    plt.close()
    incomeForYear = income.loc[[yearGDP]].T.sort(yearGDP)
    dfSize=len(incomeForYear)
    incomeForYear1 = incomeForYear[0:dfSize//3]
    incomeForYear2 = incomeForYear[dfSize//3:2*dfSize//3]
    incomeForYear3 = incomeForYear[2*dfSize//3:dfSize]
    incomeForYear1.plot(kind='bar', figsize=(16, 8), title=1)
    incomeForYear2.plot(kind='bar', figsize=(16, 8), title=2)
    incomeForYear3.plot(kind='bar', figsize=(16, 8), title=3)
    plt.show()
    
def merge_by_year(income,countries,year):
    '''
    Takes in the countries and income datasets and year
    Returns the joined table based on the provided year
    '''
    incomeByYear=income.loc[[year]].T
    incomeByYear.index.name = 'Country'
    joined = countries.join(incomeByYear,on='Country', how='right')
    joined.rename(columns={year: 'Income'}, inplace=True)
    return joined
    
def exploringJoined(joined,year):
    '''
    Takes in joined dataset and saves the histogram and boxplots
    of the data by region
    '''
    plt.close()
    joined['Income'].hist(by=joined['Region'])
    plt.savefig('Income_histogram_'+str(year)+'.png')
    joined.boxplot(by='Region')
    plt.savefig('Income_boxplot_'+str(year)+'.png')
    