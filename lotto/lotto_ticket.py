from lotto.lotto_numbers import NumbersForTicket
from lotto.lotto_bet import Bet
from lotto.lotto_city import City
from lotto.lotto_money import Money
from lotto.lotto_tables import print_ticket


class Ticket:
    """
    represents a lotto ticket
    all parameters are instances of other classes: NumbersForTicket, BetType, City, Money
    @attr numbers is an object with a sequence of random (if not specified) numbers stored as an attribute
    @attr bet_type is an object with a bet type stored as an attribute
    @attr city is an object with a city store as an attribute
    """

    def __init__(self, numbers, bet, city, money):
        if Ticket.check_coherence(numbers, bet):
            self.numbers = numbers  # instance of NumbersForTicket
            self.bet = bet  # instance of Bet
            self.city = city  # instance of City
            self.money = money  # instance of Money
        else:
            return None

    @staticmethod
    def check_coherence(numbers, bet):
        # case of incoherence between numbers_amount and bet_type
        # e.g. if the player places 3 numbers, he/she cannot bet on a "cinquina", which requires a minumum of 5 numbers
        numbers_amount = len(numbers.sequence)
        minimum_numbers = bet.min_numbers
        if numbers_amount < minimum_numbers:
            #print('NOT VALID. The type of bet ({}) is not coherent with the amount of numbers ({}).'
                  #.format(BetType.all_bets[minimum_numbers], numbers_amount))

            return False

        return True


