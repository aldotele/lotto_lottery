import unittest
from lotto.lotto_city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city_1 = City(3)
        self.city_2 = City(11)

    def test_city(self):
        self.assertRaises(ValueError, City, 0)
        self.assertRaises(ValueError, City, 12)
        self.assertRaises(ValueError, City, 'Roma')

        self.assertEqual(self.city_2.name, 'Tutte')
        self.assertNotEqual(self.city_2.name, 'tutte')  # case sensitive
        self.assertEqual(self.city_1.name, 'Firenze')
        self.assertNotEqual(self.city_1.name, 'FIRENZE')  # case sensitive

    def test_is_city_valid(self):
        self.assertTrue(City.is_city_valid(1))
        self.assertTrue(City.is_city_valid('1'))
        self.assertTrue(City.is_city_valid(11))
        self.assertFalse(City.is_city_valid(0))
        self.assertFalse(City.is_city_valid(12))
        self.assertFalse(City.is_city_valid('Roma'))  # the city code gets validated, not the string


if __name__ == '__main__':
    unittest.main()
