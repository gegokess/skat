from trick import Trick
from deck import Deck
from player import Player
from round import Round
from card import Card
from hand import Hand
import unittest


class CardTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.declarer = Player("TestPlayer")
        cls.round = Round(1)
        cls.round.set_declarer(cls.declarer)
        cls.deck = Deck()
        cls.hand = Hand(cls.deck.draw_suit(Card.Suit.CLUB), cls.round)

    def test_less(self):
        self.round.set_type(Round.Type.CLUB)

        club_ace = Card(Card.Suit.CLUB, Card.Face.ACE)
        club_ace.set_round(self.round)
        club_jack = Card(Card.Suit.CLUB, Card.Face.JACK)
        club_jack.set_round(self.round)
        heart_seven = Card(Card.Suit.HEARTS, Card.Face.SEVEN)
        heart_seven.set_round(self.round)
        heart_eight = Card(Card.Suit.HEARTS, Card.Face.EIGHT)
        heart_eight.set_round(self.round)
        heart_jack = Card(Card.Suit.HEARTS, Card.Face.JACK)
        heart_jack.set_round(self.round)
        diamond_ten = Card(Card.Suit.DIAMOND, Card.Face.TEN)
        diamond_ten.set_round(self.round)

        self.assertEqual(club_ace < club_jack, True)
        self.assertEqual(club_jack < club_ace, False)
        self.assertEqual(heart_eight < club_ace, True)
        self.assertEqual(club_ace < heart_eight, False)
        self.assertEqual(club_jack < heart_eight, False)
        self.assertEqual(heart_eight < heart_seven, False)
        self.assertEqual(heart_seven < heart_eight, True)
        self.assertEqual(diamond_ten < heart_eight, True)
        self.assertEqual(heart_eight < diamond_ten, True)

    def test_greater(self):
        self.round.set_type(Round.Type.CLUB)

        club_ace = Card(Card.Suit.CLUB, Card.Face.ACE)
        club_ace.set_round(self.round)
        club_jack = Card(Card.Suit.CLUB, Card.Face.JACK)
        club_jack.set_round(self.round)
        heart_seven = Card(Card.Suit.HEARTS, Card.Face.SEVEN)
        heart_seven.set_round(self.round)
        heart_eight = Card(Card.Suit.HEARTS, Card.Face.EIGHT)
        heart_eight.set_round(self.round)
        heart_jack = Card(Card.Suit.HEARTS, Card.Face.JACK)
        heart_jack.set_round(self.round)
        diamond_ten = Card(Card.Suit.DIAMOND, Card.Face.TEN)
        diamond_ten.set_round(self.round)

        self.assertEqual(club_ace > club_jack, False)
        self.assertEqual(club_jack > club_ace, True)
        self.assertEqual(heart_eight > club_ace, False)
        self.assertEqual(club_ace > heart_eight, True)
        self.assertEqual(club_jack > heart_eight, True)
        self.assertEqual(heart_eight > heart_seven, True)
        self.assertEqual(heart_seven > heart_eight, False)
        self.assertEqual(diamond_ten > heart_eight, False)
        self.assertEqual(heart_eight > diamond_ten, False)

        self.round.set_type(Round.Type.GRAND)

        self.assertEqual(club_ace > club_jack, False)
        self.assertEqual(club_jack > club_ace, True)
        self.assertEqual(club_jack > heart_eight, True)
        self.assertEqual(heart_eight > club_jack, False)
        self.assertEqual(heart_eight > heart_seven, True)
        self.assertEqual(heart_seven > heart_eight, False)
        self.assertEqual(heart_jack > club_jack, False)
        self.assertEqual(club_jack > heart_jack, True)
        self.assertEqual(heart_jack > heart_eight, True)
        self.assertEqual(heart_eight > heart_jack, False)
        self.assertEqual(diamond_ten > heart_eight, False)
        self.assertEqual(heart_eight > diamond_ten, False)

        self.round.set_type(Round.Type.NULL)

        self.assertEqual(club_ace > club_jack, True)
        self.assertEqual(club_jack > club_ace, False)
        self.assertEqual(club_jack > heart_eight, False)
        self.assertEqual(heart_eight > club_jack, False)
        self.assertEqual(heart_eight > heart_seven, True)
        self.assertEqual(heart_seven > heart_eight, False)
        self.assertEqual(heart_jack > club_jack, False)
        self.assertEqual(club_jack > heart_jack, False)
        self.assertEqual(heart_jack > heart_eight, True)
        self.assertEqual(heart_eight > heart_jack, False)
        self.assertEqual(diamond_ten > heart_eight, False)
        self.assertEqual(heart_eight > diamond_ten, False)

    def test_is_trump(self):
        self.round.set_type(Round.Type.CLUB)

        # check trump cards
        for card in self.hand.cards:
            self.assertEqual(card.is_trump(), True)

        # chech non trump cards
        for card in self.deck.cards:
            card.set_round(self.round)
            self.assertEqual(card.is_trump(), False)

        self.round.set_type(Round.Type.CLUB)
