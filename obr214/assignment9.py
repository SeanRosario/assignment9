from areaincomegraphs import AreaIncomeGraphs
from dataframefunctions import load_dataframes, get_hist_income_per_year, merge_by_year

__author__ = 'obr214'

countries_filename = 'countries.csv'
income_filename = ['indicator gapminder gdp_per_capita_ppp.xlsx', 'Data']

try:
    #Creates the dataframes loading the correspondant files
    countries, income = load_dataframes(countries_filename, income_filename)

    if countries is not None and income is not None:
        #Asks the user for a year
        year_flag = True
        while year_flag:
            user_input = raw_input("Insert Year: ")

            if user_input == 'finish':
                year_flag = False
            else:
                try:
                    #Try to cast the input to Integer
                    user_year = int(user_input)
                    if 1800 <= user_year <= 2012:
                        get_hist_income_per_year(income, user_year)
                    else:
                        print "Enter a year between 1800 and 2012"
                except ValueError:
                    print "Please insert a valid year"

        print "Generating Plots from 2007-2012..."

        try:
            for year in range(2007, 2013, 1):
                #Creates the merged file
                countries_merged_df = merge_by_year(income, countries, year)
                #Creates the object
                plotting = AreaIncomeGraphs(year, countries_merged_df)
                plotting.create_plots()
        except ValueError as valueerror_message:
            print valueerror_message

except IOError as ioerror_message:
    print ioerror_message
except LookupError as lookuperror_message:
    print lookuperror_message