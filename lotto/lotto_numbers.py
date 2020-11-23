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
    def __init__(self, amount):
        self.numbers = []
        if NumbersForTicket.is_amount_valid(amount):
            from_ruota = FullRuota()
            for i in range(amount):
                self.numbers.append(from_ruota.numbers.pop())
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


    # ---- TO IMPLEMENT FOR WHEN CHOOSING OWN NUMBERS
    """
    @staticmethod
    def validation(amount, numbers=''):
        # making sure that the amount of chosen numbers corresponds to the previously stated amount    
        if numbers != '' and len(numbers) != amount:
            if len(numbers) > amount:
                print('NOT VALID: amount of numbers placed for bet is too high')
                return False
            elif len(numbers) < amount:
                print('NOT VALID: amount of numbers placed for bet is too low')
                return False

        # making sure that each number in the chosen sequence is both unique (no repetitions) and in range 1-90 
        if numbers:
            i = 1
            for number in numbers:
                
                if number < 1 or number > 90:
                    print('NOT VALID: all placed numbers must be between 1 and 90')
                    return False
                if number in numbers[i:]:
                    print('NOT VALID: all placed numbers must be unique')
                    return False

                i += 1
    
        return True
        """
        

if __name__ == '__main__':
    NumbersForTicket.is_amount_valid(4) # valid
    NumbersForTicket.is_amount_valid('4') # valid
    NumbersForTicket.is_amount_valid('quattro') # not valid
    NumbersForTicket.is_amount_valid(-2) # not valid
    NumbersForTicket.is_amount_valid(11) # not valid