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
    :param bet_code is by default 1 (ambata) but can be specified in order to differentiate allowed amounts
    @attr sequence will store the series of numbers in a list, and they are generated randomly
    """
    def __init__(self, amount, bet_code=1):
        self.sequence = []
        if NumbersForTicket.is_amount_valid(amount, bet_code):
            # numbers are randomly generated using a full ruota
            from_ruota = FullRuota()
            for i in range(amount):
                self.sequence.append(from_ruota.numbers.pop())
        else:
            return None

    @staticmethod
    def is_amount_valid(amount, bet_code=1):
        """
        validates the amount which may depend on the bet type (if specified)
        the amount can never be less than 1 or more than 10
        if a bet code is specified, the amount has to be at least equal to the bet code (e.g. 3 numbers for a terno)
        :param amount: the amount of numbers to place
        :param bet_code: if specified, it allows to validate the placed amount. By default is 1 (ambata)
        :return: boolean
        """
        if Bet.is_bet_valid(bet_code):
            try:
                amount = int(amount)
                if not bet_code <= amount <= 10:
                    return False
            except:
                return False

        return True

    @staticmethod
    def show_allowed_amounts(bet_code=1):
        """
        it displays a sequence of allowed amounts, which may depend on the bet type (when specified)
        :param bet_code: if specified, it differentiates the sequence of allowed amounts
        """
        if Bet.is_bet_valid(bet_code):
            for n in range(bet_code, 11):
                print(n, end='  ')
        else:
            print('NOT VALID: bet code must be between 1 (ambata) and 5 (cinquina).')


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




