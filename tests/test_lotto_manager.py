import unittest
from lotto.lotto_numbers import NumbersForTicket
from lotto.lotto_city import City
from lotto.lotto_bet import Bet
from lotto.lotto_money import Money
from lotto.lotto_ticket import Ticket
from lotto.lotto_extraction import Extraction
from lotto.lotto_manager import LottoManager


class TestLottoManager(unittest.TestCase):
    def setUp(self):
        # simulating a "fake" game in order to make sure the business logic of the program works
        self.ticket_1 = Ticket(NumbersForTicket(8), Bet(3), City(1), Money(2))  # 8 numbers - terno - Bari - €2
        self.ticket_1.numbers.sequence = [12, 27, 40, 75, 90, 20, 37, 56]

        self.ticket_2 = Ticket(NumbersForTicket(10), Bet(1), City(11), Money(3))  # 10 numbers - ambata - Tutte - €3
        self.ticket_2.numbers.sequence = [7, 19, 45, 66, 88, 20, 37, 56, 31, 70]

        self.ticket_3 = Ticket(NumbersForTicket(5), Bet(3), City(6), Money(1))  # 5 numbers - terno - Napoli - €1
        self.ticket_3.numbers.sequence = [8, 21, 37, 56, 79]

        self.ticket_4 = Ticket(NumbersForTicket(10), Bet(4), City(6), Money(1))
        self.ticket_4.numbers.sequence = [7, 2, 3, 4, 5, 21, 15, 18, 27, 33]

        # the lotto bill is filled with chosen tickets
        self.game_sample = LottoManager(3, [self.ticket_1, self.ticket_2, self.ticket_3])
        # faking an extraction
        self.game_sample.extraction.all_extractions = {'Bari': [12, 27, 40, 75, 90], 'Cagliari': [1, 2, 3, 4, 5],
                                       'Firenze': [88, 20, 37, 4, 5], 'Genova': [1, 2, 3, 4, 5],
                                       'Milano': [19, 2, 3, 4, 5], 'Napoli': [7, 2, 3, 4, 5],
                                       'Palermo': [1, 2, 3, 4, 5], 'Roma': [45, 66, 3, 4, 5],
                                       'Torino': [1, 2, 3, 4, 5], 'Venezia': [1, 2, 3, 4, 5]}

        self.ticket_1_checked = LottoManager.ticket_winning_combinations(self.ticket_1, self.game_sample.extraction)
        self.ticket_2_checked = LottoManager.ticket_winning_combinations(self.ticket_2, self.game_sample.extraction)
        self.ticket_3_checked = LottoManager.ticket_winning_combinations(self.ticket_3, self.game_sample.extraction)
        self.ticket_4_checked = LottoManager.ticket_winning_combinations(self.ticket_4, self.game_sample.extraction)

    def test_lotto_manager(self):
        self.assertEqual(len(self.game_sample.tickets), 3)
        self.assertIsInstance(self.game_sample.tickets[0], Ticket)
        self.assertIsInstance(self.game_sample.tickets[1], Ticket)
        self.assertIsInstance(self.game_sample.tickets[2], Ticket)
        self.assertIsInstance(self.game_sample.extraction, Extraction)

        # making sure the program returns error in case the stated amount of tickets does not match the actual quantity
        self.assertRaises(ValueError, LottoManager, 2, [self.ticket_1, self.ticket_2, self.ticket_3])
        self.assertRaises(ValueError, LottoManager, 4, [self.ticket_1, self.ticket_2, self.ticket_3])

    def test_ticket_winning_combinations(self):
        # making sure th first two tickets have winning combinations, while the third one not
        self.assertIsNotNone(self.ticket_1_checked.winning_combinations)
        self.assertIsNotNone(self.ticket_2_checked.winning_combinations)
        self.assertIsNone(self.ticket_3_checked.winning_combinations)

        # making sure the winning combinations of the first two tickets are returned as dictionaries
        self.assertIs(type(self.ticket_1_checked.winning_combinations), dict)
        self.assertIs(type(self.ticket_2_checked.winning_combinations), dict)

        # making sure the dictionaries of winning combinations for the first two tickets have the correct length
        self.assertEqual(len(self.ticket_1_checked.winning_combinations), 1)
        self.assertEqual(len(self.ticket_2_checked.winning_combinations), 4)

    def test_is_ticket_winning(self):
        # making sure the first two tickets result to have won, while the third one not
        self.assertTrue(LottoManager.is_ticket_winning(self.ticket_1_checked))
        self.assertTrue(LottoManager.is_ticket_winning(self.ticket_2_checked))
        self.assertFalse(LottoManager.is_ticket_winning(self.ticket_3_checked))

        self.assertRaises(ValueError, LottoManager.is_ticket_winning, 'ticket')
        # passing a ticket without checking winning combinations will raise an error
        self.assertRaises(ValueError, LottoManager.is_ticket_winning,
                          Ticket(NumbersForTicket(5), Bet(2), City(11), Money(1)))

    def test_compute_payout(self):
        self.assertAlmostEqual(LottoManager.compute_payout(self.ticket_1_checked), 1478.44)
        self.assertAlmostEqual(LottoManager.compute_payout(self.ticket_2_checked), 2.16)
        self.assertAlmostEqual(LottoManager.compute_payout(self.ticket_4_checked), 2628.53)

        # when passing a not winning ticket to compute a win, the method raises an error
        self.assertRaises(ValueError, LottoManager.compute_payout, self.ticket_3_checked)
        # an error is raised also when passing a new Ticket whose result was not checked yet
        self.assertRaises(ValueError, LottoManager.compute_payout,
                          Ticket(NumbersForTicket(5), Bet(2), City(11), Money(1)))



if __name__ == '__main__':
    unittest.main()