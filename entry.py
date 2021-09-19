from round import Round
from player import Player
from deck import Deck
from hand import Hand

d = Deck()
p = Player("Test")
r = Round(1)
r.set_declarer(p)
r.set_type(Round.Type.CLUB)
h1 = Hand(d.draw_hand(), r)


p.set_hand(h1)
print(p.hand)
p.get_hand().sort_hand()
print(p.hand)
