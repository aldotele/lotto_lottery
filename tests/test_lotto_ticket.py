import unittest
from lotto.lotto_numbers import NumbersForTicket
from lotto.lotto_city import City
from lotto.lotto_bet import Bet
from lotto.lotto_money import Money
from lotto.lotto_ticket import Ticket


class TestTicket(unittest.TestCase):
    def setUp(self):
        self.ticket_1 = Ticket(NumbersForTicket(8), Bet(2), City(6), Money(2))

    def test_ticket(self):
        # checking that each attribute of Ticket is an object itself
        self.assertIsInstance(self.ticket_1.numbers, NumbersForTicket)
        self.assertIsInstance(self.ticket_1.bet, Bet)
        self.assertIsInstance(self.ticket_1.city, City)
        self.assertIsInstance(self.ticket_1.money, Money)

        # making sure an error is raised when wrong arguments are passed to Ticket
        self.assertRaises(ValueError, Ticket, 8, 2, 6, 2)
        self.assertRaises(ValueError, Ticket, 8, 'ambo', 'Napoli', 2)
        # the followings raise an error because the amount of numbers is not enough for the bet type
        self.assertRaises(ValueError, Ticket, NumbersForTicket(3), Bet(5), City(11), Money(2))
        self.assertRaises(ValueError, Ticket, NumbersForTicket(1), Bet(2), City(11), Money(2))

        # checking types
        self.assertIs(type(self.ticket_1.numbers.sequence), list)
        self.assertIs(type(self.ticket_1.bet.name), str)
        self.assertIs(type(self.ticket_1.bet.min_numbers), int)
        self.assertIs(type(self.ticket_1.city.name), str)
        self.assertIs(type(self.ticket_1.money.amount), float)

        # checking that the attributes of the Ticket correspond to what expected
        self.assertEqual(len(self.ticket_1.numbers.sequence), 8)
        self.assertEqual(self.ticket_1.bet.name, 'ambo')
        self.assertEqual(self.ticket_1.bet.min_numbers, 2)
        self.assertNotEqual(self.ticket_1.bet.name, 'Ambo')
        self.assertEqual(self.ticket_1.city.name, 'Napoli')
        self.assertNotEqual(self.ticket_1.city.name, 'napoli')
        self.assertEqual(self.ticket_1.money.amount, 2.00)
        self.assertEqual(self.ticket_1.money.amount, 2)

    def test_is_ticket_valid(self):
        self.assertTrue(Ticket.is_ticket_valid(NumbersForTicket(3), Bet(1)))
        self.assertTrue(Ticket.is_ticket_valid(NumbersForTicket(3), Bet('2')))
        self.assertTrue(Ticket.is_ticket_valid(NumbersForTicket(3), Bet(3)))
        self.assertFalse(Ticket.is_ticket_valid(NumbersForTicket(3), Bet(4)))  # quaterna bet needs at least 4 numbers

        # making sure the method raises an error if wrong arguments are passed
        self.assertRaises(ValueError, Ticket.is_ticket_valid, 5, 2)
        self.assertRaises(ValueError, Ticket.is_ticket_valid, 5, 'ambo')
        self.assertRaises(ValueError, Ticket.is_ticket_valid, Bet(5), NumbersForTicket(10))  # arguments are inverted


if __name__ == '__main__':
    unittest.main()




