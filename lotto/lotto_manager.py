from lotto.lotto_numbers import NumbersForTicket
from lotto.lotto_bet import Bet
from lotto.lotto_city import City
from lotto.lotto_ticket import Ticket
from lotto.lotto_extraction import Extraction
from lotto.lotto_money import Money
from lotto.lotto_prizes import Prizes
from lotto.lotto_tables import print_ticket

from datetime import datetime


class LottoManager:
    """
    represents the business logic of the program
    @attr tickets is a list with a series of Ticket objects (even one only)
    @attr extraction is an extraction object which includes all city extractions
    """

    def __init__(self, tickets_amount):
        self.tickets = []
        for t in range(1, tickets_amount + 1):
            # the class will create as many Ticket instance as the specified amount
            # each Ticket instance is created by invoking a static method, and asking all ticket info to the user
            ticket = LottoManager.ticket_creator(t)
            self.tickets.append(ticket)
        # the object will have an extraction attribute with cities as keys and extraction numbers as values
        self.extraction = Extraction()

    @staticmethod
    def ticket_creator(t):
        print()
        print('--- TICKET {} ---'.format(t))
        print()

        # below methods return objects
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
        ticket_to_confirm = Ticket(numbers, bet, city, money)  # passed arguments are objects
        print()
        # checking confirmation: if ticket is confirmed, it is also created
        # otherwise the process will restart by asking again all ticket info for the current ticket
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
        Bet.show_allowed_bets()
        bet_code = input('\nEnter a number: ')
        while True:
            if Bet.is_bet_valid(bet_code):
                bet_code = int(bet_code)
                # returning an object
                return Bet(bet_code)
            else:
                print('NOT VALID: bet must be a number between 1 and 5.')
                bet_code = input('Enter a number: ')

    @staticmethod
    def choose_city():
        print('*** CITY CHOICE ***')
        print()
        City.show_city_list()
        city_code = input('\nEnter a number: ')
        while True:
            if City.is_city_valid(city_code):
                city_code = int(city_code)
                # returning an object
                return City(city_code)
            else:
                print('NOT VALID: city must be a number between 1 and 11.')
                city_code = input('Enter a number: ')

    @staticmethod
    def choose_amount(bet):
        print('*** NUMBERS CHOICE ***')
        print()
        print('Choose an amount of numbers to place:')
        NumbersForTicket.show_allowed_amounts(bet.min_numbers)
        amount = input('\nHow many numbers? ')
        while True:
            if NumbersForTicket.is_amount_valid(amount, bet.min_numbers):
                amount = int(amount)
                return amount
            else:
                print('NOT VALID: you are allowed to place from {} to 10 numbers.'.format(bet.min_numbers))
                amount = input('How many numbers? ')

    @staticmethod
    def choose_numbers(amount):
        # the method is used to generate random sequences of numbers until the user chooses the one he likes
        print('generating your {} numbers ...'.format(amount))
        random_numbers = NumbersForTicket(amount)
        while True:
            print('numbers: {}'.format(random_numbers.sequence))
            print()
            check_confirmation = input('Do you like the above numbers?\n1 - Confirm\n0 - Regenerate\nType here: ')
            if check_confirmation == '1':
                # returning an object
                return random_numbers

            elif check_confirmation == '0':
                print()
                print('generating your {} numbers ...'.format(amount))
                random_numbers = NumbersForTicket(amount)

    @staticmethod
    def choose_money():
        print('*** MONEY CHOICE ***')
        amount = input('place amount of euro: ')
        while True:
            if Money.is_amount_valid(amount):
                amount = float(amount)
                # returning an object
                return Money(amount)
            else:
                print('NOT VALID: amount of € must be between 1 and 200.')
                amount = input('place amount of euro: ')

    @staticmethod
    def ticket_confirmator(ticket, t):
        """
        represents a summary of the chosen inputs for the current ticket
        it asks the user a confirmation by typing 1 
        otherwise the user can type 0 to restart the ticket
        """
        print('<<< Ticket {} summary >>>:'.format(t))
        print('placed NUMBERS: {}'.format(ticket.numbers.sequence))
        print('BET type: {}'.format(ticket.bet.name))
        print('CITY: {}'.format(ticket.city.name))
        print('MONEY bet: € %.2f' % ticket.money.amount)

        while True:
            print()
            check_confirmation = input('Do you wish to CONFIRM ticket {}?\n1 - Confirm\n0 - Rewrite\nType here: '
                                       .format(t))
            if check_confirmation == '1':
                return True
            elif check_confirmation == '0':
                return False

    @staticmethod
    def print_tickets(bill_of_tickets):
        """
        it prints a series of tickets one by one, or the only ticket if the bill includes one ticket only
        @param bill_of_tickets is a list of Ticket objects
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
        # when printing the extraction object, its __str__ method will be invoked (check Extraction class)
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
        city = ticket.city.name
        ticket_numbers = ticket.numbers.sequence
        winning_combinations = {}

        # the logic of winning combinations changes depending on the choice of the city: "Tutte" or single cities
        if city != 'Tutte':
            winning_combinations[city] = []
            city_extraction = extraction.all_extractions[city]
            for number in ticket_numbers:
                if number in city_extraction:
                    winning_combinations[city].append(number)
            # WINNING TICKET: there is a least amount of matching numbers in the given city extraction
            if len(winning_combinations[city]) >= ticket.bet.min_numbers:
                return winning_combinations
            # LOSING TICKET: no winning combinations
            else:
                return None

        elif city == 'Tutte':
            matching_combinations = {}
            for city_extraction in extraction.all_extractions:
                for number in ticket_numbers:
                    if number in extraction.all_extractions[city_extraction]:
                        if city_extraction not in matching_combinations:
                            matching_combinations[city_extraction] = [number]
                        else:
                            matching_combinations[city_extraction].append(number)
            for city in matching_combinations:
                if len(matching_combinations[city]) >= ticket.bet.min_numbers:
                    winning_combinations[city] = matching_combinations[city]
            # WINNING TICKET: there is a least amount of matching numbers in AT LEAST one city extraction
            if winning_combinations != {}:
                return winning_combinations
            # LOSING TICKET: no winning combinations
            else:
                return None

    def show_results(self):
        """
        the method will display the results of the tickets (win or lose)
        if ticket is winning, it will also display the winning combinations and the money win
        """
        ticket_number = 0
        for ticket in self.tickets:
            ticket_number += 1
            print_ticket(ticket, ticket_number)
            # if bet is on a single city, that city's extraction will be displayed below
            if ticket.city.name != 'Tutte':
                print('{} extraction'.format(ticket.city.name), end=' ')
                print(self.extraction.all_extractions[ticket.city.name])

            # invoking the method that returns potential winning combinations
            # if there are no winning combinations, the variable will store None as a value
            ticket_winning_combinations = LottoManager.ticket_winning_combinations(ticket, self.extraction)

            # if ticket is winning, the program displays all relevant info about matched numbers and money win
            if ticket_winning_combinations:
                money_win = Prizes.compute_payout(ticket, ticket_winning_combinations)
                print('Congratulations: YOU WON € %.2f!' % money_win)
                print()
                print('winning combinations: ')
                # displaying the winning combinations
                for city in ticket_winning_combinations:
                    print('{}: {}'.format(city, ticket_winning_combinations[city]))

            # if no winning combinations are found, then only one message gets displayed
            elif ticket_winning_combinations is None:
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
