from lotto.lotto_numbers import NumbersForTicket
from lotto.lotto_bet import Bet
from lotto.lotto_city import City
from lotto.lotto_ticket import Ticket
from lotto.lotto_extraction import Extraction
from lotto.lotto_money import Money
from lotto.lotto_prizes import Prizes
from lotto.lotto_tables import print_ticket
from lotto.helper.selection import select_bet, select_city, select_amount, confirm_numbers, confirm_ticket

from datetime import datetime


class LottoManager:
    """
    represents the business logic of the program
    @attr tickets is a list with a series of Ticket objects (even one only)
    @attr extraction is an extraction object which includes all city extractions
    """

    def __init__(self, tickets_amount, tickets=''):
        self.tickets = []
        if not tickets:
            for t in range(1, tickets_amount + 1):
                # the class will create as many Ticket instance as the specified amount
                # each Ticket instance is created by invoking a static method, and asking all ticket info to the user
                ticket = LottoManager.ticket_creator(t)
                self.tickets.append(ticket)
        else:
            if tickets_amount == len(tickets):
                self.tickets = tickets
            else:
                raise ValueError('Quantity of tickets must be equal to stated amount')
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
        bet = select_bet()  # this will store a string
        bet_code = Bet.bet_codes[bet]
        return Bet(bet_code)

    @staticmethod
    def choose_city():
        city = select_city()  # this will store a string
        city_code = City.city_codes[city]
        return City(city_code)

    @staticmethod
    def choose_amount(bet):
        amount = select_amount(bet)
        return amount

    @staticmethod
    def choose_numbers(amount):
        # the method is used to generate random sequences of numbers until the user chooses the one he likes
        print('generating your {} numbers ...'.format(amount))
        random_numbers = NumbersForTicket(amount)
        while True:
            sequence = random_numbers.sequence
            print('numbers: {}'.format(' '.join(map(str, sequence))))
            print()
            options = ["Confirm", "Regenerate"]
            check_confirmation = confirm_numbers(options)
            if check_confirmation == options[0]:
                # returning an object
                return random_numbers

            elif check_confirmation == options[1]:
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
        print('placed NUMBERS: {}'.format(' '.join(map(str, ticket.numbers.sequence))))
        print('BET type: {}'.format(ticket.bet.name))
        print('CITY: {}'.format(ticket.city.name))
        print('MONEY bet: € %.2f' % ticket.money.amount)

        while True:
            print()
            options = ["Confirm", "Rewrite"]
            check_confirmation = confirm_ticket(options, t)
            if check_confirmation == options[0]:
                return True
            elif check_confirmation == options[1]:
                return False

    @staticmethod
    def show_tickets_before_extraction(bill_of_tickets):
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
    def show_extraction_table(extraction):
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
        it searches for winning combinations in a Ticket object, once the extraction has been made
        this method manipulates the Ticket object by adding a new attribute
        the new attribute is called winning combinations and can be either a dictionary (win) or a None (lost)
        :param ticket is a Ticket object
        :param extraction is an Extraction object
        :return: the Ticket object with a new attribute called winning_combinations
        """
        if not isinstance(ticket, Ticket) or not isinstance(extraction, Extraction):
            raise ValueError('arguments must be valid Ticket and Extraction objects.')

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
                # the Ticket gets assigned a new attribute which is a dictionary of winning combinations
                ticket.winning_combinations = winning_combinations
            # LOSING TICKET: no winning combinations
            else:
                # otherwise the new attribute gets assigned a None
                ticket.winning_combinations = None

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
                # the Ticket gets assigned a new attribute which is a dictionary of winning combinations
                ticket.winning_combinations = winning_combinations
            # LOSING TICKET: no winning combinations
            else:
                # otherwise the new attribute gets assigned a None
                ticket.winning_combinations = None

        return ticket

    @staticmethod
    def is_ticket_winning(checked_ticket):
        if not isinstance(checked_ticket, Ticket):
            raise ValueError('argument must be a valid Ticket object.')
        if not hasattr(checked_ticket, 'winning_combinations'):
            raise ValueError('the ticket\'s result has not been checked yet.')

        if checked_ticket.winning_combinations:
            return True
        else:
            return False

    @staticmethod
    def compute_payout(winning_ticket):
        if not isinstance(winning_ticket, Ticket):
            raise ValueError('argument must be a valid Ticket object')
        if not hasattr(winning_ticket, 'winning_combinations'):
            raise ValueError('the ticket\'s result has not been checked yet.')
        # if the winning combinations attribute is None, an error is raised
        if not winning_ticket.winning_combinations:
            raise ValueError('the passed ticket is not a winning ticket.')

        # the net win will firstly depend on the amount of numbers that were placed
        amount_of_numbers = len(winning_ticket.numbers.sequence)
        bet_code = winning_ticket.bet.min_numbers
        money = winning_ticket.money.amount
        gross_payout = 0
        for city in winning_ticket.winning_combinations:
            base_prize = Prizes.prizes_table[amount_of_numbers][bet_code]
            matched = len(winning_ticket.winning_combinations[city])
            mol_factor = Prizes.combinations[matched][bet_code]
            gross_payout += base_prize * mol_factor

        # if the bet was on "Tutte", payout gets divided by 10
        if winning_ticket.city.name == 'Tutte':
            gross_payout = gross_payout / 10

        taxes = 0.08 * gross_payout
        net_payout = gross_payout - taxes
        net_win = net_payout * money

        if net_win > 6000000:
            net_win = 6000000

        net_win = '%.2f' % net_win
        net_win = float(net_win)

        winning_ticket.net_win = net_win

        return net_win

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

            ticket_after_checking = LottoManager.ticket_winning_combinations(ticket, self.extraction)

            if LottoManager.is_ticket_winning(ticket_after_checking):
                money_win = LottoManager.compute_payout(ticket_after_checking)
                print('Congratulations: YOU WON € %.2f!' % money_win)
                print()
                print('winning combinations: ')
                # displaying the winning combinations
                for city in ticket.winning_combinations:
                    print('{}: {}'.format(city, ticket.winning_combinations[city]))
            else:
                print('YOU LOST :(')
            print()

    def __str__(self):
        LottoManager.show_tickets_before_extraction(self.tickets)
        print()
        extraction_button = input('press ENTER to check extraction')
        print()
        LottoManager.show_extraction_table(self.extraction)
        print()
        results_button = input('press ENTER to check results')
        print()
        self.show_results()
        return ''


if __name__ == '__main__':
    lotto_game = LottoManager(2)
    print(lotto_game)
