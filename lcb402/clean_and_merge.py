### Laura Buchanan ###
###     lcb402     ###

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_countries_data(infile_name):   
    data = pd.read_csv(infile_name,sep=',',header=0)
    df = pd.DataFrame(data)
    return df
    
def load_gdp_data(infile_name):   
    data = pd.read_csv(infile_name,sep=',',header=0,index_col='gdp pc test')
    df = pd.DataFrame(data).transpose()
    df = df.dropna(axis=1)
    return df
    
#def plot_gdp_data(gdp_data,year):
#    data = gdp_data.loc[str(year)]
#    plot = plt.hist(data,bins=50)
#    plt.title('Income Per Person in ' + str(year))
#    plt.xlabel('Income Per Person in $')
#    plt.ylabel('# of Countries')
#    plot.show()
#    return plot

def merge_by_year(countries_data,gdp_data,year):
    gdp_data = gdp_data.loc[str(year)]
    gdp_data = pd.DataFrame(gdp_data)
    gdp_data.reset_index(level=0, inplace=True)
    gdp_data.rename(columns={'gdp pc test': 'Country',str(year):'Income'},inplace=True)
    merged_data = pd.merge(countries_data,gdp_data,on='Country',how='outer')
    merged_data = merged_data.dropna()
    return merged_data
