# lotto_lottery
# # three-levels project

Level 1 of the project requires to develop a lotto ticket generator: the software will have to ask how many tickets to generate
and, for each ticket: how many numbers (max. 10), the type of bet (ambo, terna, etc.) and the city of extraction (ruota napoli, ruota firenze, etc.).

There are two scripts for level 1. The 'lotto-ticket-generator.py' is the script that actually does generate the tickets, while
the script 'lotto_table_lib.py' is part of a module from which a function will be imported, and it was developed to generate a visual
representation of the lotto bill after each ticket is generated.

Each ticket is a bill itself, but in the implementation I used the word bill to indicate a final bill where all the generated
tickets are gathered.

I used three classes:

Ruota ---> it has an attribute 'numbers' which is a list of all numbers (shuffled) between 1-90.

Ticket --> each instance refers to one single ticket. It is constructed on three main information: amount of numbers, bet, city.
These informations will be stored separately into its three attributes.
It uses an instance of Ruota in order to randomly generate the 'n' numbers, extracting them from the range 1-90

TicketGenerator --> an instance of it can be considered as a final bill with 'n' generated tickets. The numbers of tickets
to generate is the parameter n of the class and will be chosen by the user.
It has two attributes: the 'tickets' attribute will store the 'n' tickets as elements of a list. Each element will be then an instance
of Ticket with its own informations (numbers, bet, city). 
While 'the bill_info attribute' is a dictionary that gathers in one place all informations about all tickets, using three keys: nums bets and cities. The value of each key is a list that gets the informations from each ticket in an ordered way: for example, the first element of 'nums' will be the list of numbers of ticket 1, the second element will be the list of numbers of ticket 2, while the first element of 'bets' will be the bet chosen for ticket 1, and so on.
This dictionary will be passed as a parameter of a function which is imported from 'lotto_table_lib.py', and that will be invoked in the
__str__ method of the TicketGenerator class. When printing an instance of this class, the program will use the function (and its dictionary parameter) to display a visual representation of the bill with every ticket (and their details) inside it, organized into rows and columns.


