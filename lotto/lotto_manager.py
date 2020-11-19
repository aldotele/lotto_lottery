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

        # AMOUNT OF NUMBERS TO PLACE
        amount = int(input('How many numbers? [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\nType here: '))
        while True:
            if NumbersForTicket.validation(amount):
                break
            else:
                amount = int(input('how many numbers? [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\nType here: '))
        
        print()

        # NUMBERS TO PLACE: it can be a random generation or a chosen sequence of numbers
        numbers = input('Which numbers? [Write a sequence of numbers (whitespace between them) or leave empty for random numbers]\
            \nType numbers or press ENTER for random numbers: ')
        while True:
            if numbers:
                numbers = numbers.split()
                for i in range(len(numbers)):
                    numbers[i] = int(numbers[i])
            if NumbersForTicket.validation(amount, numbers):
                break
            else:
                numbers = input('Try again your sequence or press ENTER for random numbers: ')

        print()

        # TYPE OF BET: the program will automatically show the allowed bets based on the amount of numbers
        bet = input('Which bet? {}\nType your bet here: '.format(BetType.all_bets[1:amount+1]))
        while True:
            # double validation check: the bet must be spelled correctly as well as coherent with the amount of numbers
            if BetType.is_bet_valid(bet):
                if Ticket.check_coherence(amount, bet, numbers):
                    break
                else:
                    # if chosen bet is not coherent, the user can retry or type zero to restart the ticket from scratch
                    choice = input('Enter an allowed bet or press 0 to restart ticket: ')
                    if choice == '0':
                        LottoManager.ticket_creator(t)
                        break
                    bet = choice                    
            else:
                bet = input('Try again. Type your bet here: ')

        print()

        # CITY 
        city = input('Which city? {}\nType a city here: '.format(City.all_cities))
        while True:
            if City.is_city_valid(city):
                break
            else:
                city = input('Allowed cities --> {}\nTry again. Type a city here: '.format(' '.join(City.all_cities)))
            
        print()

        # TICKET CREATION ATTEMPT
        ticket = Ticket(amount, bet, city, numbers)
        print()
        # checking confirmation: if ticket is confirmed, it is also created
        # otherwise the process will restart by asking again all ticket info 
        if LottoManager.ticket_confirmator(ticket, t):
            print('TICKET {} was created successfully!'.format(t))
            return ticket
        else:
            LottoManager.ticket_creator(t)  

    @staticmethod
    def ticket_confirmator(ticket, t):
        """
        represents a summary of the chosen inputs for the current ticket
        it asks the user a confirmation of the ticket by pressing ENTER
        otherwise the user can type 0 to restart the ticket
        """
        print('<<< Ticket {} info >>>:'.format(t))
        print('placed NUMBERS: {}'.format(ticket.numbers.numbers))
        print('BET type: {}'.format(ticket.bet_type.bet_type))
        print('CITY: {}'.format(ticket.city.city))

        print()
        check = input('Do you wish to CONFIRM?\npress ENTER to confirm or type 0 to rewrite ticket {}: '.format(t))
        if check != '0':
            return True
        else:
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

    print()
    
    for ticket in mybill.tickets:
        print(ticket)
