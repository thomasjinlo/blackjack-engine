class ReferenceGame:

    def __init__(self, dealer: Dealer, players: List[Player], shoe: Shoe):
        self.dealer = dealer
        self.players = players
        self.shoe = shoe

    def start_game(self):
        while not shoe.past_penetration:
            self.play_hands()

    def play_hands(self):
        self.place_bets()
        self.deal_initial_cards()
        self.dealer.add_card(next(self.shoe))
        self.dealer.add_card(next(self.shoe))

        for player in self.players:
            player.play_hands(shoe=self.shoe)

        self.dealer.finish_hand(shoe=self.shoe)
        self.process_bets()

    def place_bets(self):
        for player in self.players:
            player.place_bet()

    def process_bets(self):
        for player in self.players:
            player.process_bet(dealer_hand=dealer_hand)

    def deal_initial_cards(self):
        for player in self.players:
            player.receive_one_card_per_hand(self.shoe)
