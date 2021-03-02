from duelchik.core.player import Player
from duelchik.core.deck import Deck


class Game:

    def __init__(self):
        self.size = 23
        self.players = []
        self.deck = Deck([1, 2, 3, 4, 5]*5)

    def create_player(self):
        if len(self.players) == 0:
            self.players.append(Player(self.size))
            return self.players[0]
        elif len(self.players) == 1:
            self.players.append(Player(self.size))
            self.players[0].start(self.players[1])
            for player in self.players:
                for i in range(5):
                    card = self.deck.next_card()
                    player.take(card)
            return self.players[1]
        return None

    def has_players(self):
        return len(self.players) == 2

    def turn(self, player, move_card):
        if not self.has_players():
            return player
        if player.is_active and not player.has_moves():
            player.hurt()
        elif move_card > 0:
            player.forward(move_card)
        elif move_card < 0:
            player.backward(-move_card)
        else:
            if len(player.cards) == 0 and len(player.enemy.cards) == 0:
                if player.position < player.enemy.position:
                    player.hurt()
                elif player.position == player.enemy.position:
                    player.hurt()
                    player.enemy.hurt()
        while len(player.cards) < 5 and not self.deck.empty():
            card = self.deck.next_card()
            player.take(card)
        return player
