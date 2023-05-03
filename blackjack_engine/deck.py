import itertools
from enum import Enum
from typing import List

from . import Card


class Suit(Enum):
    SPADES = '♠'
    HEARTS = '♥'
    DIAMONDS = '♦'
    CLUBS = '♣'


class Deck:
    FACE_VALUES = [
        'A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1'
    ]

    def __init__(self):
        self.cards = self.instantiate_cards()

    @staticmethod
    def instantiate_cards(self):
        return [
            Card(suit=suit, face_value=face_value) for suit, face_value in
            itertools.product(self.suits, Deck.face_values)
        ]

    @property
    def suits(self) -> List[str]:
        return [suit.value for suit in Suit]
