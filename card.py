# -*- coding: utf-8 -*-

from enum import Enum
from round import Round


class Card:
  # Defines a card within a deck
    class Face(Enum):
        SEVEN = 0
        EIGHT = 1
        NINE = 2
        TEN = 3
        JACK = 4
        QUEEN = 5
        KING = 6
        ACE = 7

        @staticmethod
        def to_display(suit):
            if suit is Card.Face.SEVEN:
                return str(7)
            elif suit is Card.Face.EIGHT:
                return str(8)
            elif suit is Card.Face.NINE:
                return str(9)
            elif suit is Card.Face.TEN:
                return str(10)
            elif suit is Card.Face.JACK:
                return "J"
            elif suit is Card.Face.QUEEN:
                return "Q"
            elif suit is Card.Face.KING:
                return "K"
            elif suit is Card.Face.ACE:
                return "A"

        @classmethod
        def list(cls):
            return list(cls)

    class Suit(Enum):
        CLUB = 0
        SPADE = 1
        HEARTS = 2
        DIAMOND = 3

        @staticmethod
        def to_display(suit):
            if suit is Card.Suit.DIAMOND:
                return "♦"
            elif suit is Card.Suit.HEARTS:
                return "♥"
            elif suit is Card.Suit.SPADE:
                return "♠"
            elif suit is Card.Suit.CLUB:
                return "♣"

        @classmethod
        def list(cls):
            return list(cls)

    def has_suit(self, suit):
        return self.suit == suit

    def has_face(self, face):
        return self.face == face

    def get_value(self):
        if self.face is Card.Face.JACK:
            return 2
        elif self.face is Card.Face.ACE:
            return 11
        elif self.face is Card.Face.TEN:
            return 10
        elif self.face is Card.Face.KING:
            return 4
        elif self.face is Card.Face.QUEEN:
            return 3
        else:
            return 0

    @staticmethod
    def jack_list():
        jacks = list()
        for suit in Card.Suit.list():
            print(suit)
            jacks.append(Card(suit, Card.Face.JACK))
        return jacks

    def set_round(self, round):
        # sets the round the card is played in
        self.round = round

    def get_round(self, round):
        # gets the round the card is played in
        return self.round

    def is_trump(self):
        # Checks wether or not the card is trump
        if self.round.is_NULL():
            return True
        elif self.round.is_grand():
            return self.has_face(Card.Face.JACK)
        elif self.round.is_suit():
            return 12 - self.suit.value == self.round.get_type().value

    def is_jack(self):
        return self.has_face(Card.Face.JACK)

    def is_not_jack(self):
        return not self.is_jack()

    def is_greater_NULL_game(self, other):
        # defines the greater comparision of two cards in a NULL game
        if self.has_suit(other.suit):
            return self.face.value > other.face.value
        return False

    def is_less_NULL_game(self, other):
        # defines the less comparision of two cards in a NULL game
        if not self.__eq__(other):
            return self.is_greater_NULL_game(other)
        return False

    def is_greater_non_NULL_game(self, other):
        # defines the greater comparision of two cards in a non NULL game

        # self is trump or jack while the other card isn't
        if self.is_trump() and not other.is_trump() or self.is_jack() and other.is_not_jack():
            return True

        # both are jacks
        elif self.is_jack() and other.is_jack():
            return self.suit.value < other.suit.value

        # both have the same suit and other is not a jack
        elif self.has_suit(other.suit) and other.is_not_jack():
            return self.face.value > other.face.value
        return False

    def is_less_non_NULL_game(self, other):
        # defines the less comparision of two cards in a non NULL game
        if self.__eq__(other):
            return False
        return not self.is_greater_non_NULL_game(other)

    def __init__(self, suit, face):
        self.suit = suit
        self.face = face
        self.round = None

    def __repr__(self):
        return Card.Face.to_display(self.face) + Card.Suit.to_display(self.suit)

    def __eq__(self, other):
        return other is not None and self.suit is other.suit and self.face is other.face

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.suit, self.face))

    def __gt__(self, other):
        if self.round.is_NULL():
            return self.is_greater_NULL_game(other)
        else:
            return self.is_greater_non_NULL_game(other)

    def __ge__(self, other):
        if self.__eq__(other):
            return True
        else:
            return self > other

    def __lt__(self, other):
        if self.round.is_NULL():
            return self.is_less_NULL_game(other)
        else:
            return self.is_less_non_NULL_game(other)

    def __le__(self, other):
        if self.__eq__(other):
            return True
        else:
            return self < other
