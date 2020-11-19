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
    ap = argparse.ArgumentParser(description='single Lotto ticket')
    ap.add_argument("-n", type=int, help='amount of tickets', choices=[1, 2, 3, 4, 5])
    args = ap.parse_args()
    lotto_bill = play_lotto(args.n)
    print(lotto_bill)


if __name__ == '__main__':
    main()



"""
def main():
    num = int(input('enter amount: '))
    output = play_lotto(num)
    print()
    print('Here is your bill...')
    print(output)


if __name__ == '__main__':
    main()
"""
