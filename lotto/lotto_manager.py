from lotto.lotto_numbers import NumbersForTicket
from lotto.lotto_bet import BetType
from lotto.lotto_city import City
from lotto.lotto_ticket import Ticket
from lotto.lotto_extraction import Extraction
from lotto.lotto_tables import print_ticket, print_extraction

from datetime import datetime


class LottoManager:
    """
    represents the business logic of the program
    @attr tickets is a list with a series of Ticket objects (even one only)
    @attr extraction is an extraction object
    """
    def __init__(self, tickets_amount):
        self.tickets = []
        for t in range(1, tickets_amount + 1):
            # the class will create as many Ticket instance as the specified amount
            # each Ticket instance is created by invoking a static method, and asking all ticket info to the user
            ticket = LottoManager.ticket_creator(t)
            self.tickets.append(ticket)
        #the object will have an extraction attribute with cities as keys and extraction numbers as values
        self.extraction = Extraction()


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
        ticket_to_confirm = Ticket(amount, bet, city, numbers)
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
                return random_numbers
                
            elif check_confirmation == '0':
                print()
                print('generating your {} numbers ...'.format(amount))
                random_numbers = NumbersForTicket(amount).numbers


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
      

    @staticmethod
    def print_tickets(bill_of_tickets):
        """
        it print a series of tickets one by one, or the only ticket if the bill includes one ticket only
        @param bill_of_tickets is a series of Ticket objects
        """
        ticket_number = 0

        for ticket in bill_of_tickets:
            ticket_number += 1
            print()
            # the imported function is invoked to print the ticket object
            print_ticket(ticket, ticket_number)
            print('Good Luck :)')


    @staticmethod      
    def check_extraction(extraction):
        """
        it displays the full extraction table
        @param extraction has to be an extraction object, with an extraction dictionary as attribute
        """
        date = str(datetime.today()).split()[0]
        print('Extraction of {}'.format(date))
        # when printing the extraction object, its __str__ method will be invoked (check Extraction class in its own module)
        print(extraction)

    
    @staticmethod
    def is_ticket_winning(ticket, extraction):
        """
        it checks if a single ticket object resulted to have won
        @param ticket is a Ticket object
        @param extraction is an Extraction object
        """
        city = ticket.city.city
        ticket_numbers = ticket.numbers.numbers
        matching_numbers = 0

        if city != 'Tutte':
            city_extraction = extraction.extraction[city]
            for number in ticket_numbers:
                if number in city_extraction:
                    matching_numbers += 1
            # each bet type has a minimum numbers to play, which is also the minimum numbers to match in order to win
            if matching_numbers < ticket.bet_type.min_numbers:
                return False
            else:
                return True
        else:
            for city_extraction in extraction.extraction:
                for number in ticket_numbers:
                    if number in extraction.extraction[city_extraction]:
                        matching_numbers += 1
                if matching_numbers < ticket.bet_type.min_numbers:
                    matching_numbers = 0
                else: 
                    return True
            

 
    def check_results(self):
        """
        this method will check each ticket's result within the bill of tickets of the LottoManager object
        """
        ticket_number = 0

        for ticket in self.tickets:
            ticket_number += 1
            print_ticket(ticket, ticket_number)
            if ticket.city.city != 'Tutte':
                print('{} extraction'.format(ticket.city.city), end=' ')
                print(self.extraction.extraction[ticket.city.city])
            print()
            if LottoManager.is_ticket_winning(ticket, self.extraction):
                print('Congratulations: YOU WON !')
            else:
                print('YOU LOST :(')
            print()


    def __str__(self):
        LottoManager.print_tickets(self.tickets)
        print()
        extraction_button = input('press ENTER to check extraction')
        print()
        LottoManager.check_extraction(self.extraction)
        print()
        results_button = input('press ENTER to check results')
        print()
        self.check_results()
        return ''

    
if __name__ == '__main__':
    lotto_game = LottoManager(3)
    print(lotto_game)

