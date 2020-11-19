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
    @attr numbers will store the given amount of numbers, that can be chosen or be generated randomly
    """
    def __init__(self, amount, numbers=''):
        self.numbers = []
        if NumbersForTicket.validation(amount, numbers):
            if not numbers:
                # if numbers are not specified, the class will use an instance of FullRuota just to generate random numbers
                from_ruota = FullRuota()
                for i in range(amount):
                    self.numbers.append(from_ruota.numbers.pop())
            else:
                self.numbers += numbers
        else:
            return None

    @staticmethod
    def validation(amount, numbers=''):
        amount = int(amount)
        # making sure the amount of numbers to generate is between 1 and 10
        if amount < 1 or amount > 10:
            print('NOT VALID: amount of numbers must be between 1 and 10')
            return False

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
        

if __name__ == '__main__':
    NumbersForTicket(4, [34, 56])
    NumbersForTicket(2, [26, 77])