import random 


# ogni istanza di questa classe avrà come attributo una lista di numeri da 1 a 90, mischiati
# la classe può essere utilizzata per fare tutte le operazioni del gioco del lotto: generazione numeri biglietti ed estrazione


class fullRuota:
    def __init__(self):
        self.numbers = []
        for i in range(1, 91):
            self.numbers.append(i)
        random.shuffle(self.numbers)


class NumbersForTicket:
    def __init__(self, amount, numbers=''):
        self.numbers = []
        if self.validation(amount, numbers):
            if not numbers:
                from_ruota = fullRuota()
                for i in range(amount):
                    self.numbers.append(from_ruota.numbers.pop())
            else:
                self.numbers += numbers


    def validation(self, amount, numbers):
        if amount < 1 or amount > 10:
            raise ValueError('amount of numbers is not valid.\nPlease choose an amount between 1 and 10')
        
        if numbers != '' and len(numbers) != amount:
            if len(numbers) > amount:
                raise ValueError('amount of numbers placed for bet is too high')
            elif len(numbers) < amount:
                raise ValueError('amount of numbers placed for bet is too low')

        if numbers:
            i = 1
            for number in numbers:
                
                if number < 1 or number > 90:
                    raise ValueError('all placed numbers must be between 1 and 90')
                if number in numbers[i:]:
                    raise ValueError('all placed numbers must be unique')
                i += 1

        return True
        

if __name__ == '__main__':
    print(NumbersForTicket(4, [3, 5, 8, 77]).numbers)