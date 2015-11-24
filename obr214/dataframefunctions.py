import pandas as pd
import matplotlib.pyplot as plt

__author__ = 'obr214'


def load_dataframes(countries_filename, income_filename):
    try:
        countries_df = pd.read_csv('../' + countries_filename)
        income_df = pd.read_excel('../' + income_filename[0], income_filename[1])
        income_df = income_df.dropna()
        income_df = income_df.transpose()

        income_df.columns = income_df.iloc[0]
        income_df = income_df.drop('gdp pc test')

        income_df = income_df.reset_index()
        income_df = income_df.set_index('index')

        print "Income DataFrame Head:"
        print income_df.head()

        return countries_df, income_df
    except IOError:
        raise IOError("Error: Files not found")
    except LookupError:
        raise LookupError("Error: Key or Index Problem")


def get_hist_income_per_year(income_df, year):
    try:
        year = int(year)
        income_year_row = income_df.loc[[year]]

        plt.hist(income_year_row.values[0])
        plt.xlabel("Income", fontsize=14)
        plt.ylabel("No. of Countries", fontsize=14)
        plt.title("Income Year:"+str(year), fontsize=14)
        plt.show()
    except ValueError:
        raise ValueError("Error: Year is not an Int")


def merge_by_year(income_df, countries_df, year):
    try:
        year = int(year)
        income_year_row = income_df.loc[[year]]

        income_year = income_year_row.transpose()
        income_year = income_year.reset_index()
        income_year.columns = ['Country', 'Income']

        merged_dataframe = pd.merge(countries_df, income_year, how='left', on=['Country'])

        merged_dataframe = merged_dataframe.fillna(0)
        merged_dataframe = merged_dataframe.sort(['Country'])
        merged_dataframe = merged_dataframe.reset_index(drop=True)

        return merged_dataframe
    except ValueError:
        raise ValueError("Error: Year is not an Int")