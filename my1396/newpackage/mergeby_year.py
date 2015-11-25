import pandas as pd
import matplotlib.pyplot as plt

def display_income_by_year(year,income_dataset):
    disp_income_dataset=income_dataset.ix[year]
    plt.hist(disp_income_dataset.dropna())
    plt.title('Distribution of income of all countries in '+ str(year))
    plt.show()


def merge_by_year(year,coutries_dataset,income_dataset):
    income_year=income_dataset.ix[year]
    df_income=pd.DataFrame(income_year)
    df_income['Country']=df_income.index
    merged_dataset=pd.merge(coutries_dataset,df_income,how='inner')
    merged_dataset=merged_dataset.rename(columns={year:'Income'})
    return merged_dataset
    
    
    