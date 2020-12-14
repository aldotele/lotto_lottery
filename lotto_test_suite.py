import unittest
from tests.test_lotto_numbers import TestNumbersForTicket, TestNumbersForExtraction, TestFullRuota
from tests.test_lotto_bet import TestBet
from tests.test_lotto_city import TestCity
from tests.test_lotto_money import TestMoney
from tests.test_lotto_ticket import TestTicket
from tests.test_lotto_extraction import TestExtraction
from tests.test_lotto_manager import TestLottoManager


def suite():
    suite = unittest.TestSuite()

    suite.addTest(TestNumbersForTicket('test_ticket_numbers'))
    suite.addTest(TestNumbersForTicket('test_is_amount_valid'))
    suite.addTest(TestFullRuota('test_full_ruota'))
    suite.addTest(TestNumbersForExtraction('test_extraction_sequence'))
    suite.addTest(TestBet('test_bet'))
    suite.addTest(TestBet('test_is_bet_valid'))
    suite.addTest(TestCity('test_city'))
    suite.addTest(TestCity('test_is_city_valid'))
    suite.addTest(TestMoney('test_money'))
    suite.addTest(TestMoney('test_is_amount_valid'))
    suite.addTest(TestTicket('test_ticket'))
    suite.addTest(TestTicket('test_is_ticket_valid'))
    suite.addTest(TestExtraction('test_extraction'))
    suite.addTest(TestLottoManager('test_lotto_manager'))
    suite.addTest(TestLottoManager('test_ticket_winning_combinations'))
    suite.addTest(TestLottoManager('test_is_ticket_winning'))
    suite.addTest(TestLottoManager('test_compute_payout'))

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())


