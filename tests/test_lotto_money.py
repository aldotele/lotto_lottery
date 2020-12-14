import unittest
from lotto.lotto_money import Money


class TestMoney(unittest.TestCase):
    def setUp(self):
        self.money_1 = Money(5)
        self.money_2 = Money(1.50)
        self.money_3 = Money('10.00')  # a string can be passed as long as it is a valid digit

    def test_money(self):
        self.assertEqual(self.money_1.amount, 5)
        # the amount is stored as floating number even if it was passed as integer
        self.assertIs(type(self.money_1.amount), float)
        self.assertEqual(self.money_2.amount, 1.50)
        self.assertEqual(self.money_3.amount, 10)

        self.assertRaises(ValueError, Money, 0)
        self.assertRaises(ValueError, Money, 201)
        self.assertRaises(ValueError, Money, '10,00')  # the comma does not work, dot is required
        self.assertRaises(ValueError, Money, '200.01')
        self.assertRaises(ValueError, Money, '€ 2')

    def test_is_amount_valid(self):
        self.assertTrue(Money.is_amount_valid(1))
        self.assertTrue(Money.is_amount_valid(200))
        self.assertTrue(Money.is_amount_valid('1'))
        self.assertTrue(Money.is_amount_valid('30.50'))
        self.assertFalse(Money.is_amount_valid('30,50'))
        self.assertTrue(Money.is_amount_valid(2.50))
        self.assertFalse(Money.is_amount_valid(200.01))
        self.assertFalse(Money.is_amount_valid(201))
        self.assertFalse(Money.is_amount_valid(0.50))
        self.assertFalse(Money.is_amount_valid('ten'))





