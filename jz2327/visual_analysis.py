import matplotlib.pyplot as plt 
import load_csv

class data_visulization():
	'''class to generate histograms and boxplots for given year.'''

	def __init__(self, year, merged_distribution):
		self.year = year
		self.distribution = merged_distribution

	def data_histograms(self):
		label_list = self.distribution['Region'].unique().tolist()
		list_by_region = []
		for region in label_list:
			list_by_region.append(self.distribution[self.distribution['Region'] == region].Income)
		plt.figure()
		plt.hist(list_by_region, stacked = True, label = label_list)
		plt.legend(loc = 'upper right')
		plt.title(self.year)
		plt.savefig('histograms_{}.png'.format(str(self.year)))

	def data_boxplots(self):
		plt.figure()
		self.distribution.boxplot(by = 'Region')   #boxplots grouped by region
		plt.title(self.year)
		plt.savefig('boxplots_{}.png'.format(str(self.year)))


