class Money:
    """
    represents the money bet on a given ticket
    """
    def __init__(self, amount):
        if Money.is_amount_valid(amount):
            amount = float(amount)
            self.amount = amount
        else:
            raise ValueError('amount must be an integer between 1 and 200')

    @staticmethod
    def is_amount_valid(amount):
        try:
            amount = float(amount)
            if 1 <= amount <= 200:
                return True
            else:
                return False
        except:
            return False

