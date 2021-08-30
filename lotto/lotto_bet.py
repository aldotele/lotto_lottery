class Bet:
    """
    represents the type of bet
    @attr name is the name of the bet as a lowercase string
    @attr min_numbers is the minimum amount of numbers needed for that bet, and is equal to the bet code
    """
    bet_strings = {1: 'ambata', 2: 'ambo', 3: 'terno', 4: 'quaterna', 5: 'cinquina'}
    bet_codes = {'ambata': 1, 'ambo': 2, 'terno': 3, 'quaterna': 4, 'cinquina': 5}

    def __init__(self, bet_code):
        if Bet.is_bet_valid(bet_code):
            bet_code = int(bet_code)
            self.name = Bet.bet_strings[bet_code]
            self.min_numbers = bet_code
        else:
            raise ValueError('bet code must be an integer between 1 and 5')

    @staticmethod
    def is_bet_valid(bet_code):
        """
        validates the bet code which has to be between 1 and 5
        :param bet_code: integer
        :return: boolean
        """
        try:
            bet_code = int(bet_code)
            if bet_code in Bet.bet_strings:
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
        for key in Bet.bet_strings:
            if amount >= key:
                print('{} : {}'.format(key, Bet.bet_strings[key]))

    @staticmethod
    def get_bets():
        return list(Bet.bet_strings.values())
