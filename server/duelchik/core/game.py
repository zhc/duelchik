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
        if self.position + card > self.size - self.enemy.position - 1:
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
        if self.position - card < 0:
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


class Game:

    def __init__(self):
        pass
