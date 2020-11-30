from lotto.lotto_numbers import NumbersForTicket
from lotto.lotto_bet import BetType
from lotto.lotto_city import City
from lotto.lotto_ticket import Ticket
from lotto.lotto_extraction import Extraction
from lotto.lotto_money import Money
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
        print('--- TICKET {} ---'.format(t))
        print()

        bet = LottoManager.choose_bet()
        print()
        city = LottoManager.choose_city()
        print()
        # the amount of numbers that a player can place will depend on the chosen bet
        amount = LottoManager.choose_amount(bet)    
        print()
        numbers = LottoManager.choose_numbers(amount)
        print()
        money = LottoManager.choose_money()
    
        # TICKET CREATION ATTEMPT
        ticket_to_confirm = Ticket(amount, bet, city, money, numbers)
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
    def choose_bet():
        print('*** BET CHOICE ***')
        print()
        BetType.print_allowed_bets()
        bet = input('\nEnter a number: ')
        while True:
            try:
                bet = int(bet)
                if 1 <= bet <= 5:
                    break
                else:
                    print('NOT VALID. Enter a number between 1 and 5.')
                    bet = input('Try again: ')       
            except:
                print('NOT VALID. Enter the number associated to the bet type.')
                bet = input('Try again: ')

        return bet

    
    @staticmethod
    def choose_city():
        print('*** CITY CHOICE ***')
        print()
        for key in City.all_cities:
            print('{} : {}'.format(key, City.all_cities[key]))
        
        city = input('\nEnter a number: ')
        while True:
            try:
                city = int(city)
                if 1 <= city <= 11:
                    break
                else:
                    print('NOT VALID. Enter a number between 1 and 11.')
                    city = input('Try again: ')
            except:
                print('NOT VALID. Enter the number associated to the city.')
                city = input('Try again: ')

        return city


    @staticmethod
    def choose_amount(bet):
        print('*** NUMBERS CHOICE ***')
        print()
        print('Choose an amount of numbers to place:')
        for n in range(bet, 11):
            print(n, end='  ')
        print()
        amount = input('\nHow many numbers? ')

        while True:
            try:
                amount = int(amount)
                if bet <= amount <= 10:
                    break
                else:
                    print('NOT VALID. Enter an amount of numbers between {} and 10.'.format(bet))
                    amount = input('How many numbers? ')
            except:
                print('NOT VALID. Enter an amount of numbers between {} and 10.'.format(bet))
                amount = input('How many numbers? ')

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
    def choose_money():
        print('*** MONEY CHOICE ***')
        amount = input('money bet: ')
        while True:
            if Money.is_amount_valid(amount):
                amount = int(amount)
                return amount
            else:
                amount = input('money bet: ')


    @staticmethod
    def ticket_confirmator(ticket, t):
        """
        represents a summary of the chosen inputs for the current ticket
        it asks the user a confirmation by typing 1 
        otherwise the user can type 0 to restart the ticket
        """
        print('<<< Ticket {} summary >>>:'.format(t))
        print('placed NUMBERS: {}'.format(ticket.numbers.numbers))
        print('BET type: {}'.format(ticket.bet_type.bet_type))
        print('CITY: {}'.format(ticket.city.city))
        print('MONEY bet: € {}'.format(ticket.money.amount))

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
        it prints a series of tickets one by one, or the only ticket if the bill includes one ticket only
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
    def ticket_winning_combinations(ticket, extraction):
        """
        it checks if there are winning combinations within the ticket
        @param ticket is a Ticket object
        @param extraction is an Extraction object
        return value is a dictionary with winning combinations if the ticket is winning
        otherwise the method returns None (no winning combinations)
        """
        city = ticket.city.city
        ticket_numbers = ticket.numbers.numbers
        winning_combinations = {}

        # the logic of winning combinations changes depending of the choice of the city: "Tutte" or single cities
        if city != 'Tutte':
            winning_combinations[city] = []
            city_extraction = extraction.extraction[city]
            for number in ticket_numbers:
                if number in city_extraction:
                    winning_combinations[city].append(number)
            # WINNING TICKET
            if len(winning_combinations[city]) >= ticket.bet_type.min_numbers:
                return winning_combinations
            # LOSING TICKET: no winning combinations
            else:
                return None
    
        elif city == 'Tutte':
            matching_combinations = {}
            for city_extraction in extraction.extraction:
                for number in ticket_numbers:
                    if number in extraction.extraction[city_extraction]:
                        if city_extraction not in matching_combinations:
                            matching_combinations[city_extraction] = [number]
                        else:
                            matching_combinations[city_extraction].append(number)
            for city in matching_combinations:
                if len(matching_combinations[city]) >= ticket.bet_type.min_numbers:
                    winning_combinations[city] = matching_combinations[city]
            # WINNING TICKET
            if winning_combinations != {}:
                return winning_combinations
            # LOSING TICKET: no winning combinations
            else:
                return None


    def show_results(self):
        """
        the method will display the results of the tickets (win or lose)
        if ticket is winning, it will also display the winning combinations
        """
        ticket_number = 0

        for ticket in self.tickets:
            ticket_number += 1
            print_ticket(ticket, ticket_number)

            if ticket.city.city != 'Tutte':
                print('{} extraction'.format(ticket.city.city), end=' ')
                print(self.extraction.extraction[ticket.city.city])
            #print()

            ticket_win = LottoManager.ticket_winning_combinations(ticket, self.extraction)
            if ticket_win:
                print('Congratulations: YOU WON !')
                print()
                print('winning combinations: ')
                for city in ticket_win:
                    print('{}: {}'.format(city, ticket_win[city]))

            elif ticket_win == None:
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
        self.show_results()
        return ''

    
if __name__ == '__main__':
    lotto_game = LottoManager(2)
    print(lotto_game)
