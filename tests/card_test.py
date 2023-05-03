import pytest

from blackjack_engine import Card


def test_adding_cards():
    card = Card(suit='suit', face_value='10')
    other_card = Card(suit='suit', face_value='9')

    assert card + other_card == card.value + other_card.value


def test_adding_int():
    card = Card(suit='suit', face_value='10')
    other_value = 10

    assert card + other_value == card.value + other_value


@pytest.mark.parametrize('unexpected_value, unexpected_type', [('10', str),
                                                               (10.0, float)])
def test_adding_unexpected_type(unexpected_value, unexpected_type):
    card = Card(suit='suit', face_value='10')

    with pytest.raises(
            TypeError,
            match=
            f'Unsupported type. Expected Card or int, but received {unexpected_type}'
    ):
        card + unexpected_value


@pytest.mark.parametrize('face_value, is_ace', [('10', False), ('K', False),
                                                ('A', True)])
def test_is_ace(face_value, is_ace):
    card = Card(suit='suit', face_value=face_value)

    assert card.is_ace == is_ace
