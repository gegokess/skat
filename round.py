from enum import Enum
from card import Card


class Round:
    # Defines one round in a skat game
    def __init__(self, number):
        #self.id = uuid()
        self.number = number  # round number within a game
        self.is_declared = False
        self.is_finished = False
        self.is_won = None
        self.type = None
        self.variant = None
        self.points = None
        self.highest_bid = None
        self.trick_stack = list()
        self.declarer = None  # player who is the declarer
        self.responder = None
        self.caller = None
        self.is_schneider = False
        self.is_schwarz = False

    class Type(Enum):
        CLUB = 12
        SPADE = 11
        HEART = 10
        DIAMOND = 9
        GRAND = 24
        NULL = 1

    class Variant(Enum):
        NORMAL = 1
        HAND = 2
        SCHNEIDER = 3
        SCHWARZ = 4
        OUVERT = 5

    def end(self):
        # ends the round and performs the necessary calculations
        self.calculate_points()

    def get_players(self):
        players = list()
        players.add(self.declarer, self.caller, self.responder)
        return players

    def set_finished(self):
        self.is_finished = True

    def is_suit(self):
        # returns True if the round is declared to be a suit game
        return self.type in [
            Round.Type.CLUB,
            Round.Type.SPADE,
            Round.Type.HEART,
            Round.Type.DIAMOND
        ]

    def calculate_points(self):
        self.calculate_winner()
        self.calculate_schneider()
        self.calculate_schwarz()

    def calculate_winner(self):
        # Check wether round was won
        if not self.is_finished():
            return None
        if self.is_NULL():
            self.is_won = self.declarer.hand.get_number_of_tricks() == 0
        self.is_won = self.declarer.hand.get_points() > 60
        self.set_finished()

    def calculate_schneider(self):
        # Check wether round was round with Schneider
        if self.is_finished() and not self.is_NULL():
            self.is_schneider = self.declarer.hand.get_points() > 89

    def calculate_schwarz(self):
        # Check wether round was round with Schwarz
        if self.is_finished() and not self.is_NULL():
            self.is_schwarz = self.declarer.hand.get_points() == 120

    def is_schwarz(self):
        if self.is_finished:
            return self.is_schwarz
        return False

    def get_trump_suit(self):
        if not self.is_suit():
            return False
        if self.type == Round.Type.CLUB:
            return Card.Suit.CLUB
        elif self.type == Round.Type.SPADE:
            return Card.Suit.SPADE
        elif self.type == Round.Type.HEART:
            return Card.Suit.HEARTS
        elif self.type == Round.Type.DIAMOND:
            return Card.Suit.DIAMOND

    def get_type(self):
        return self.type

    def is_grand(self):
        return self.type == Round.Type.GRAND

    def is_NULL(self):
        return self.type == Round.Type.NULL

    def set_declarer(self, declarer):
        self.declarer = declarer

    def get_declarer(self):
        return self.declarer

    def set_type(self, type):
        if self.declarer:
            self.type = type
            return True
        return False

    def get_multiplier(self):
        # Calculate the multiplier of the round
        if self.type == Round.Type.NULL:
            return 1
        else:
            return self.get_type_multiplier() * (self.get_jack_multiplier() + self.get_variant_multiplier() + 1)

    def get_jack_multiplier(self):
        if self.type == Round.Type.NULL:
            return 1
        else:
            return self.get_declarer().get_hand().get_jack_multiplier()

    def get_type_multiplier(self):
        return self.type.value

    def get_variant_multiplier(self):
        return int(self.is_hand()) + int(self.is_schneider()) + int(self.is_ouvert())

    def is_hand(self):
        if self.is_declared:
            return self.is_hand
        return False

    def is_ouvert(self):
        if self.is_declared:
            return self.is_ouvert
        return False

    def is_schneider(self):
        if self.is_finished:
            return self.is_schneider
        return False
