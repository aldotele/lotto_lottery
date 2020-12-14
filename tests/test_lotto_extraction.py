import unittest
from lotto.lotto_extraction import Extraction


class TestExtraction(unittest.TestCase):
    def setUp(self):
        self.extraction_table = Extraction().all_extractions

    def test_extraction(self):
        self.assertIs(type(self.extraction_table), dict)
        # making sure each key in the extraction dictionary is a capitalized city
        self.assertIn('Roma', self.extraction_table)
        self.assertNotIn('roma', self.extraction_table)
        self.assertNotIn('ROMA', self.extraction_table)
        # making sure there is no extraction for Tutte
        self.assertNotIn('Tutte', self.extraction_table)
        # making sure numbers of a city extraction are stored in a list
        self.assertIs(type(self.extraction_table['Roma']), list)
        # making sure the extraction table always includes 10 cities/keys
        self.assertEqual(len(self.extraction_table), 10)
        # making sure the amount of extracted numbers in each city is always 5
        self.assertEqual(len(self.extraction_table['Roma']), 5)


if __name__ == '__main__':
    unittest.main()