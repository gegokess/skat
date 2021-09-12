from round import Round
from player import Player
from deck import Deck
from hand import Hand

d = Deck()
h1 = Hand(d.draw_hand())
p = Player("Test")
p.set_hand(h1)
print(p.hand)

r = Round(2)
r.set_declarer(p)
print(r.get_multiplier())
