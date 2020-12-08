class Money:
    """
    represents the money bet on a given ticket
    """
    def __init__(self, amount):
        if Money.is_amount_valid(amount):
            amount = float(amount)
            self.amount = amount
        else:
            return None

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

