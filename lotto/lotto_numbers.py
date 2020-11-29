import random 


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
    @attr numbers will store the given amount of numbers, which is generated randomly
    """
    def __init__(self, amount, numbers=''):
        self.numbers = []
        if NumbersForTicket.is_amount_valid(amount):
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
    def is_amount_valid(amount):
        try:
            amount = int(amount)
            if not 1 <= amount <= 10:
                print('NOT VALID: amount must be between 1 and 10.')
                return False
        except:
            print('NOT VALID: amount must be a number.')
            return False

        return True


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
    NumbersForTicket.is_amount_valid(4) # valid
    NumbersForTicket.is_amount_valid('4') # valid
    NumbersForTicket.is_amount_valid('quattro') # not valid
    NumbersForTicket.is_amount_valid(-2) # not valid
    NumbersForTicket.is_amount_valid(11) # not valid
    print()
    print(NumbersForExtraction().numbers)

    print(NumbersForTicket(3, [3, 8, 9]).numbers)