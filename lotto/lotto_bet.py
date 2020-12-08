class BetType:
    """
    represents the type of bet
    @attr bet_code is a numeric value which the bet type is associated to
    @attr min_numbers is the minimum amount of numbers needed to place that bet
    """
    all_bets = {1: 'ambata', 2: 'ambo', 3: 'terno', 4: 'quaterna', 5: 'cinquina'}

    def __init__(self, bet_code):
        if BetType.is_bet_valid(bet_code):
            bet_code = int(bet_code)
            self.bet_type = BetType.all_bets[bet_code]
            self.min_numbers = bet_code
        else:
            return None


    @staticmethod
    def is_bet_valid(bet_code):
        try:
            bet_code = int(bet_code)
            if bet_code in BetType.all_bets:
                return True
            else:
                return False
        except:
            return False


    @staticmethod
    def show_allowed_bets(amount=5):
        """
        it shows the allowed bets based on the placed amount of numbers
        @param amount is by default 5, which means the method will show all existing bets
        """
        for key in BetType.all_bets:
            if amount >= key:
                print('{} : {}'.format(key, BetType.all_bets[key]))

