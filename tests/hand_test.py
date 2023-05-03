import pytest

from blackjack_engine import Card, Hand


def test_initialized_with_empty_list_of_cards():
    hand = Hand()

    assert hand.cards == []


def test_add_card_to_list():
    card = Card(suit='suit', face_value='10')
    hand = Hand()
    hand.add_card(card)

    assert hand.cards == [card]


@pytest.mark.parametrize(
    ['face_values', 'expected_min_value', 'expected_max_value'],
    [(['10', '10', '10'], 30, 30), (['A', '10'], 11, 21),
     (['A', '5', 'A'], 7, 17), (['5', '6', 'K'], 21, 21)])
def test_calculates_correct_total_value(face_values, expected_min_value,
                                        expected_max_value):
    hand = Hand()
    for face_value in face_values:
        hand.add_card(Card(suit='suit', face_value=face_value))
    min_value, max_value = hand.value

    assert min_value == expected_min_value
    assert max_value == expected_max_value


@pytest.mark.parametrize('face_values, is_bust', [(['2', '10', '10'], True),
                                                  (['10', '10'], False),
                                                  (['A', '7', 'A'], False),
                                                  (['A', '10'], False)])
def test_is_bust(face_values, is_bust):
    hand = Hand()

    for face_value in face_values:
        hand.add_card(Card(suit='suit', face_value=face_value))

    assert hand.is_bust == is_bust


@pytest.mark.parametrize('face_values, is_blackjack',
                         [(['5', '6', '10'], False), (['5', '6', 'K'], False),
                          (['10', '10'], False), (['K', 'A'], True),
                          (['10', 'A'], True), (['A', '10'], True)])
def test_is_blackjack(face_values, is_blackjack):
    hand = Hand()

    for face_value in face_values:
        hand.add_card(Card(suit='suit', face_value=face_value))

    assert hand.is_blackjack == is_blackjack
