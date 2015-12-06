'''
Created on Nov 13, 2015

@author: Rafael Garcia (rgc292)
'''

import sys

'''This class is intended to validate user's input'''

class Validation(object):
    

    def __init__(self):
        pass
    
    #Check if user's input is in expected format 
    def validate_input(self, input):
        self.invalid = True
        self.exit = ""
        self.value = 0
        self.output = True
        
        #It iterates until input is valid 
        while self.invalid:
            
            try:
                self.value = int(input)
                if self.value in range(1800, 2013):
                    self.invalid = False
                    self.output = False 
                else:
                    break       
                
            except (ValueError, NameError, SyntaxError, TypeError, 
                                                        KeyboardInterrupt):
                self.exit = raw_input("\nWould you like to finish? (y,n) >>> ")
                
                if self.exit.lower() == "y":
                    print "Good bye!"
                    self.invalid == False
                    self.output = True
                    self.value = ''
                    return self.output, self.value
                    
                elif self.exit.lower() == "n":
                    print "Ok!"
                    break
                
                else:
                    break
            
            except (EOFError, SystemExit):
                print "Good Bye!"
                sys.exit(1)
          
        return self.output, self.value
        