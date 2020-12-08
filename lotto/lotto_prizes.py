from lotto.lotto_numbers import NumbersForTicket
from lotto.lotto_bet import Bet
from lotto.lotto_city import City
from lotto.lotto_ticket import Ticket
from lotto.lotto_money import Money


class Prizes:
    # the following dictionary shows the amounts of bet combinations for each amount of matching numbers
    # the index within the list is the bet_type (e.g. amount at index 1 refers to number of ambata)
    # e.g. for 5 extracted numbers, the player might win 5 ambata, 10 ambo, 10 terno, 5 quaterna and 1 cinquina
    # e.g. for 10 extracted numbers, the player might win 10 ambata, 45 ambo, 10 terno, 210 quaterna and 252 cinquina
    combinations = {1: [None, 1],
                    2: [None, 2, 1],
                    3: [None, 3, 3, 1],
                    4: [None, 4, 6, 4, 1],
                    5: [None, 5, 10, 10, 5, 1],
                    6: [None, 6, 15, 20, 15, 6],
                    7: [None, 7, 21, 35, 35, 21],
                    8: [None, 8, 28, 56, 70, 56],
                    9: [None, 9, 36, 84, 126, 126],
                    10: [None, 10, 45, 120, 210, 252]}

    # the following dictionary shows GROSS payout combinations. (NET payout = GROSS - 0.08*GROSS)
    # each key is the amount of placed numbers and the index within the list is the bet_type
    # e.g. doing an ambata with 1 placed number will pay €11.23
    # e.g. doing a cinquina with 5 placed numbers will lead to maximum win of € 6 million
    # e.g. doing an ambata with 10 placed numbers will lead to minimum win of € 1.12
    prizes_table = {1: [None, 11.23],
                    2: [None, 5.61, 250],
                    3: [None, 3.74, 83.33, 4500],
                    4: [None, 2.80, 41.66, 1125, 120000],
                    5: [None, 2.24, 25, 450, 24000, 6000000],
                    6: [None, 1.87, 16.66, 225, 8000, 1000000],
                    7: [None, 1.60, 11.90, 128.57, 3428.57, 285714.28],
                    8: [None, 1.40, 8.92, 80.35, 1714.28, 107142.85],
                    9: [None, 1.24, 6.94, 53.57, 952.38, 47619.04],
                    10: [None, 1.12, 5.55, 37.50, 571.42, 23809.52]}

    @staticmethod
    def compute_payout(ticket, winning_combinations):
        """
        :param ticket: is a Ticket object which resulted to have won
        :param winning_combinations: dictionary with cities as keys and list of matching numbers as values
        :return: the net win (post 8% taxes) of a winning ticket
        """
        # the net win will firstly depend on the amount of numbers that were placed
        amount_of_numbers = len(ticket.numbers.sequence)
        bet_code = ticket.bet.min_numbers
        money = ticket.money.amount
        gross_payout = 0
        for city in winning_combinations:
            base_prize = Prizes.prizes_table[amount_of_numbers][bet_code]
            matched = len(winning_combinations[city])
            mol_factor = Prizes.combinations[matched][bet_code]
            gross_payout += base_prize * mol_factor

        # if the bet was on "Tutte", payout gets divided by 10
        if ticket.city.name == 'Tutte':
            gross_payout = gross_payout / 10

        taxes = 0.08 * gross_payout
        net_payout = gross_payout - taxes
        net_win = net_payout * money

        if net_win > 6000000:
            net_win = 6000000

        return net_win


# TESTS
if __name__ == '__main__':
    # 8 numbers on terno Roma, 2€, 5 matching numbers
    ticket1 = Ticket(NumbersForTicket(8), Bet(3), City(8), Money(2))
    combs1 = {'Roma': [3, 19, 45, 66, 88]}
    print('ticket 1 prize: € {}'.format(Prizes.compute_payout(ticket1, combs1)))
    # 10 numbers on quaterna Napoli, 1€, 5 matching numbers
    ticket2 = Ticket(NumbersForTicket(10), Bet(4), City(6), Money(1))
    combs2 = {'Napoli': [7, 15, 66, 78, 90]}
    print('ticket 2 prize: € {}'.format(Prizes.compute_payout(ticket2, combs2)))
    # 4 numbers on ambo Torino, 2€, 3 matching numbers
    ticket3 = Ticket(NumbersForTicket(4), Bet(2), City(9), Money(2))
    combs3 = {'Torino': [15, 65, 72]}
    print('ticket 3 prize: € {}'.format(Prizes.compute_payout(ticket3, combs3)))
    # 10 numbers on ambata Tutte, 3€, 7 matching numbers
    ticket4 = Ticket(NumbersForTicket(10), Bet(1), City(11), Money(3))
    combs4 = {'Napoli': [3], 'Milano': [79], 'Roma': [55, 81], 'Firenze': [13, 46, 88]}
    print('ticket 4 prize: € {}'.format(Prizes.compute_payout(ticket4, combs4)))
    # 5 numbers on cinquina Bari, 1€, 5 matching numbers
    ticket5 = Ticket(NumbersForTicket(5), Bet(5), City(1), Money(1))
    combs5 = {'Napoli': [10, 21, 35, 66, 70]}
    print('ticket 5 prize: € {}'.format(Prizes.compute_payout(ticket5, combs5)))











