__author__ = 'sb5518'


"""
This class contains three Functions:

- load_indicators receives the names of two files with the variables file_countries_dict, file_income_data

        It is important to clarify that these files are expected to be 'countries.csv', 'indicator gapminder gdp_per_capita_ppp.xlsx'
        which were provided in HomeWork 9, or files with similar structure.

        This function puts the data into a pandas dataframe, transposes it, and prints the head.

- income_distribution receives an integer between 1800 and 2012 which corresponds to an year, and plots the distribution of income
    for that particular year. It uses the load_indicator function to load data.

- merge_by_year receives a similar integer as income_distribution_hist. It merges the two files and creates a new table as required by
    Homework 9

"""

import pandas as pd
import matplotlib.pyplot as plt


list_valid_years = (1800,1801,1802,1803,1804,1805,1806,1807,1808,1809,1810,1811,1812,1813,1814,1815,1816,1817,1818,1819,1820,1821,1822,1823,1824,1825,1826,1827,1828,1829,1830,1831,1832,1833,1834,1835,1836,1837,1838,1839,1840,1841,1842,1843,1844,1845,1846,1847,1848,1849,1850,1851,1852,1853,1854,1855,1856,1857,1858,1859,1860,1861,1862,1863,1864,1865,1866,1867,1868,1869,1870,1871,1872,1873,1874,1875,1876,1877,1878,1879,1880,1881,1882,1883,1884,1885,1886,1887,1888,1889,1890,1891,1892,1893,1894,1895,1896,1897,1898,1899,1900,1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915,1916,1917,1918,1919,1920,1921,1922,1923,1924,1925,1926,1927,1928,1929,1930,1931,1932,1933,1934,1935,1936,1937,1938,1939,1940,1941,1942,1943,1944,1945,1946,1947,1948,1949,1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012)

class MyError(Exception):  #This class is used to raise errors in the loaderandmerger class
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)


def load_indicators(file_countries_dict, file_income_data):

    try:
        countries = pd.read_csv(file_countries_dict)
        indicator = pd.read_excel(file_income_data, sheetname=0, index_col=0).T
        print indicator.head()

    except IOError:
        raise IOError("At least one of the files was not found. Please be sure that  'countries.csv' and indicator 'gapminder gdp_per_capita_ppp.xlsx' are in the parent directory.")
    except TypeError:
        raise TypeError("Error: Make sure that required files are in the directory ")

    return countries, indicator

def income_distribution_hist(year):

    try:
        if year in list_valid_years:
            _, indicator_per_capita = load_indicators('countries.csv', 'indicator gapminder gdp_per_capita_ppp.xlsx')
            indicator_per_capita = pd.DataFrame(indicator_per_capita, index = [year])
            indicator_per_capita = indicator_per_capita.T
            indicator_per_capita.dropna().hist()
            plt.xlabel("Distribution of Income per capita")
            plt.show()
        else:
            raise MyError("Introduced integer was not between 1800 and 2012 which are the valid years")

    except IOError as e:
        print str(e)
    except TypeError as e:
        print str(e)


def merge_by_year(year):
    try:

        if year in list_valid_years:
            countries, indicator = load_indicators('countries.csv', 'indicator gapminder gdp_per_capita_ppp.xlsx')
            indicator = indicator.T
            indicator['Country'] = indicator.index
            indicator.set_index('Country')
            indicator = indicator[['Country', year]]
            merged_df = pd.merge(countries, indicator, how='inner', on='Country')
            merged_df.columns = ['Country', 'Region', 'Income']
            return merged_df
        else:
            raise MyError("Introduced integer was not between 1800 and 2012 which are the valid years")

    except IOError as e:
        print str(e)
    except TypeError as e:
        print str(e)


