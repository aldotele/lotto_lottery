
class BetType:
    # la seguente è una proprietà della classe e non d'istanza
    all_bets = {'ambata': 1, 'ambo': 2, 'terno': 3, 'quaterna': 4, 'cinquina': 5}

    def __init__(self, bet_type):
        # faccio in modo che scrivere "AMBO", "    amBo" oppure "Ambo   " equivalga a scrivere "ambo"
        bet_type = bet_type.strip().lower()
        if self.is_bet_valid(bet_type):
            self.bet_type = bet_type
            self.minimum_to_bet = BetType.all_bets[bet_type]


    def is_bet_valid(self, bet_type):
        if bet_type in BetType.all_bets:
            return True
        else:
            raise ValueError('bet is not valid.\nPlease type one of the following bets ---> {}'.format(' '.join(BetType.all_bets)))


# tests
if __name__ == '__main__':

    mybet = BetType('    AmB')
    print(mybet.bet_type)
