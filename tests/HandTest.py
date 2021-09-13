from trick import Trick
from deck import Deck
from player import Player
from round import Round
from card import Card
from hand import Hand
import unittest


class HandTest(unittest.TestCase):

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
