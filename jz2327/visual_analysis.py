import matplotlib.pyplot as plt 
import load_csv

class data_visulization():
	'''class to generate histograms and boxplots for given year.'''

	def __init__(self, year, merged_distribution):
		self.year = year
		self.distribution = merged_distribution

	def data_histograms(self):
		plt.figure()
		for region in self.distribution['Region'].unique():   #generate histograms of different region in a figure.
			region_distribution_dist = self.distribution[self.distribution['Region'] == region]
			plt.hist(region_distribution_dist['Income'].tolist(), label = region, stacked = False)
		plt.legend(loc = 'upper right')
		plt.title(self.year)
		plt.savefig('histograms_{}.png'.format(str(self.year)))

	def data_boxplots(self):
		plt.figure()
		self.distribution.boxplot(by = 'Region')   #boxplots grouped by region
		plt.title(self.year)
		plt.savefig('boxplots_{}.png'.format(str(self.year)))


