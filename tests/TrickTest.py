from trick import Trick
from deck import Deck
from player import Player
from round import Round
from card import Card
from hand import Hand
import unittest


class TrickTest(unittest.TestCase):

    def test_winning_card(self):
        p1 = Player("Player1")
        p2 = Player("Player2")
        p3 = Player("Player3")

        r = Round(1)
        r.set_declarer(p1)
        r.set_type(Round.Type.NULL)

        c1 = Card(Card.Suit.HEARTS, Card.Face.ACE)
        c2 = Card(Card.Suit.CLUB, Card.Face.JACK)
        c3 = Card(Card.Suit.DIAMOND, Card.Face.JACK)
        c1.set_round(r)
        c2.set_round(r)
        c3.set_round(r)

        t = Trick(r)

        t.add_card(p1, c1)
        t.add_card(p2, c2)
        t.add_card(p3, c3)

        self.assertEqual(t.get_winner(), p1)
        self.assertEqual(t.get_points(), 15)
