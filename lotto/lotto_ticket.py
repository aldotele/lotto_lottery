from lotto.lotto_numbers import NumbersForTicket
from lotto.lotto_bet import BetType
from lotto.lotto_city import City
from lotto.lotto_table_lib import print_lotto_bill


class Ticket:
    """
    represents a lotto ticket
    @attr numbers is an object with a sequence of chosen/random numbers stored as an attribute
    @attr bet_type is an object with a bet type stored as an attribute
    @attr city is an object with a city store as an attribute
    """
    def __init__(self, numbers_amount, bet_type, city, chosen_numbers=''):
        if Ticket.check_coherence(numbers_amount, bet_type, chosen_numbers):
            self.numbers = NumbersForTicket(numbers_amount, chosen_numbers)
            self.bet_type = BetType(bet_type)
            self.city = City(city)
        else:
            return None   

    @staticmethod
    # the method checks two possible types of "incoherence" inside the ticket info
    def check_coherence(numbers_amount, bet_type, chosen_numbers=''):

        # case 1: incoherence between stated amount of numbers and placed amount of numbers
        # e.g. if the player decides to bet on 5 numbers, he/she cannot enter a sequence of 6 numbers
        if chosen_numbers != '' and len(chosen_numbers) != numbers_amount:
            if len(chosen_numbers) > numbers_amount:
                print('amount of numbers placed for bet is too high')
                return False
            if len(chosen_numbers) < numbers_amount:
                print('amount of numbers placed for bet is too low')  
                return False

        # case 2: incoherence between numbers_amount and bet_type
        # e.g. if the player places 3 numbers, he/she cannot bet on a "cinquina", which requires a minumum of 5 numbers
        bet_check = bet_type.strip().lower()     
        if bet_check in BetType.all_bets:
            min_of_numbers = BetType.all_bets.index(bet_check)     
            if numbers_amount < min_of_numbers:      
                print('amount of numbers is not coherent with type of bet.\nAllowed bets: {}'.format(BetType.all_bets[1:numbers_amount+1]))
                return False        

        return True


    def ticket_printer(self):
        """
        it builds and returns a dictionary with all ticket info
        the dictionary will then be passed as argument of an imported function 
        the function will print a visual representation of the ticket 
        such function is invoked through the __str__ method
        """
        ticket_info = {'nums': [], 'bets': [], 'cities': []}

        ticket_info['nums'].append(self.numbers.numbers)
        ticket_info['bets'].append(self.bet_type.bet_type)


        if self.city.city == 'Roma':
            ticket_info['cities'].append('RM')
        else:
            ticket_info['cities'].append(self.city.city[:2].upper())
        return ticket_info


    def __str__(self):
        d_print = self.ticket_printer()
        print_lotto_bill(d_print)
        return ''


if __name__ == '__main__':
    ticket1 = Ticket(3, 'terno', 'MILANO')
    #print(ticket1)

    ticket2 = Ticket(1, 'ambo', ' NAPOLI   ')
    #print(ticket2)


