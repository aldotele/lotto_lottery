def print_beam(width):
    """
    creates a beam of a given width
    e.g. a beam of width 8 is: +------+
    """
    print('+', end='')
    for i in range(width-2):
        print('-', end='')
    print('+')


def print_row(width, string):
    """
    creates a row with centered text
    @param width is the preferred width of the row
    @param string is the string that has to appear inside the row
    """
    if width % 2 != 0:
        width -= 1

    margin = width - len(string) - 2
    print('|' + ' '*(margin//2) + string + ' '*(margin//2) + '|')


def print_ticket(ticket, ticket_n=' ', width=50):
    # making sure the width is even in order to improve layout
    if width % 2 != 0:
        width -= 1

    print_beam(width)

    # HEADER ROW
    header_string = 'LOTTO Ticket {}'.format(ticket_n)
    print_row(width, header_string)  

    print_beam(width)

    # BET-CITY ROW
    bet = ticket.bet_type.bet_type
    city = ticket.city.city
    bet_city_string = '{} on {}'.format(bet, city)
    if len(bet_city_string) % 2 != 0:
        bet_city_string += ' '
    print_row(width, bet_city_string)

    print('|' + ' '*(width-2) + '|')

    # NUMBERS ROW
    numbers = ticket.numbers.numbers
    str_sequence = [str(n) for n in numbers]
    numbers_string = ' '.join(str_sequence)
    if len(numbers_string) % 2 != 0:
        numbers_string += ' '
    print_row(width, numbers_string)

    print_row(width, '----')

    # MONEY ROW
    money_str = '€ {}'.format(ticket.money.amount)
    if len(money_str) % 2 != 0:
        money_str += ' '
    print_row(width, money_str)

    print_beam(width)


def print_extraction(extraction):
    print('+' + '-'*33 + '+')
    for city in extraction:
        int_sequence = extraction[city]
        #str_sequence = [str(el) for el in int_sequence]
        print('|%10s' % city, end = '  ')
        for number in int_sequence:
            print('%.2d' % number, end='  ')
        print(' |')
    print('+' + '-'*33 + '+')

