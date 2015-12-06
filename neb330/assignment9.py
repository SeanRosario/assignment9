from LoadData import *
from Explore import *

'''Author: Nora Barry (neb330). Also collaborated with Michael Higgins.'''

def main():

    for i in range(2007, 2013):
        instance = Explore(i)
        instance.generate_box()
        instance.generate_hist()
       
    while(1):
        year = raw_input("Enter a year between 1800 and 2012: ")
        if year == 'finish':
            exit()    
        try:
            year = int(year)
        except ValueError:
            print 'Please enter a valid year.'
            continue
        except (KeyboardInterrupt, EOFError):
            continue
        else:
            if year < 1800 or year > 2012:
                print 'Please enter a year in the listed interval.'
                continue
            else:
                income_by_year(year)
        
    
                
if __name__ == "__main__":
    main()         
                
        
