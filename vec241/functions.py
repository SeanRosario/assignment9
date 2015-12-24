'''
Defines the various functions required to run module assignment9.py
'''

import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib

__author__ = 'vec241'

def transformDataframe(dataframe):
    '''
    transforms the data set to have years as the rows and countries as the columns,
    then show the head of this data set when it is loaded
    '''

    #dataframe is income

    income_transpose = dataframe.transpose()

    # Countries becomes the column index
    new_index = [country for country in income_transpose.iloc[0]]
    income_transpose.columns = new_index
    # removes row containing the countries
    income_transpose = income_transpose.ix[1:]

    # Show 5 first rows
    income_transpose.head()

    return income_transpose


def plotIncomeDistribution(dataframe, year):
    '''
    Graphically displays the distribution of income per person across all countries in the world for the given year
    into a horizontal barchart
    '''

    #dataframe is income_transpose

    # rearranges the dataframe to be plotted
    dataframe_to_plot = pd.Series.to_frame(dataframe.ix[year])
    dataframe_to_plot = dataframe_to_plot.dropna(axis=0)
    dataframe_to_plot = dataframe_to_plot.sort(columns=year, ascending=True)

    #plots horizontal bar chart
    title = 'Income per person per country for year ' + str(year)
    dataframe_to_plot[year].plot(kind='barh', figsize=(20, 70), title=title, grid = True)

    plot_name = 'Income_distribution_for_year_'+str(year)
    plt.savefig(plot_name)
    plt.clf()

    print 'The plot has been saved in the current directory under the name {}'.format(plot_name)


def mergeByYear(year, income, countries):
    '''
    Merges the countries and income data sets for any given year.
    Returns a DataFrame with three columns titled Country, Region, and Income.
    '''

    merged = income[['gdp pc test', year]]
    merged = merged.rename(columns = {'gdp pc test':'Country', year:'Income'})
    merged['Region'] = 'No region found'

    #reorders columns
    col_list = list(merged)
    col_list[1], col_list[2] = col_list[2], col_list[1]
    merged = merged[col_list]

    #matches the countries with their region
    merged_Region_index = 1
    for country in merged['Country']:
        if country in countries['Country'].values:
            idx_countries = countries[countries['Country']==country].index.tolist()
            idx_merged = merged[merged['Country']==country].index.tolist()
            merged.iloc[idx_merged[0], merged_Region_index ] = countries.iloc[idx_countries[0], 1]

    return merged

def boxPlotPerRegion(year, income, countries):
    '''
    param year: year for which graph is displayed
    return: boxplot of the income per person by region
    '''

    merged = mergeByYear(year, income, countries)

    #groups the income (per person per country) into a dictionary per region
    income_per_region = {}
    for i in merged.index:
        if merged.iloc[i, 1] in income_per_region:
            income_per_region[merged.iloc[i, 1]].append(merged.iloc[i, 2])
        elif merged.iloc[i, 1] != 'No region found':
            income_per_region[merged.iloc[i, 1]] = [merged.iloc[i, 2]]

    #Splits into 2 lists : list of regions to illustrate the x axis of the plot, and the data to plot
    incomes_values = []
    region_names = []
    for key in income_per_region:
        incomes_values.append(income_per_region[key])
        region_names.append(key)

    #Plotting
    plt.boxplot(incomes_values)
    plt.xlabel(region_names)
    plot_name = 'Income_boxplot_per_region_for_year_'+str(year)
    plt.savefig(plot_name)
    plt.clf()

