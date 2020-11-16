from lotto_bet import BetType
from lotto_city import City
from lotto_numbers import NumbersForTicket
from lotto_table_lib import print_lotto_bill




class Ticket:
    def __init__(self, numbers_amount, bet_type, city, chosen_numbers = ''):
        self.numbers = NumbersForTicket(numbers_amount, chosen_numbers)
        self.bet_type = BetType(bet_type)
        self.city = City(city)
        
    """
    def is_ticket_valid(self, numbers_amount, chosen_numbers):
        # case of difference between allowed amount of numbers and placed amount of numbers
        if chosen_numbers != '' and len(chosen_numbers) != numbers_amount:
            if len(chosen_numbers) > numbers_amount:
                raise ValueError('amount of numbers placed for bet is too high')
            elif len(chosen_numbers) < numbers_amount:
                raise ValueError('amount of numbers placed for bet is too low')
    """   


    def ticket_printer(self):
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
    try:
        ticket1 = Ticket(5, 'terno', 'MILANO', [-1, 18, 77, 17, 90])
        print(ticket1)
    except:
        print('error')
    








"""
    ticket2 = Ticket(10, 'cinquina', ' NAPOLI   ')
    print(ticket1, end='')
    print(ticket2)
"""

