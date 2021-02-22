from random import shuffle


YOUR_TURN = 'YOUR_TURN'
ENEMY_TURN = 'ENEMY_TURN'
WAITING_PLAYER = 'WAITING_PLAYER'
GAME_OVER = 'GAME_OVER'
ERROR = 'ERROR'


class Message:
    def __init__(self, state=WAITING_PLAYER, error_message='',
                 deck=[], win=0, size=23, your_index=0, enemy_index=0,
                 stack_size=10):
        self.state = state
        self.error_message = error_message
        self.deck = deck
        self.win = win
        self.size = size
        self.your_index = your_index
        self.enemy_index = enemy_index
        self.stack_size = stack_size


class Deck:

    def __init__(self, cards):
        self.cards = cards
        shuffle(cards)

    def next_card(self):
        card = self.cards.pop()
        return card

    def empty(self):
        return len(self.cards) == 0


class Player:

    def __init__(self, size):
        self.size = size
        self.enemy = None
        self.position = 0
        self.cards = []
        self.is_active = False
        self.is_dead = False

    def start(self, enemy):
        self.enemy = enemy
        self.enemy.enemy = self
        self.is_active = True

    def forward(self, card):
        if not self.is_active:
            return
        if card not in self.cards:
            return
        if not self.can_move_forward(card):
            return
        self.position += card
        self.cards.remove(card)
        if self.position == self.size - self.enemy.position - 1:
            self.enemy.hurt()
        else:
            self.switch_turn()

    def backward(self, card):
        if not self.is_active:
            return
        if card not in self.cards:
            return
        if not self.can_move_backward(card):
            return
        self.position -= card
        self.cards.remove(card)
        self.switch_turn()

    def hurt(self):
        self.is_active = False
        self.enemy.is_active = False
        self.is_dead = True

    def switch_turn(self):
        self.is_active = False
        self.enemy.is_active = True

    def take(self, card):
        self.cards.append(card)

    def empty(self):
        return len(self.cards) == 0

    def has_moves(self):
        for card in self.cards:
            if self.can_move_forward(card):
                return True
            if self.can_move_backward(card):
                return True
        return False

    def can_move_forward(self, card):
        return self.position + card <= self.size - self.enemy.position - 1

    def can_move_backward(self, card):
        return self.position - card >= 0


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
        if not player.has_moves():
            player.hurt()
        if move_card > 0:
            player.forward(move_card)
        elif move_card < 0:
            player.backward(move_card)
        else:
            pass
        while len(player.cards) < 5 and not self.deck.empty():
            card = self.deck.next_card()
            player.take(card)
        return player
