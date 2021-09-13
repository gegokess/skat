from card import Card
import random


class Deck():
    # Defines a deck during a skat round
    def __init__(self):
        self.cards = list()
        self.generate()

    def generate(self):
        # Generates a new shuffled 32-card deck
        for suit in Card.Suit.list():
            for face in Card.Face.list():
                self.add(Card(suit, face))
        self.shuffle()

    def add(self, card):
        # Adds a card to the deck
        self.cards.append(card)

    def size(self):
        # Return the size of the deck
        return len(self.cards)

    def draw(self):
        # Draw a card from the deck
        # Returns the drawn card
        if self.size():
            card = self.cards.pop()
            return card
        return False

    def draw_specific_card(self, card):
        if self.size():
            for deck_card in self.cards:
                if card == deck_card:
                    self.cards.remove(deck_card)
                    return card
        return False

    def draw_suit(self, suit):
        # draws all the cards with the given suit from the deck
        cards = list()
        if self.size():
            for card in self.cards:
                if card.has_suit(suit):
                    cards.append(card)
            for card in cards:
                self.draw_specific_card(card)
        return cards

    def draw_face(self, face):
        # draws all the cards with the given face from the deck
        cards = list()
        if self.size():
            for card in self.cards:
                if card.has_face(face):
                    cards.append(self.draw_specific_card(card))
        return cards

    def draw_n_cards(self, n):
        # Draws n number of cards
        cards = list()
        if self.size() >= n:
            for _ in range(n):
                cards.append(self.draw())
            return cards
        return False

    def draw_hand(self):
        # Draws 10 cards for a players hand
        return self.draw_n_cards(10)

    def draw_skat(self):
        # Draws two cards for the skat
        return self.draw_n_cards(2)

    def shuffle(self):
        # Shuffles the deck
        random.shuffle(self.cards)

    def __repr__(self):
        return self.cards.__str__()
