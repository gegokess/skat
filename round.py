from enum import Enum


class Round:
    # Defines one round in a skat game
    def __init__(self, number):
        #self.id = uuid()
        self.number = number  # round number within a game
        self.is_declared = False
        self.is_finished = False
        self.is_won = None
        self.type = Round.Type.CLUB
        self.variant = None
        self.points = None
        self.highest_bid = None
        self.trick_stack = list()
        self.declarer = None  # player who is the declarer

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

    def is_suit(self):
        # returns True if the round is declared to be a suit game
        return self.type in [
            Round.Type.CLUB,
            Round.Type.SPADE,
            Round.Type.HEART,
            Round.Type.DIAMOND
        ]

    def get_type(self):
        return self.type

    def is_grand(self):
        return self.type == Round.Type.GRAND

    def is_NULL(self):
        return self.type == Round.Type.NULL

    def set_declarer(self, declarer):
        self.declarer = declarer
        return True

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
