
__author__ = 'sb5518'

""" This program is meant to provide insights about income per capita distribution for each region in the globe by year.
Data is available from 1800 to 2012.

First, the program will ask user to input a year in that range. Spaces are not allowed, and any input other than a number
in the range 1800-2012 will be considered invalid. In case the input is invalid, the program will ask for input again.

When a valid year is introduced, the program will plot an histrogram to show the distribution of income per capita across the
globe for that particular year.

When the user closes the histogram window, the program will ask for input again, and repeat the process until the user
enters the work "finish"

After that, the program will plot histograms and boxplots to show income per capita and save them in individual files.
The charts will be plotted by region and by year.

Please make sure that the files 'countries.csv' and 'indicator gapminder gdp_per_capita_ppp.xlsx' are in the same directory as this program """

import loaderandmerger
import plot_income_by_region

list_of_valid_years = ('1800','1801','1802','1803','1804','1805','1806','1807','1808','1809','1810','1811','1812','1813','1814','1815','1816','1817','1818','1819','1820','1821','1822','1823','1824','1825','1826','1827','1828','1829','1830','1831','1832','1833','1834','1835','1836','1837','1838','1839','1840','1841','1842','1843','1844','1845','1846','1847','1848','1849','1850','1851','1852','1853','1854','1855','1856','1857','1858','1859','1860','1861','1862','1863','1864','1865','1866','1867','1868','1869','1870','1871','1872','1873','1874','1875','1876','1877','1878','1879','1880','1881','1882','1883','1884','1885','1886','1887','1888','1889','1890','1891','1892','1893','1894','1895','1896','1897','1898','1899','1900','1901','1902','1903','1904','1905','1906','1907','1908','1909','1910','1911','1912','1913','1914','1915','1916','1917','1918','1919','1920','1921','1922','1923','1924','1925','1926','1927','1928','1929','1930','1931','1932','1933','1934','1935','1936','1937','1938','1939','1940','1941','1942','1943','1944','1945','1946','1947','1948','1949','1950','1951','1952','1953','1954','1955','1956','1957','1958','1959','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012')
list_of_years_graph_explorer = (2007, 2008, 2009 , 2010 , 2011 , 2012 )

is_input_correct = False

while is_input_correct == False:    #Loop until we get a valid input year

    try:
        user_input = raw_input("Please enter a year from 1800 to 2012. No spaces are allowed ")

        if user_input in list_of_valid_years:
                is_input_correct = True
                year = int(user_input)
                loaderandmerger.income_distribution_hist(year)
        else:
                print "Please enter a valid year from 1800 to 2012"

    except (KeyboardInterrupt, EOFError): #avoid interrupting the program
        continue

user_input_2 = "hey"

while user_input_2 <> "finish":  #Loop until user inputs 'finish'

    try:
        user_input_2 = raw_input('Please enter another year from 1800 to 2012.  '
                                 'If you do not want to enter more years, please write "finish". '
                                 'No spaces are allowed.')

        if user_input_2 in  list_of_valid_years:
            year = int(user_input_2)
            loaderandmerger.income_distribution_hist(year)

        elif ((user_input_2 not in list_of_valid_years) and (user_input_2!="finish")):
            print "Please enter a valid year from 1800 to 2012"

    except (KeyboardInterrupt, EOFError): #avoid interrupting the program
        continue


for year in list_of_years_graph_explorer:
    plot_income_by_region.graphical_explorer(year)