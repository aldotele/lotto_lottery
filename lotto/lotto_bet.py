class BetType:
    """
    represents the type of bet
    @attr bet_type is the chosen bet type
    @attr min_numbers is the minimum amount of numbers needed to place that bet
    """
    all_bets = [None, 'ambata', 'ambo', 'terno', 'quaterna', 'cinquina']

    def __init__(self, bet_type):
        # making sure that writing "AMBO", " amBo " or "Ambo " is same as writing "ambo"
        bet_type = bet_type.strip().lower()
        if BetType.is_bet_valid(bet_type):
            bet_type = bet_type
            self.bet_type = bet_type
            self.min_numbers = BetType.all_bets.index(bet_type)
        else:
            return None


    @staticmethod
    def is_bet_valid(bet_type):
        bet_type = bet_type.strip().lower()
        if bet_type in BetType.all_bets:
            return True
        else:
            print('NOT VALID: bet type must be spelled correctly.')
            return False


# tests
if __name__ == '__main__':
    #print(BetType.is_bet_valid('ambo'))
    mybet = BetType('TERno     ')
    print(mybet.bet_type)
    print('minimum numbers to place: {}'.format(mybet.min_numbers))
