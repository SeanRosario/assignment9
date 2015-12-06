import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

__author__ = 'obr214'


class AreaIncomeGraphs:

    def __init__(self, year, merged_dataframe):
        self.year = year
        self.countries_regions_income = merged_dataframe

    def create_plots(self):
        """
        From a given Merged Dataframe. It is separated by regions and then a histogram and a boxplot is created for
        each one.
        At the end, a World Boxplot is created with the 6 regions in it.
        """

        try:
            regions = self.countries_regions_income['Region'].unique()

            regions_values = []
            regions_names = []
            for idx, region in enumerate(regions):
                region_indexes = self.countries_regions_income['Region'].isin([region])
                region_df = self.countries_regions_income[region_indexes]
                regions_values.append(region_df['Income'].values)
                regions_names.append(region)

                print "Creating Plots for " + region + ": " + str(self.year)
                with PdfPages(region + '_' + str(self.year) +'_income_per_person.pdf') as pdf:
                    #Creates the Histogram for the given region
                    plt.hist(region_df['Income'].values)
                    plt.xlabel("Income Per Person", fontsize=14)
                    plt.ylabel("No. of Countries", fontsize=14)
                    plt.title(region + " - Income Per Person. Year: "+str(self.year), fontsize=14)
                    #plt.savefig(str(self.year) + "_" + str(region) + "_hist_income_per_person.pdf")
                    pdf.savefig()
                    plt.close()

                    #Creates the Boxplot for the given region
                    plt.boxplot(region_df['Income'].values)
                    plt.title(region + " - Income Per Person. Year: "+str(self.year), fontsize=14)
                    plt.xticks([1], [region])
                    plt.xlabel("Income")
                    pdf.savefig()
                    plt.close()

            print "Creating World Boxplot"
            plt.boxplot(regions_values)
            plt.xticks(range(1, len(regions_names)+1), regions_names, fontsize=6)
            plt.xlabel("Income")
            plt.savefig(str(self.year) + "_WORLD_boxplot.pdf")
            plt.close()
            print "Finish Plots. Year:" + str(self.year)

            return True
        except IOError as e:
            print "ERROR: IOError " + str(e)
            return False

