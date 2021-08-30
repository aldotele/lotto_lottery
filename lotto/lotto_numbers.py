import random 

from lotto.lotto_bet import Bet


class FullRuota:
    """
    represents a starting "Ruota" with all numbers 1-90
    it can be used both to generate random numbers for tickets and for the official 5-numbers extraction
    @attr numbers contains all numbers (shuffled)
    """
    def __init__(self):
        self.numbers = []
        for i in range(1, 91):
            self.numbers.append(i)
        random.shuffle(self.numbers)


class NumbersForTicket:
    """
    represents the sequence of numbers inside a ticket
    :param amount is the amount of numbers to place. It cannot be less than 1 or more than 10
    :param bet is a Bet object which is passed by default 1 (ambata)
    @attr sequence will store the series of numbers in a list, and they are generated randomly
    """
    def __init__(self, amount, bet=Bet(1)):
        self.sequence = []
        if NumbersForTicket.is_amount_valid(amount, bet):
            # numbers are randomly generated using a full ruota
            from_ruota = FullRuota()
            for i in range(int(amount)):
                self.sequence.append(from_ruota.numbers.pop())
        else:
            raise ValueError('amount of numbers to generate is not valid.')

    @staticmethod
    def is_amount_valid(amount, bet=Bet(1)):
        """
        validates the amount and validaton may depend on the bet object (if specified):
        the amount can never be less than 1 or more than 10, but
        if a bet object is passed, the amount has to be at least equal to its bet code (e.g. 3 numbers for a terno)
        :param amount: integer representing the amount of numbers to place
        :param bet: An object which allows to validate the placed amount. By default is passed code 1 (ambata)
        :return: boolean
        """
        if not isinstance(bet, Bet):
            raise ValueError('a valid Bet object must be passed.')

        try:
            amount = int(amount)
            if not bet.min_numbers <= amount <= 10:
                return False
        except:
            return False

        return True

    @staticmethod
    def show_allowed_amounts(bet=Bet(1)):
        """
        it displays a sequence of allowed amounts, which may depend on the bet type (when specified)
        if bet object is not specified, it is passed 1 by default, then the sequence will always be 1 to 10
        :param bet: if specified, it customizes the sequence of allowed amounts. By default is passed code 1 (ambata)
        """
        if not isinstance(bet, Bet):
            raise ValueError('argument must be a valid Bet object')

        for n in range(bet.min_numbers, 11):
            print(n, end='  ')

    @staticmethod
    def get_allowed_amounts(bet=Bet(1)):
        if not isinstance(bet, Bet):
            raise ValueError('argument must be a valid Bet object')
        amounts = []
        for n in range(bet.min_numbers, 11):
            amounts.append(str(n))
        return amounts


class NumbersForExtraction:
    """
    represents 5 extracted numbers
    @attr sequence will store in a list the 5 extracted numbers
    """      
    def __init__(self):
        self.sequence = []
        from_ruota = FullRuota()
        for i in range(5):
            self.sequence.append(from_ruota.numbers.pop())





