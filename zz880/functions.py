import pandas as pd
import matplotlib.pyplot as plt

# load csv file and name it countries
def read_csv(file_path):
    countries = pd.read_csv(file_path)
    return countries

# load xlcs file and name it income
# transpose the data frame and print head of the data set
def read_xlsx(file_path):
    income = pd.read_excel(file_path,sheetname='Data',index_col = 0)
    income_transpose = income.T
    print income_transpose.head()
    return income_transpose

# plot histogram of income per person across all countries in the world for the given year
def hist_plot(income,year):
    income_year = income.ix[year]
    income_year = income_year.dropna() # drop missing values
    income_year.hist(bins=30)
    plt.xlabel("Income per Person")
    plt.ylabel("Frequent")
    plt.title("Income per person across all countries in the world for year {0}".format(year))
    plt.show()

def merge_by_year(year):
    # file path should be modified
    countries = read_csv("/Users/zhaoyinzhu/Dropbox/NYU/GA 1007 Data Science/python/assignment9/countries.csv")
    income = read_xlsx("/Users/zhaoyinzhu/Dropbox/NYU/GA 1007 Data Science/python/assignment9/indicator gapminder gdp_per_capita_ppp.xlsx")
    merge_income = pd.DataFrame(income.ix[year].dropna(),index=None).reset_index()
    merge_income.columns = ['Country','Income']
    final_merge = pd.merge(countries, merge_income, how="left")
    return final_merge
