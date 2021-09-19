from card import Card


class Hand:
    # Defines a players hand during one round
    # of a skat game
    def __init__(self, cards, round):
        self.cards = cards
        self.round = round
        self.jacks = self.get_jacks()
        self.set_cards_round()
        self.tricks = list()

    def get_tricks(self):
        return self.tricks

    def get_points(self):
        points = 0
        for trick in self.get_tricks():
            points = trick.get_points() + points
        return points

    def get_number_of_tricks(self):
        return len(self.tricks)

    def sort_hand(self):
        if self.round.is_grand():
            self.sort_hand_for_grand()
        elif self.round.is_suit():
            self.sort_hand_for_suit()
        else:
            self.sort_hand_for_null()

    def sort_hand_for_null(self):
        # sorts the hand from heighest to lowest according to null game rules
        self.cards = sorted(self.cards, key=lambda x: (
            4 - x.suit.value, x.face.value), reverse=True)

    def sort_hand_for_grand(self):
        # sorts the hand from heighest to lowest according to grand game rules
        # basic order
        self.sort_hand_for_null()

        # add sorted jacks
        new_ordered_cards = self.get_jacks()

        # add rest of the cards
        new_ordered_cards.extend(self.get_cards_from_non_trump_suits())

        self.cards = new_ordered_cards

    def sort_hand_for_suit(self):
        # sorts the hand from heighest to lowest according to suit game rules
        # basic order

        # sort for null
        self.sort_hand_for_null()

        # add sorted jacks
        new_ordered_cards = self.get_jacks()

        # add sorted trump suit
        new_ordered_cards.extend(
            self.get_cards_from_trump_suit())

        # add rest of the cards
        new_ordered_cards.extend(
            self.get_cards_from_non_trump_suits())

        self.cards = new_ordered_cards

    def get_cards_from_trump_suit(self):
        return self.get_cards_depending_on_trump_status(True)

    def get_cards_from_non_trump_suits(self):
        return self.get_cards_depending_on_trump_status(False)

    def get_cards_depending_on_trump_status(self, trump):
        # returns the cards from the requested suit if trump==true,
        # otherwise returns all cards except the request trump cards
        # jacks are excluded
        cards = list()
        for card in self.cards:
            if card.is_trump() == trump and card.is_not_jack():
                cards.append(card)
        return cards

    def set_cards_round(self):
        for card in self.cards:
            card.set_round(self.round)

    def has_card(self, card):
        for hand_card in self.cards:
            if hand_card == card:
                return True
        return False

    def has_suit(self, suit):
        # checks wether the hand contains a card of the requested suit
        for card in self.cards:
            if card.has_suit(suit):
                return True
        return False

    def has_face(self, face):
        # checks wether the hand contains a card of the requested face
        for card in self.cards:
            if card.has_face(face):
                return True
        return False

    def get_jack_multiplier(self):
        # returns the jack multiplier
        # generally the distance to the club jack defines the multiplier
        # however the presence of the club adds one on top
        if self.has_first_jack():
            return self.get_lowest_successive_jack_from_highest_jack().suit.value + 1
        elif self.jacks:
            return self.get_highest_jack().suit.value
        return 4

    def get_jacks(self):
        # returns list of jacks in the hand
        jacks = list()
        for card in self.cards:
            if card.has_face(Card.Face.JACK):
                jacks.append(card)
        jacks.sort(key=lambda x: x.suit.value, reverse=False)
        return jacks

    def get_lowest_successive_jack_from_highest_jack(self):
        # Determines the lowest jack which is successive to the highest jack
        # in the hand
        if len(self.jacks) == 1:
            return self.get_highest_jack()
        elif len(self.jacks) == 2 and self.get_highest_jack().suit.value + 1 == self.get_lowest_jack().suit.value:
            return self.get_lowest_jack()
        elif len(self.jacks) == 3 and self.get_highest_jack().suit.value + 1 == self.get_lowest_jack().suit.value - 1:
            return self.get_lowest_jack()
        elif len(self.jacks) == 4:
            return self.get_lowest_jack()
        return self.get_highest_jack()

    def get_highest_jack(self):
        # get the highest jack of the hand
        if self.jacks:
            return self.get_jacks()[0]
        return None

    def get_lowest_jack(self):
        # get the highest jack of the hand
        if self.jacks:
            return self.jacks[len(self.jacks) - 1]
        return None

    def lay_card(self, card):
        # Lays card from hand
        # Returns layed card if found in the hand
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
