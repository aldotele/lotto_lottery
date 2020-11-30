import random 

from lotto.lotto_bet import BetType

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
    represents the series of numbers inside a ticket
    @attr amount is the amount of numbers to place. It cannot be less than 1 or more than 10
    @attr bet_code is by default 1 (ambata) but can be specified in order to differentiate allowed amounts
    @attr numbers will store the given amount of numbers, which is generated randomly, but can also be specified
    """
    def __init__(self, amount, numbers='', bet_code=1):
        self.numbers = []
        if NumbersForTicket.is_amount_valid(amount, bet_code):
            # if numbers are not specified, they are randomly generated from a full ruota
            if not numbers:
                from_ruota = FullRuota()
                for i in range(amount):
                    self.numbers.append(from_ruota.numbers.pop())
            # otherwise the numbers will be the ones specified in the sequence
            else:
                self.numbers = numbers
        else:
            return None


    @staticmethod
    def is_amount_valid(amount, bet_code=1):
        """
        it validates the amount which may depend on the bet type (if specified)
        :param amount: the amount of numbers to place
        :param bet_code: if specified, it allows to validate the placed amount. By default is 1 (ambata)
        :return: boolean True or False
        """
        if BetType.is_bet_valid(bet_code):
            try:
                amount = int(amount)
                if not bet_code <= amount <= 10:
                    print('NOT VALID: You are allowed to place from {} to 10 numbers.'.format(bet_code))
                    return False
            except:
                print('NOT VALID: amount must be a number.')
                return False

        return True


    @staticmethod
    def show_allowed_amounts(bet_code=1):
        """
        it displays a sequence of allowed amounts, which may depend on the bet type (when specified)
        :param bet_code: if specified, it differentiates the sequence of allowed amounts
        """
        if BetType.is_bet_valid(bet_code):
            for n in range(bet_code, 11):
                print(n, end='  ')
        else:
            print('NOT VALID: bet code must be between 1 (ambata) and 5 (cinquina).')


class NumbersForExtraction:
    """
    represents 5 extracted numbers
    """      
    def __init__(self):
        self.numbers = []
        from_ruota = FullRuota()
        for i in range(5):
            self.numbers.append(from_ruota.numbers.pop())


if __name__ == '__main__':
    NumbersForTicket(amount=11)  # not valid amount
    NumbersForTicket(amount=3, bet_code=6)  # not valid bet code
    NumbersForTicket(amount=3, bet_code=4)  # not valid amount (3) for bet type (quaterna)
    NumbersForTicket(amount=5, bet_code=5)  # valid: 5 numbers placed for a cinquina

