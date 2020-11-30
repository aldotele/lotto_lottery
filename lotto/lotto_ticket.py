from lotto.lotto_numbers import NumbersForTicket
from lotto.lotto_bet import BetType
from lotto.lotto_city import City
from lotto.lotto_money import Money
from lotto.lotto_tables import print_ticket


class Ticket:
    """
    represents a lotto ticket
    @attr numbers is an object with a sequence of random (if not specified) numbers stored as an attribute
    @attr bet_type is an object with a bet type stored as an attribute
    @attr city is an object with a city store as an attribute
    """
    def __init__(self, numbers_amount, bet_type, city, money, numbers=''):
        if Ticket.check_coherence(numbers_amount, bet_type):
            # if a sequence of numbers is not specified, numbers are randomly generated
            self.numbers = NumbersForTicket(numbers_amount, numbers)
            self.bet_type = BetType(bet_type)
            self.city = City(city)
            self.money = Money(money)
        else:
            return None   


    @staticmethod
    def check_coherence(numbers_amount, bet_type):
        # case of incoherence between numbers_amount and bet_type
        # e.g. if the player places 3 numbers, he/she cannot bet on a "cinquina", which requires a minumum of 5 numbers  
        if numbers_amount < bet_type:      
            print('NOT VALID. The type of bet ({}) is not coherent with the amount of numbers ({}).'\
                .format(BetType.all_bets[bet_type], numbers_amount))

            return False        

        return True


 
if __name__ == '__main__':
    ticket = Ticket(numbers_amount=2, bet_type=3, city=9, money=1)  # not valid: 2 numbers and a terno bet
    ticket = Ticket(numbers_amount=7, bet_type=3, city=6, money=0)  # not valid amount of money
    ticket = Ticket(numbers_amount=7, bet_type=3, city=6, money=201)  # not valid amount of money
    ticket = Ticket(numbers_amount=7, bet_type=3, city=6, money=201)  # valid






