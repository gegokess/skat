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

    def set_declarer(self, declarer):
        self.declarer = declarer
        return True

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
            return self.type_multiplier() * (self.jack_multiplier() + self.variant_multiplier() + 1)

    def jack_multiplier(self):
        if self.type == Round.Type.NULL:
            return 1
        else:
            return self.declarer.hand.get_jack_multiplier()

    def type_multiplier(self):
        return self.type.value

    def variant_multiplier(self):
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
