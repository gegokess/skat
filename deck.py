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


