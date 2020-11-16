import random
import argparse

from lotto.lotto_table_lib import print_lotto_bill


# each instance of Ruota will have an attribute called numbers which is a list of all numbers between 1-90, shuffled
class Ruota:
    def __init__(self):
        self.numbers = []
        for i in range(1, 91):
            self.numbers.append(i)
        random.shuffle(self.numbers)
 
    # when printing an instance of Ruota, all numbers shuffled will appear as a sequence. There may be no need of using it.
    def __str__(self):
        res = []
        for num in self.numbers:
            res.append(str(num))       
        return ' '.join(res)


# each instance of the class Ticket is a single ticket with three attributes: an attribute which describes how many
# numbers does the ticket have, an attribute for the type of bet (ambo, terna, etc.) and an attribute for the
# city to bet on (napoli, bari, milano, etc.)
class Ticket:
    def __init__(self, n, bet, city): 
        # I will construct the ticket only if all three parameters pass the tests that are written in the validation method.
        if self.validation(n, bet, city):
            # the generator is a temporary variable that uses an instance of Ruota to put random numbers in the ticket
            generator = Ruota()
            all_numbers = generator.numbers
            self.numbers = []
            self.bet = bet.upper() 
            # I want the city to appear as a two-character string (Napoli --> NA, Roma --> RM, etc.)
            # for every city except roma, I can just take the first two characters
            if city.lower() == 'roma':
                self.city = 'RM'
            else:  
                self.city = city.upper()[:2]
            # the amount of numbers generated (per-ticket) will depend on the parameter n 
            for i in range(n):
                self.numbers.append(all_numbers.pop())


    def validation(self, n, bet, city):
        # I use the following dictionary to perform an error checking
        t_check = {'n': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'bet': ['ambata', 'ambo', 'terna', 'quaterna', 'cinquina'],\
            'city': ['napoli', 'bari', 'cagliari', 'firenze', 'genova', 'milano', 'palermo', 'roma', 'torino', 'venezia']}
        # error checking: amount of numbers and bet
        if n not in t_check['n']:
            print('Amount of numbers is not valid: choose one between 1 and 10.')
            raise ValueError('invalid amount of numbers')
        if bet.lower() not in t_check['bet']:
            print('Bet is not valid. Please choose a bet type from this list: {}'.format(' '.join(t_check['bet'])))
            raise ValueError('invalid bet')
        # error checking: I make sure the type of bet is coherent with the amount of numbers
        bet = bet.lower()
        if (n < 5 and bet in t_check['bet'][4:]) or (n < 4 and bet in t_check['bet'][3:]) or\
        (n < 3 and bet in t_check['bet'][2:]) or (n < 2 and bet in t_check['bet'][1:]):
            print('amount of numbers {} and bet {} are not valid together. Try again.'.format(n, bet.upper()))
            raise ValueError('invalid combination numbers-bet')  
        # error checking: city
        if city.lower() not in t_check['city']:
            print('City is not valid. Please choose a valid city from this list: {}.'.format(' '.join(t_check['city'])))
            raise ValueError('invalid city')

        # if no ValueError is encountered, then all three parameters are validated
        return True


    # when printed, the single ticket will show a string indicating numbers, city and type of bet
    # for example "TERNA bet on NA. Ticket >>> 5 38 14 87"
    def __str__(self):
        numbers = []
        for num in self.numbers:
            numbers.append(str(num))
        output = ' '.join(numbers)       
        return f"{self.bet.upper()} bet on {self.city.upper()}. Ticket >>> {output}"


# the following class can be used to generate n tickets automatically (I call it a bill), and printing any instance of it will display
# a visual version of the bill with all the tickets and their details shown together, separed by columns and rows
# this class has reference to the Ticket class
class TicketGenerator:
    def __init__(self, n):
        # the tickets attribute will store all instances of Ticket as elements of the same list
        # each instance/element will have its own numbers-bet-city attributes
        self.tickets = []
        # Then I build a dictionary with all the info (numbers, bets and cities) about all the generated tickets
        # the dictionary will store values coming from the attributes of each Ticket instance
        # this "dictionary" attribute will be used in the visual version of the bill, when calling the __str__ method
        self.bill_info = {'nums': [], 'bets': [], 'cities': []}

        # the following loop is used to populate the two previous attributes
        for ticket in range(1, n + 1):
            # For each ticket, the user will be asked to enter: amount of numbers, type of bet and city
            # in case an error is encountered while generating one ticket, the program will give info and ask to rewrite that ticket
            while True:
                try:
                    numbers = int(input(f"ticket {ticket}. How many numbers? "))
                    bet = input(f"ticket {ticket}. Type of bet: ")
                    city = input(f"ticket {ticket}. Choose a city: ")
    
                    # when I have all the info for a single ticket, I use them to make a Ticket instance
                    single_ticket = Ticket(numbers, bet, city)
                    # each single ticket instance will be added to the tickets attribute
                    self.tickets.append(single_ticket)
                    # then for each ticket instance, all relevant information will be also stored into a main dictionary
                    self.bill_info['nums'].append(single_ticket.numbers)
                    self.bill_info['bets'].append(single_ticket.bet.upper())
                    self.bill_info['cities'].append(single_ticket.city)
                except ValueError:
                    print('please rewrite current ticket.')
                    continue
                else:
                    break
    

    def __str__(self):
        # I use a function of my own library that I created (and imported) in order to print the lotto bill
        # the imported function takes a dictionary as parameter, in this case the dictionary is an attribute of my instance
        print_lotto_bill(self.bill_info)

        # the code below is just an alternative way of printing the bill: instead of a visual bill, it is a sequence of strings
        """
        for ticket in self.tickets:
            print(ticket)
        """
        return 'good luck :)'


def main():
    
    # I use argparse to parse arguments passed from CLI
    parser = argparse.ArgumentParser(description="single lotto ticket")
    parser.add_argument("n", type=int, help='amount of ticket or numbers', choices=[1, 2, 3, 4, 5])
    args = parser.parse_args()
    # the bill is an istance of TicketGenerator
    my_bill = TicketGenerator(args.n)
    # printing an instance of TicketGenerator means calling its __str__ method which will display a visual bill
    print(my_bill)  
    

if __name__ == "__main__":
    main()









