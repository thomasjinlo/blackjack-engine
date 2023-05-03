from typing import Generator


class Player:

    def __init__(self, balance: str, prompter: PlayerMovePrompter):
        self.balance = balance
        self.prompter = prompter
        self.hands = []

    def prompt_move(self, hand):
        return self.prompter.prompt_move(hand=hand)

    def play_hands(self,
                   hand_index=0,
                   shoe: Generator[Card, None, None]) -> None:
        for hand in self.hands[hand_index:]:
            move = prompt_move(hand)

            while hand.active and move != PlayerMove.STAY:
                if move is PlayerMove.HIT:
                    hand.add_card(next(shoe))

                if move is PlayerMove.SPLIT:
                    self.bet(amount=hand.bet_amount)
                    new_hands = hand.split(card_one=next(shoe),
                                           card_two=next(shoe))

                    self.hands = self.hands[:
                                            hand_index] + new_hands + self.hands[
                                                hand_index + 1:]

                    return self.play_hands(hand_index=hand_index, shoe=shoe)

                if move is PlayerMove.DOUBLE:
                    self.bet(amount=hand.bet_amount)
                    hand.double(next(shoe))

                move = prompt_move(hand)

    def receive_one_card_per_hand(self, shoe: Generator[Card, None,
                                                        None]) -> None:
        for hand in self.hands:
            hand.add_card(next(shoe))

    def place_bet(self, minimum_bet) -> None:
        bet_amount = self.prompter.prompt_bet()

        if bet_amount < minimum_bet:
            self.prompter.print_less_than_minimum_bet(bet_amount)
            return self.place_bet(minimum_bet)

        if bet_amount > self.balance:
            self.prompter.print_insufficient_funds(bet_amount=bet_amount,
                                                   player_balance=self.balance)
            return self.place_bet(minimum_bet)

        hand = Hand(bet_amount=bet_amount)
        self.bet(amount=bet_amount)
        self.hands.append(hand)

    def bet(self, amount: int) -> None:
        self.amount -= amount
