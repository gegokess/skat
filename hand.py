from card import Card


class Hand:
    # Defines a players hand during one round
    # of a skat game
    def __init__(self, cards):
        self.cards = cards
        self.jacks = self.get_jacks()

    # Sort Null
    # Sort Grand
    # Sort Suit

    def has_card(self, card):
        for hand_card in self.cards:
            if hand_card == card:
                return True
        return False

    def has_suit(self, suit):
        for card in self.cards:
            if card.has_suit(suit):
                return True
        return False

    def has_face(self, face):
        for card in self.cards:
            if card.has_face(face):
                return True
        return False

    def get_jack_multiplier(self):
        # returns the jack multiplier
        # generally the distance to the club jack defines the multiplier
        # however the presence of the club adds one on top
        if self.has_first_jack():
            return self.get_jacks_from_top() + 1
        else:
            return self.get_jacks_from_top()

    def get_jacks(self):
        # returns list of jacks on hand
        jacks = list()
        for card in self.cards:
            if card.has_face(Card.Face.JACK):
                jacks.append(card)
        jacks.sort(key=lambda x: x.suit.value, reverse=False)
        return jacks

    def get_jacks_from_top(self):
        # returns the difference between the club jack
        # and the next jack on the hand
        if self.jacks:
            return self.get_highest_jack().suit.value
        return 4

    def get_highest_jack(self):
        # get the highest jack of the hand
        if self.jacks:
            return self.jacks[0]
        return None

    def lay_card(self, card):
        # Lays card from hand
        # Returns removed card if found in hand
        if self.cards.remove(card):
            return card
        return False

    def has_first_jack(self):
        # checks wether the hand contains a club jack
        for card in self.jacks:
            if card == Card(Card.Suit.CLUB, Card.Face.JACK):
                return True
        return False

    def __repr__(self):
        return self.cards.__str__()
