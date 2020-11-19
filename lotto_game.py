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
    
    if args.verbose:
        print('ITALIAN LOTTERY\nYou have chosen to create {} Lotto tickets\nLet\'s get started!'.format(args.n))
    else:
        pass

    lotto_bill = play_lotto(args.n)
    print()
    print(lotto_bill)


if __name__ == '__main__':
    main()
