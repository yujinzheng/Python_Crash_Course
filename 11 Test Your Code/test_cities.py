#coding=utf-8

import unittest
from city_functions import formatted_city

class CitiesTestCase(unittest.TestCase):
    '''测试city_funciton.py'''

    def test_city_country(self):
        '''能够正确处理输入城市和国家的数据'''
        formatted_name = formatted_city("Santiago", "Chile")
        self.assertEqual(formatted_name, "Santiago, Chile")

    def test_city_country_population(self):
        '''能够处理输入有人口的情况'''
        formatted_name= formatted_city("Santiago", "Chile", "5000000")
        self.assertEqual(formatted_name, "Santiago, Chile - population 5000000")



unittest.main()
