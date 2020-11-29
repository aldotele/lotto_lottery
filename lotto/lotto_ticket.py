from lotto.lotto_numbers import NumbersForTicket
from lotto.lotto_bet import BetType
from lotto.lotto_city import City
from lotto.lotto_tables import print_ticket


class Ticket:
    """
    represents a lotto ticket
    @attr numbers is an object with a sequence of random (if not specified) numbers stored as an attribute
    @attr bet_type is an object with a bet type stored as an attribute
    @attr city is an object with a city store as an attribute
    """
    def __init__(self, numbers_amount, bet_type, city, numbers=''):
        if Ticket.check_coherence(numbers_amount, bet_type):
            # if a sequence of chosen numbers is passed, that will be the sequence, otherwise numbers are randomly generated
            self.numbers = NumbersForTicket(numbers_amount, numbers)
            self.bet_type = BetType(bet_type)
            self.city = City(city)
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
    ticket = Ticket(2, 3, 9)
    try:
        print(ticket.numbers.numbers, ticket.city.city, ticket.bet_type.bet_type)
    except:
        pass

