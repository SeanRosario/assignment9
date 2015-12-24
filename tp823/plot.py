class plot:
    'Transforms a DataFrame to a plot'
    def __init__(self,x):
        self.x=x
    
    def histogram(self): 
        'Returns a Histogram'
        x=self.x[['Region','Income']]
        x=x.hist(by= 'Region',figsize=(20,11))
        

    def barplot(self):
        'Returns a Barplot' 
        x=self.x[['Region','Income']]
        x=x.boxplot(by='Region',figsize=(11,12))

