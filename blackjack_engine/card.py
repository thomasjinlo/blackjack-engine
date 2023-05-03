class Card:
    FACE_VALUE_TO_VALUE = {
        'A': 11,
        'K': 10,
        'Q': 10,
        'J': 10,
        '10': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2
    }

    def __init__(self, suit: str, face_value: str):
        self.suit = suit
        self.face_value = face_value
        self.value = Card.FACE_VALUE_TO_VALUE[face_value]

    def __add__(self, other) -> int:
        if isinstance(other, Card):
            return self.value + other.value

        if isinstance(other, int):
            return self.value + other

        raise TypeError(
            f'Unsupported type. Expected Card or int, but received {type(other)}'
        )

    def __radd__(self, other) -> int:
        return self + other

    @property
    def is_ace(self) -> bool:
        return self.face_value == 'A'
