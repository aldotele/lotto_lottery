import argparse

from lotto.lotto_manager import LottoManager


def play_lotto(tickets_amount):
    """
    it returns an object which represents a lotto bill
    the object will have as attribute a list of single Ticket objects (even one Ticket object only)
    """
    bill = LottoManager(tickets_amount)

    return bill


def main():
    ap = argparse.ArgumentParser(description='Lotto bill with one or more tickets')
    ap.add_argument("n", type=int, help='amount of tickets', choices=[1, 2, 3, 4, 5])
    ap.add_argument('-v', '--verbose', help='introduction message', action='store_true')
    args = ap.parse_args()
    
    print('ITALIAN LOTTERY\nYou have chosen to create {} Lotto tickets'.format(args.n))

    if args.verbose:
        print('You can place a minimum of 1 and a maximum of 10 unique numbers per ticket.')
        print('Each number must be between 1 and 90. You can choose them or generate a random sequence.')
        print('For each ticket, you will be asked to enter a bet type, which must be coherent with the amount of numbers.')
        print('For each ticket, you will be asked to choose a city of extraction.')
    else:
        pass

    print("Let's get started!")
    lotto_bill = play_lotto(args.n)
    print()
    print(lotto_bill)


if __name__ == '__main__':
    main()
