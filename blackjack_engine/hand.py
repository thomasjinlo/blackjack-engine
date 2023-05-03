from . import Card


class Hand:
    MAX = 21

    def __init__(self, bet_amount: int):
        self.bet_amount = bet_amount
        self.cards = []

    @property
    def value(self) -> int:
        non_ace_value = sum(card.value for card in self.cards
                            if not card.is_ace)
        num_aces = sum(1 for card in self.cards if card.is_ace)

        min_value = non_ace_value + num_aces
        max_value = non_ace_value + (num_aces * 11)

        for _ in range(num_aces):
            if max_value > Hand.MAX:
                max_value -= 10

        return min_value, max_value

    @property
    def min_value(self) -> int:
        _min_value, _ = self.value

        return _min_value

    @property
    def max_value(self) -> int:
        _, _max_value = self.value

        return _max_value

    @property
    def is_bust(self) -> bool:
        return self.min_value > Hand.MAX

    @property
    def is_blackjack(self) -> bool:
        return len(self.cards) == 2 and self.max_value == Hand.MAX

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def split(self, card_one: Card, card_two: Card) -> List[Hand, Hand]:
        split_card_one, split_card_two = self.cards
        hand_one, hand_two = Hand(), Hand()

        hand_one.add_card(split_card_one)
        hand_one.add_card(card_one)
        hand_two.add_card(split_card_two)
        hand_two.add_card(card_two)

        return [hand_one, hand_two]

    def double(self, card: Card) -> None:
        self.add_card(card)
        self.bet_amount *= 2
