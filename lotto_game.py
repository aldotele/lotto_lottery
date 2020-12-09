import argparse

from lotto.lotto_manager import LottoManager


def play_lotto(tickets_amount):
    """
    :param tickets_amount: integer which corresponds to the number of tickets to create
    :return: an object which represents a lotto game with two attributes: a series of Ticket objects and one Extraction
    """
    lotto_game = LottoManager(tickets_amount)

    return lotto_game


def main():
    ap = argparse.ArgumentParser(description='Lotto bill with one or more tickets')
    ap.add_argument("n", type=int, help='amount of tickets', choices=[1, 2, 3, 4, 5])
    ap.add_argument('-v', '--verbose', help='introduction message', action='store_true')
    args = ap.parse_args()
    print()
    print('****** ITALIAN LOTTERY ******')

    # if the optional argument is specified, instructions about the game will show up
    if args.verbose:
        print('- You can place a minimum of 1 and a maximum of 10 unique numbers per ticket.')
        print('- Each number is between 1 and 90. The sequence will be generated randomly.')
        print('- You will be allowed to generate new random sequences until selecting the one you prefer.')
        print('- For each ticket, you will be asked to enter a bet type,'
              ' which must be coherent with the amount of numbers.')
        print('- For each ticket, you will be asked to choose a city of extraction.')

    print('\nYou have chosen to create {} Lotto tickets'.format(args.n))
    print('Let\'s get started!')
    # the lotto_game variable will store an instance of LottoManager
    lotto_game = play_lotto(args.n)

    # printing an instance of LottoManager will invoke the instance __str__ method with the business logic of the game
    print(lotto_game)


if __name__ == '__main__':
    main()
