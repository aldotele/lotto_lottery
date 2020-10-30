# the function creates one column
def print_beam():
    print('+----------', end='')

# I can use this function to call another function n times
def do_n_times(f, n):
    for i in range(n):
        f()

# the function prints the first row where to see how many tickets are present in the bills
# each column will have the title "ticket n" where n is the number of that specific ticket
# each column will occupy the same space, so that the creation can be automatized based on the number of tickets
def print_header(bill):
    n = len(bill['nums'])
    do_n_times(print_beam, n)
    print('+')

    for i in range(1, n + 1):
        print('| ticket {} '.format(i), end='')
    print('|')

    do_n_times(print_beam, n)
    print('+')


# the function creates a single line of numbers: it fills the row by taking the "index" number of each list of numbers
# it uses a loop to go through all the numbers' lists of the, while the parameter line_n is the nth number of each ticket
def print_numline(bill, line_n):
    index = 0
    for i in range(len(bill['nums'])):
        # since the tickets may have different amount of numbers, when I have already printed all the numbers of a specific ticket
        # a white space will be added to that cell
        if line_n < len(bill['nums'][index]): 
            print('| {}'.format(bill['nums'][index][line_n]) + ' '*(9 - len(str(bill['nums'][index][line_n]))), end='')
        else:
            print('|' + ' '*10, end='')
        index += 1          
    print('|')


# the function, based on the previous, creates all the lines of numbers
# the parameter n is the number of lines that we want to create (it cannot be less than the length of the longest ticket)
# to decide n, I can make it equal to the maximum amount of numbers among the generated tickets
def print_numlines(bill):
    row_height = 0
    for el in bill['nums']:
        if len(el) > row_height:
            row_height = len(el)
    # I create as many lines as the highest amount of numbers among the generated tickets
    # tickets may have a different amount of numbers
    # for this reason, I leave an empty space when the row_height exceeds the amount of numbers for a specific ticket
    for i in range(row_height):
        print_numline(bill, i)


def print_footer(bill):
    n = len(bill['nums'])
    do_n_times(print_beam, n)
    print('+')

    for i in range(n):
        print('| {}'.format(bill['bets'][i]) + ' '*(9 - len(bill['bets'][i])), end='')
    print('|')

    for i in range(n):
        print('| ruota {}'.format(bill['cities'][i]) + ' ', end='')
    print('|')

    do_n_times(print_beam, n)
    print('+')


def print_lotto_bill(bill):
    print_header(bill)
    print_numlines(bill)
    print_footer(bill)


# TESTING ...
def main():
    # Here I manually typed a bill example (shaped as a dictionary) in order to test the function
    # the bill is designed as a dictionary with three keys which describe the three main information of each ticket
    # inside the key nums, each sublist contains the numbers generated in one of the ticket
    # inside the key bets, each element is a bet of one ticket. Same logic for the key cities.
    # same tickets have the same indexes in each key of the dictionary
    mybill = {'nums': [[10, 33, 57, 8, 21, 37, 88], [89, 16, 28], [36, 14, 77, 65, 18]], 'bets': ['terna', 'ambo', 'quaterna'],\
        'cities': ['NA', 'MI', 'RM']}

    print_lotto_bill(mybill)


if __name__ == "__main__":
    main()
