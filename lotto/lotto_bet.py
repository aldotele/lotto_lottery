class Bet:
    """
    represents the type of bet
    @attr name is the name of the bet as a lowercase string
    @attr min_numbers is the minimum amount of numbers needed for that bet, and is equal to the bet code
    """
    all_bets = {1: 'ambata', 2: 'ambo', 3: 'terno', 4: 'quaterna', 5: 'cinquina'}

    def __init__(self, bet_code):
        if Bet.is_bet_valid(bet_code):
            bet_code = int(bet_code)
            self.name = Bet.all_bets[bet_code]
            self.min_numbers = bet_code
        else:
            return None

    @staticmethod
    def is_bet_valid(bet_code):
        """
        validates the bet code which has to be between 1 and 5
        :param bet_code: integer
        :return: boolean
        """
        try:
            bet_code = int(bet_code)
            if bet_code in Bet.all_bets:
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
        for key in Bet.all_bets:
            if amount >= key:
                print('{} : {}'.format(key, Bet.all_bets[key]))

