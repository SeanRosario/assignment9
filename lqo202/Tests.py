import unittest
from unittest import  TestCase
import DescriptiveAnalysisTool as DAT
import InitialCharge as IC
import  pandas as pd
__author__ = 'lqo202'


class TestAssigment9(TestCase):

    def testValidateClassDefinition(self):
        #Values to test
        erroanswers = ['1999', '2009', 'a' , 1600]
        noerroranswers = [1999,2009, 1801]

        #Validating that two different values do not give same result in the class
        for value in range(len(noerroranswers)-1):
             self.assertNotEqual(DAT.DescriptiveAnalysisTool(noerroranswers[value]), DAT.DescriptiveAnalysisTool(noerroranswers[value+1]))

        #Validating that the error values raise the expcetion
        for value in erroanswers:
            self.assertRaises(DAT.DescriptiveException, DAT.DescriptiveAnalysisTool, value)

        #Validating that the error values raise the expcetion
        for value in noerroranswers:
            self.assertTrue(DAT.DescriptiveAnalysisTool(value))

    def testValidateBaseCountries(self):
        errorfile='abcd'
        self.assertRaises(IOError, IC.UtilsFunctions.getDataCountries, errorfile)


    def testValidateBaseIncome(self):
        errorfile='abcd'
        self.assertRaises(IOError, IC.UtilsFunctions.getDataIncome, errorfile)
















if __name__ == '__main__':
    unittest.main()

