class BetType:
    """
    represents the type of bet
    @attr bet_code is a numeric value which the bet type is associated to
    @attr min_numbers is the minimum amount of numbers needed to place that bet
    """
    all_bets = {1: 'ambata', 2: 'ambo', 3: 'terno', 4: 'quaterna', 5: 'cinquina'}

    def __init__(self, bet_code):
        if BetType.is_bet_valid(bet_code):
            self.bet_type = BetType.all_bets[bet_code]
            self.min_numbers = bet_code
        else:
            return None


    @staticmethod
    def is_bet_valid(bet_code):
        if bet_code in BetType.all_bets:
            return True
        else:
            print('NOT VALID: choose a number between 1 and 5')
            return False


    @staticmethod
    def print_allowed_bets(amount=5):
        for key in BetType.all_bets:
            if amount >= key:
                print('{} : {}'.format(key, BetType.all_bets[key]))


# tests
if __name__ == '__main__':
    mybet = BetType('3') # not valid
    mybet = BetType(3)
    print(mybet.bet_type)
    print('minimum numbers to place: {}'.format(mybet.min_numbers))
    BetType.print_allowed_bets(4)
