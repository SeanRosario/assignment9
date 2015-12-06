import unittest
from Income import *
import os


class TestIncome(unittest.TestCase):
    '''This test will test the Income class'''
    def setUp(self):
        pass

    def test_init(self):
        '''This function will test if the data was loaded successfully '''
        i = Income()
        self.assertTrue(i.countries.shape == (194, 1))
        self.assertTrue(i.merged.shape == (194, 1))
        self.assertTrue(i.income.shape == (213, 260))

    def test_plot(self):
        '''This function will test if plots from year 2007 to 2012 are generated successfully'''
        try:
            for i in range(2007,2013):
                os.remove('./Income_Box_'+str(i)+'.jpg')
                os.remove('./Income_Hist_'+str(i)+'.jpg')

        except OSError:
            pass
        i = Income()
        i.plot_2007_2012()
        for i in range(2007,2013):
            self.assertTrue(os.path.isfile('./Income_Box_'+str(i)+'.jpg'), "Fail to generate plot.")
            self.assertTrue(os.path.isfile('./Income_Hist_'+str(i)+'.jpg'), "Fail to generate plot.")

if __name__ == '__main__':
    unittest.main()
