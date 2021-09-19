from trick import Trick
from deck import Deck
from player import Player
from round import Round
from card import Card
from hand import Hand
import unittest


class HandTest(unittest.TestCase):

    # TODO: Sort hand tests
    def test_sort_hand_null(self):
        deck = Deck()
        # Arrange
        cards = deck.cards

        player = Player("TestPlayer")

        round = Round(1)
        round.set_declarer(player)
        round.set_type(Round.Type.NULL)
        hand = Hand(cards, round)

        # Act
        hand.sort_hand_for_null()
        # Assert
        self.assertEqual(
            hand.cards[0], Card(Card.Suit.CLUB), Card.Face.JACK)
        self.assertEqual(
            hand.cards[31], Card(Card.Suit.DIAMOND, Card.Face.SEVEN))

    def test_jack_multiplier_1(self):
        # Arrange
        cards = [
            Card(Card.Suit.CLUB, Card.Face.JACK),
            # Card(Card.Suit.SPADE, Card.Face.JACK),
            # Card(Card.Suit.HEARTS, Card.Face.JACK),
            # Card(Card.Suit.DIAMOND, Card.Face.JACK)
        ]
        hand = Hand(cards, Round(1))
        # Act
        multiplier = hand.get_jack_multiplier()
        # Assert
        self.assertEqual(multiplier, 1)

    def test_jack_multiplier_1_1(self):
        # Arrange
        cards = [
            # Card(Card.Suit.CLUB, Card.Face.JACK),
            Card(Card.Suit.SPADE, Card.Face.JACK),
            # Card(Card.Suit.HEARTS, Card.Face.JACK),
            # Card(Card.Suit.DIAMOND, Card.Face.JACK)
        ]
        hand = Hand(cards, Round(1))
        # Act
        multiplier = hand.get_jack_multiplier()
        # Assert
        self.assertEqual(multiplier, 1)

    def test_jack_multiplier_2(self):
        # Arrange
        cards = [
            Card(Card.Suit.CLUB, Card.Face.JACK),
            Card(Card.Suit.SPADE, Card.Face.JACK),
            # Card(Card.Suit.HEARTS, Card.Face.JACK),
            # Card(Card.Suit.DIAMOND, Card.Face.JACK)
        ]
        hand = Hand(cards, Round(1))
        # Act
        multiplier = hand.get_jack_multiplier()
        # Assert
        self.assertEqual(multiplier, 2)

    def test_jack_multiplier_2_1(self):
        # Arrange
        cards = [
            # Card(Card.Suit.CLUB, Card.Face.JACK),
            #Card(Card.Suit.SPADE, Card.Face.JACK),
            Card(Card.Suit.HEARTS, Card.Face.JACK),
            # Card(Card.Suit.DIAMOND, Card.Face.JACK)
        ]
        hand = Hand(cards, Round(1))
        # Act
        multiplier = hand.get_jack_multiplier()
        # Assert
        self.assertEqual(multiplier, 2)

    def test_jack_multiplier_3(self):
        # Arrange
        cards = [
            Card(Card.Suit.CLUB, Card.Face.JACK),
            Card(Card.Suit.SPADE, Card.Face.JACK),
            Card(Card.Suit.HEARTS, Card.Face.JACK),
            # Card(Card.Suit.DIAMOND, Card.Face.JACK)
        ]
        hand = Hand(cards, Round(1))
        # Act
        multiplier = hand.get_jack_multiplier()
        # Assert
        self.assertEqual(multiplier, 3)

    def test_jack_multiplier_3_1(self):
        # Arrange
        cards = [
            # Card(Card.Suit.CLUB, Card.Face.JACK),
            # Card(Card.Suit.SPADE, Card.Face.JACK),
            # Card(Card.Suit.HEARTS, Card.Face.JACK),
            Card(Card.Suit.DIAMOND, Card.Face.JACK)
        ]
        hand = Hand(cards, Round(1))
        # Act
        multiplier = hand.get_jack_multiplier()
        # Assert
        self.assertEqual(multiplier, 3)

    def test_jack_multiplier_4(self):
        # Arrange
        cards = [
            Card(Card.Suit.CLUB, Card.Face.JACK),
            Card(Card.Suit.SPADE, Card.Face.JACK),
            Card(Card.Suit.HEARTS, Card.Face.JACK),
            Card(Card.Suit.DIAMOND, Card.Face.JACK)
        ]
        hand = Hand(cards, Round(1))
        # Act
        multiplier = hand.get_jack_multiplier()
        # Assert
        self.assertEqual(multiplier, 4)
