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
        self.trick_stack = dict()  # {game_round: [(player, card), ...]}

    def set_hand(self, hand):
        self.hand = hand

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
        return "id=" + str(id) + "name=" + self.name + " cards=" + str(self.cards)

    def __eq__(self, other):
        return other is not None and self.id is other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.id, self.name))
