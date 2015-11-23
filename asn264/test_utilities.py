from unittest import TestCase
from assignment9 import *

countries, income = load_session()

class test_merge_by_year(TestCase):

	#Make sure invalid year (years that are not in the income df) are handled correctly
	#The same logic applies to the inc_by_year function so no need to test both
	def test_invalid_year(self):
		self.assertEqual(merge_by_year(countries, income, 2016), None)
