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

    def is_someone_dead(self):
        return self.enemy and (self.is_dead or self.enemy.is_dead)

    def is_blocked(self):
        return self.is_active and not self.has_moves()

    def are_empty_hands(self):
        return len(self.cards) == 0 and len(self.enemy.cards) == 0

    def hurt_on_game_over(self):
        if self.position < self.enemy.position:
            self.hurt()
        elif self.position == self.enemy.position:
            self.hurt()
            self.enemy.hurt()
