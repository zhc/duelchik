from random import shuffle


YOUR_TURN = 'YOUR_TURN'
ENEMY_TURN = 'ENEMY_TURN'
WAITING_PLAYER = 'WAITING_PLAYER'
GAME_OVER = 'GAME_OVER'
ERROR = 'ERROR'


class Message:
    def __init__(self, status, cards, is_won=False,
                 your_index=0, enemy_index=0):
        self.status = status
        self.cards = cards
        self.is_won = is_won
        self.your_index = your_index
        self.enemy_index = enemy_index


class Player:

    def __init__(self, game):
        self.game = game
        self.position = 0
        self.cards = []
        self.is_won = False
        self.last_played_card = 0

    def get_message(self):
        if self.game.has_players():
            if self.game.game_over:
                return Message(GAME_OVER, self.cards, is_won=self.is_won,
                               your_index=self.position,
                               enemy_index=self.get_enemy().position)
            else:
                if self.game.current_player == self:
                    return Message(YOUR_TURN, self.cards, is_won=self.is_won,
                                   your_index=self.position,
                                   enemy_index=self.get_enemy().position)
                else:
                    return Message(ENEMY_TURN, self.cards,
                                   is_won=self.is_won,
                                   your_index=self.position,
                                   enemy_index=self.get_enemy().position)
        else:
            return Message(WAITING_PLAYER, self.cards)

    def move_card(self, card, sign):
        if card in self.cards:

            left_bound = 0
            right_bound = self.game.size - 1
            if self.game.left_player == self:
                right_bound = self.game.right_player.position
            if self.game.right_player == self:
                left_bound = self.game.left_player.position

            next_position = self.position + card*sign
            if next_position < left_bound or next_position > right_bound:
                raise Exception('Illegal move')

            self.position = next_position
            self.cards.remove(card)
            self.last_played_card = card

            if len(self.game.deck) > 0:
                self.add_card(self.game.deck.pop())

            if next_position == self.get_enemy().position:
                self.game.game_over = True
                self.is_won = True

    def add_card(self, card):
        self.cards.append(card)

    def get_enemy(self):
        if self.game.left_player == self:
            return self.game.right_player
        else:
            return self.game.left_player


class Game:

    def __init__(self):
        self.players = {}
        self.current_player = None
        self.left_player = None
        self.right_player = None
        self.size = 23
        self.deck = [1, 2, 3, 4, 5]*5
        shuffle(self.deck)
        self.game_over = False

    def add_player(self, token):
        if token not in self.players:
            player = Player(self)
            self.players[token] = player
            if self.left_player is None:
                self.left_player = player
                player.position = 0
            else:
                self.right_player = player
                player.position = self.size - 1
        if self.has_players():
            self.current_player = list(self.players.values())[0]
            self.deal_cards()

    def has_players(self):
        return len(self.players) >= 2

    def get_player(self, token):
        return self.players[token]

    def deal_cards(self):
        for i in range(5):
            self.left_player.add_card(self.deck.pop())
        for i in range(5):
            self.right_player.add_card(self.deck.pop())
