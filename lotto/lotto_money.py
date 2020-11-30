class Money:
    """
    represents the money bet on a given ticket
    """
    def __init__(self, amount):
        if Money.is_amount_valid(amount):
            self.amount = amount
        else:
            return None


    @staticmethod
    def is_amount_valid(amount):
        try:
            amount = int(amount)
            if 1 <= amount <= 200:
                return True
            else:
                print('NOT VALID. Amount of money must be between € 1 and € 200.')
                return False
        except:
            print('NOT VALID. Amount of money must be a number.')
            return False


if __name__ == '__main__':
    my_money = Money('dieci')  # not valid
    my_money = Money(220)  # not valid
    my_money = Money(0)  # not valid
    my_money = Money('10')  # valid because it gets converted to an integer
    my_money = Money(1)
