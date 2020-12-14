import unittest
import random
from lotto.lotto_bet import Bet
from lotto.lotto_numbers import NumbersForTicket
from lotto.lotto_numbers import NumbersForExtraction
from lotto.lotto_numbers import FullRuota


class TestNumbersForTicket(unittest.TestCase):
    def setUp(self):
        self.numbers_1 = NumbersForTicket(10)
        self.numbers_2 = NumbersForTicket(1)

    def test_ticket_numbers(self):
        self.assertEqual(len(self.numbers_1.sequence), 10)
        self.assertEqual(len(self.numbers_2.sequence), 1)

        self.assertRaises(ValueError, NumbersForTicket, 0)
        self.assertRaises(ValueError, NumbersForTicket, 11)
        self.assertRaises(ValueError, NumbersForTicket, 'six')
        self.assertRaises(ValueError, NumbersForTicket, 4, Bet(5))  # 4 numbers are not enough for a cinquina
        self.assertRaises(ValueError, NumbersForTicket, 4, 4)  # second argument must be Bet object

    def test_is_amount_valid(self):
        self.assertTrue(NumbersForTicket.is_amount_valid(10))
        self.assertTrue(NumbersForTicket.is_amount_valid('10'))
        self.assertTrue(NumbersForTicket.is_amount_valid(1))
        self.assertTrue(NumbersForTicket.is_amount_valid('1'))
        self.assertTrue(NumbersForTicket.is_amount_valid('6', Bet(5)))  # amount is enough for a cinquina (bet_code 5)
        self.assertFalse(NumbersForTicket.is_amount_valid(0))
        self.assertFalse(NumbersForTicket.is_amount_valid(11))
        self.assertFalse(NumbersForTicket.is_amount_valid('ten'))  # integer must be passed, not string
        self.assertFalse(NumbersForTicket.is_amount_valid(3, Bet(4)))  # 3 numbers are not enough for a quaterna

        self.assertRaises(ValueError, NumbersForTicket.is_amount_valid, 5, 1)  # second argument must be Bet object
        self.assertRaises(ValueError, NumbersForTicket.is_amount_valid, 5, 'ambo')  # second argument must be Bet object


class TestFullRuota(unittest.TestCase):
    def setUp(self):
        self.full_ruota = FullRuota()

    def test_full_ruota(self):
        self.assertEqual(len(self.full_ruota.numbers), 90)  # numbers before extraction are always 90
        # making sure a random integer between 1 and 90 is always in a full ruota before extraction
        self.assertIn(random.randint(1, 90), self.full_ruota.numbers)


class TestNumbersForExtraction(unittest.TestCase):
    def setUp(self):
        self.extraction = NumbersForExtraction()

    def test_extraction_sequence(self):
        self.assertEqual(len(self.extraction.sequence), 5)  # numbers in single extraction are always 5
        # making sure a random number of one extraction is always between 1 and 90
        self.assertIn(random.choice(self.extraction.sequence), FullRuota().numbers)


if __name__ == '__main__':
    unittest.main()



