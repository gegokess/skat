class Trick():
    def __init__(self, round):
        self.round = round
        self.player_card_tuples = list()
        self.current_winning_tuple = None

    def add_card(self, player, card):
        # add a card to the trick ({"player" : Player, "card" : Card})
        # compares the played card to currently winning card
        # to determine the new currently winning card
        if len(self.player_card_tuples) <= 3:
            player_card_tuple = {"player": player, "card": card}
            # new current winning tuple if None so far or the new card
            # is higher than the old best
            if self.current_winning_tuple == None or card > self.current_winning_tuple["card"]:
                self.current_winning_tuple = player_card_tuple
            self.player_card_tuples.append(player_card_tuple)
            return True
        return False

    def give_trick_to_winner(self):
        if self.get_winner().add_trick(self):
            return True
        return False

    def get_points(self):
        # returns the total points of the trick
        points = 0
        for tuple in self.player_card_tuples:
            points += tuple["card"].get_value()
        return points

    def is_finished(self):
        return len(self.player_card_tuples) == 3

    def is_started(self):
        return len(self.player_card_tuples) > 0

    def get_winner(self):
        if self.is_finished():
            return self.current_winning_tuple["player"]
        return False

    def get_played_card_n(self, n):
        # returns the n-th card of the trick
        if len(self.player_card_tuples) >= n:
            return self.player_card_tuples[n]["card"]
        return False

    def get_player_of_played_card_n(self, n):
        # returns the n-th card of the trick
        if len(self.player_card_tuples) >= n:
            return self.player_card_tuples[n]["player"]
        return False
