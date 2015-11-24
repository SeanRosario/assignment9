from LoadData import *


class Explore(int):
    '''Class that takes in a year, and allows the user to explore
    the income per person across all regions through box plots and
    histograms'''
    
    def __init__(self, num):
        self.year = num
        self.data = merge_by_year(self.year)
    
    def generate_box(self):
        '''Function that generates boxplots for the average income per person
        for each different region in the given year'''
        regions = self.data['Region'].unique()
        boxes = []
        for region in regions:
            boxes.append(self.data.loc[self.data['Region'] == region])
        plt.boxplot([box['Income'] for box in boxes], positions = range(len(boxes))) 
        plt.xticks(range(len(regions)), [region for region in regions], rotation = 15) 
        plt.title('Income by Region in year ' + str(self.year))  
        plt.savefig('Box Plot for Year '+ str(self.year) + '.png')
        plt.close()

    def generate_hist(self):
        '''Function that generates a stacked histogram for the average
        income per person in each region for the given year'''
        regions = self.data['Region'].unique()
        boxes = []
        for region in regions:
            boxes.append(self.data.loc[self.data['Region'] == region])
        plt.figure()
        plt.hist([box['Income'] for box in boxes], bins = 30, stacked=True, 
                 color = ['b', 'g', 'r', 'c', 'm', 'y'], 
                 label = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America'])
        plt.title('Distribution of Income by Region in year ' + str(self.year))
        plt.legend()
        plt.savefig('Histogram for Year ' + str(self.year) + '.png')
        plt.close()

        
        