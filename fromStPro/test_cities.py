import unittest
from city_functions import city_country

#print(city_country('chengdu','china'))

class CityCountryTestCase(unittest.TestCase):
	'''测试city_functions.py'''
	def test_city_country(self):
		'''是否能够正确处理 Santiago,Chile这样的城市'''
		formatted_city_name = city_country('santiago','Chile')
		self.assertEqual(formatted_city_name,'Santiago,Chile')
	
	def test_city_country_population(self):
		'''是否能够正确处理 Santiago,Chile-population 5000000这样的字符串'''
		formatted_city_name = city_country('santiago','Chile','500000')
		self.assertEqual(formatted_city_name,'Santiago,Chile - 500000')
	
unittest.main()
