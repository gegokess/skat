from enum import Enum


class Player:
    # Defines a player during a skat game
    class Type(Enum):
        DECLARER = 0
        DEFENDER = 1

    def __init__(self, name):
        self.name = name
        self.type = None
        self.hand = None
        self.tricks = list()

    def add_trick(self, trick):
        self.tricks.append(trick)
        return True

    def get_tricks_from_round(self, round):
        # gets all the tricks the player has won in a specific round
        tricks = list()
        if self.tricks:
            for trick in self.tricks:
                if trick.get_round() == round:
                    tricks.append(trick)
            return tricks
        return False

    def set_hand(self, hand):
        self.hand = hand

    def get_hand(self):
        return self.hand

    def sum_trick_values(self):
        sum_tricks = 0
        for trick in self.trick_stack.values():
            for entry in trick:
                sum_tricks += entry[1].get_value()

            return sum_tricks

    def has_card(self, card):
        return self.hand.has_card(card)

    def has_suit(self, suit):
        return self.hand.has_suit(suit)

    def has_face(self, face):
        return self.hand.has_face(face)

    def __repr__(self):
        return "id=" + str(id) + "name=" + self.name + " cards=" + str(self.hand)

    def __eq__(self, other):
        return other is not None and self.name is other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.id, self.name))
