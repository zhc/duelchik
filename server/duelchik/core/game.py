from duelchik.core.player import Player
from duelchik.core.deck import Deck


class Game:

    def __init__(self):
        self.size = 23
        self.players = []
        self.deck = Deck([1, 2, 3, 4, 5]*5)
        self.hand_size = 5

    def create_player(self):
        if len(self.players) == 0:
            self.players.append(Player(self.size))
            return self.players[0]
        elif len(self.players) == 1:
            self.players.append(Player(self.size))
            self.begin_game()
            return self.players[1]
        return None

    def begin_game(self):
        self.players[0].start(self.players[1])
        for player in self.players:
            for i in range(self.hand_size):
                card = self.deck.next_card()
                player.take(card)

    def has_players(self):
        return len(self.players) == 2

    def turn(self, player, move_card):
        if not self.has_players():
            return player

        if player.is_blocked():
            player.hurt()
        elif move_card > 0:
            player.forward(move_card)
        elif move_card < 0:
            player.backward(-move_card)
        elif player.are_empty_hands():
            player.hurt_on_game_over()

        self.deal_card(player)
        return player

    def deal_card(self, player):
        while len(player.cards) < self.hand_size and not self.deck.empty():
            card = self.deck.next_card()
            player.take(card)
