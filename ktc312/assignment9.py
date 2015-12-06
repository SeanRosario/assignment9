__author__ = 'ktc312'

from dada_visualization import *

def main():
    while True:
        response = raw_input("Enter a year or 'finish': ")
        if response == 'quit':
            sys.exit()
        elif response == 'finish':
            for year in range(2007,2013,1):
                ploting = exploratory_tools(year)
                ploting.histogram()
                ploting.boxplot()
            break
        elif int(response)>=1800 and int(response)<=2012:
            plt.close('all')
            year = int(response)
            histogram(year, income)
        else:
            print 'Invalid year'



if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print 'Invalid inputs'
    except KeyboardInterrupt:
        print 'Quiting'
    except EOFError:
        print 'Quiting'