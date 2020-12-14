from lotto.lotto_numbers import NumbersForTicket
from lotto.lotto_bet import Bet
from lotto.lotto_city import City
from lotto.lotto_money import Money


class Ticket:
    """
    represents a lotto ticket
    all parameters are instances of other classes: NumbersForTicket, BetType, City, Money
    @attr numbers is a NumbersForTicket object with a sequence of random numbers stored as an attribute
    @attr bet is a Bet object with a bet type stored as an attribute
    @attr city is a City object with a city name stored as an attribute
    @attr money is a Money object with an amount stored as an attribute
    """
    def __init__(self, numbers, bet, city, money):
        if not isinstance(numbers, NumbersForTicket):
            raise ValueError('a NumbersForTicket object must be passed as first argument.')
        if not isinstance(bet, Bet):
            raise ValueError('a Bet object must be passed as second argument.')
        if not isinstance(city, City):
            raise ValueError('a City object must be passed as third argument.')
        if not isinstance(money, Money):
            raise ValueError('a Money object must be passed as fourth argument.')

        if Ticket.is_ticket_valid(numbers, bet):
            self.numbers = numbers
            self.bet = bet
            self.city = city
            self.money = money
        else:
            raise ValueError('amount of numbers and bet type are not allowed together.')

    @staticmethod
    def is_ticket_valid(numbers, bet):
        """
        checks if amount of numbers and bet type are coherent and therefore allowed together:
        there is a minimum amount of numbers for each bet: 1 for ambata, 2 for ambo, 3 for terno, etc.
        :param numbers: object
        :param bet: object
        :return: boolean
        """
        if not isinstance(numbers, NumbersForTicket) or not isinstance(bet, Bet):
            raise ValueError('first two arguments must be a NumbersForTicket and a Bet object.')

        numbers_amount = len(numbers.sequence)
        minimum_numbers = bet.min_numbers
        if numbers_amount < minimum_numbers:
            return False

        return True










