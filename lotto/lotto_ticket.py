from lotto.lotto_numbers import NumbersForTicket
from lotto.lotto_bet import BetType
from lotto.lotto_city import City
from lotto.lotto_table_lib import print_lotto_bill


class Ticket:
    """
    represents a lotto ticket
    @attr numbers is an object with a sequence of random numbers stored as an attribute
    @attr bet_type is an object with a bet type stored as an attribute
    @attr city is an object with a city store as an attribute
    """
    def __init__(self, numbers_amount, bet_type, city):
        if Ticket.check_coherence(numbers_amount, bet_type):
            self.numbers = NumbersForTicket(numbers_amount)
            self.bet_type = BetType(bet_type)
            self.city = City(city)
        else:
            return None   


    @staticmethod
    def check_coherence(numbers_amount, bet_type):
        # case of incoherence between numbers_amount and bet_type
        # e.g. if the player places 3 numbers, he/she cannot bet on a "cinquina", which requires a minumum of 5 numbers
        bet_check = bet_type.strip().lower()     
        if bet_check in BetType.all_bets:
            min_of_numbers = BetType.all_bets.index(bet_check)     
            if numbers_amount < min_of_numbers:      
                print('NOT VALID. The type of bet ({}) is not coherent with the amount of numbers ({}).'.format(bet_type, numbers_amount))

                return False        

        return True



if __name__ == '__main__':
    ticket1 = Ticket(3, 'terno', 'MILANO')
    ticket2 = Ticket(1, 'ambo', ' NAPOLI   ')
    


