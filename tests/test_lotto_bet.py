import unittest
from lotto.lotto_bet import Bet


class TestBet(unittest.TestCase):
    def setUp(self):
        self.bet_1 = Bet(3)
        self.bet_2 = Bet(5)

    def test_bet(self):
        self.assertRaises(ValueError, Bet, 0)
        self.assertRaises(ValueError, Bet, 6)
        self.assertRaises(ValueError, Bet, 'ambo')  # bet code must be passed as integer, not string

        self.assertEqual(self.bet_1.name, 'terno')
        self.assertNotEqual(self.bet_1.name, 'terna')  # misspelled
        self.assertEqual(self.bet_1.min_numbers, 3)
        self.assertEqual(self.bet_2.name, 'cinquina')
        self.assertNotEqual(self.bet_1.name, 'Cinquina')  # case sensitive, bet name is all lowercase
        self.assertEqual(self.bet_2.min_numbers, 5)

        # checking types of attributes
        self.assertIs(type(self.bet_1.name), str)
        self.assertIs(type(self.bet_1.min_numbers), int)

    def test_is_bet_valid(self):
        self.assertTrue(Bet.is_bet_valid(1))
        self.assertTrue(Bet.is_bet_valid(3))
        self.assertTrue(Bet.is_bet_valid('5'))
        self.assertFalse(Bet.is_bet_valid(0))
        self.assertFalse(Bet.is_bet_valid(6))
        self.assertFalse(Bet.is_bet_valid('ambo'))  # bet code gets checked, not string


if __name__ == '__main__':
    unittest.main()