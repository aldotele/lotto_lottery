from lotto.lotto_numbers import NumbersForTicket
from lotto.lotto_bet import BetType
from lotto.lotto_city import City
from lotto.lotto_table_lib import print_lotto_bill
from lotto.lotto_ticket import Ticket


class LottoManager:
    """
    represents the business logic of the program
    @attr tickets is a list with a series of Ticket objects (even one only)
    """
    def __init__(self, tickets_amount):
        self.tickets = []
        for t in range(1, tickets_amount + 1):
            # the class will create as many Ticket instance as the specified amount
            # each Ticket instance is created by invoking a static method, and asking all ticket info to the user
            ticket = LottoManager.ticket_creator(t)
            self.tickets.append(ticket)


    @staticmethod
    def ticket_creator(t):
        print()
        print('TICKET {}'.format(t))

        amount = LottoManager.choose_amount()
        print()
        numbers = LottoManager.choose_numbers(amount)
        print()
        bet = LottoManager.choose_bet(amount, numbers)
        print()
        city = LottoManager.choose_city()
        print()

        # TICKET CREATION ATTEMPT
        ticket_to_confirm = Ticket(amount, bet, city)
        print()
        # checking confirmation: if ticket is confirmed, it is also created
        # otherwise the process will restart by asking again all ticket info 
        if LottoManager.ticket_confirmator(ticket_to_confirm, t):
            confirmed_ticket = ticket_to_confirm
            print('TICKET {} was created successfully!'.format(t))
            return confirmed_ticket
        else:
            # using recursion to restart the ticket creation. Note that the return is necessary
            return LottoManager.ticket_creator(t)  


    @staticmethod
    def choose_amount():
        amount = input('How many numbers? [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\nType here: ')
        while True:
            if NumbersForTicket.is_amount_valid(amount):
                amount = int(amount)
                break
            else:
                amount = input('How many numbers? [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\nType here: ')

        return amount


    @staticmethod
    def choose_numbers(amount):
        # the function is used to generate random sequences of numbers until the user chooses the one he likes
        print('generating your {} numbers ...'.format(amount))
        random_numbers = NumbersForTicket(amount).numbers
        while True:
            print('numbers: {}'.format(random_numbers))
            print()
            check_confirmation = input('Do you like the above numbers?\n1 - Confirm\n0 - Regenerate\nType here: ')
            if check_confirmation == '1':
                numbers = random_numbers
                break
            elif check_confirmation == '0':
                print()
                print('generating your {} numbers ...'.format(amount))
                random_numbers = NumbersForTicket(amount).numbers
            
        return numbers


    @staticmethod   
    def choose_bet(amount, numbers):
        # the program will automatically show the allowed bets based on the placed amount of numbers
        bet = input('Which bet? {}\nType here: '.format(BetType.all_bets[1:amount+1]))
        while True:
            # double validation check: the bet must be spelled correctly as well as be coherent with the amount of numbers
            if BetType.is_bet_valid(bet):
                if Ticket.check_coherence(amount, bet):
                    break
                else:
                    # if chosen bet is not coherent, the user will be informed and asked to retry
                    bet = input('Which bet? {}\nType here: '.format(BetType.all_bets[1:amount+1]))    
            # if chosen bet is not spelled correctly, the user will be informed and asked to retry              
            else:
                bet = input('Which bet? {}\nType here: '.format(BetType.all_bets[1:amount+1]))

        return bet


    @staticmethod
    def choose_city():
        city = input('Which city? {}\nType a city here: '.format(City.all_cities))
        while True:
            if City.is_city_valid(city):
                break
            else:
                city = input('Try again. Type a city here: ')

        return city


    @staticmethod
    def ticket_confirmator(ticket, t):
        """
        represents a summary of the chosen inputs for the current ticket
        it asks the user a confirmation by typing 1 
        otherwise the user can type 0 to restart the ticket
        """
        print('<<< Ticket {} info >>>:'.format(t))
        print('placed NUMBERS: {}'.format(ticket.numbers.numbers))
        print('BET type: {}'.format(ticket.bet_type.bet_type))
        print('CITY: {}'.format(ticket.city.city))

        while True:
            print()
            check_confirmation = input('Do you wish to CONFIRM ticket {}?\n1 - Confirm\n0 - Rewrite\nType here: '.format(t))
            if check_confirmation == '1':
                return True
            elif check_confirmation == '0':
                return False
      

    def bill_printer(self):
        """
        it builds and returns a dictionary with all tickets' info
        the dictionary will then be passed as argument of an imported function
        the function will print a visual representation of the bill, with all tickets (even a single one) gathered 
        such function is invoked in the __str__ method
        """
        bill_info = {'nums': [], 'bets': [], 'cities': []}

        for ticket in self.tickets:
            bill_info['nums'].append(ticket.numbers.numbers)
            bill_info['bets'].append(ticket.bet_type.bet_type)
            bill_info['cities'].append(ticket.city.city)

        return bill_info


    def __str__(self):
        d_print = self.bill_printer()
        print('Here is your bill ...')
        print_lotto_bill(d_print)
        return 'Good Luck :)' 


if __name__ == '__main__':
    n = int(input('how many tickets? '))
    mybill = LottoManager(n)
    print(mybill)
    
