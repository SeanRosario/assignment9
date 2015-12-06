__author__ = 'Leo'

import unittest


class MyTestCase(unittest.TestCase):
    def raw_input(self):
        response = range(1800, 2013, 1)
        self.assertTrue(1999 in response)
        self.asertFalse(0000 in response)


if __name__ == '__main__':
    unittest.main()
