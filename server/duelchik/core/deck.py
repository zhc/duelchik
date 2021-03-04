from random import shuffle


class Deck:

    def __init__(self, cards):
        self.cards = cards
        shuffle(cards)

    def next_card(self):
        card = self.cards.pop()
        return card

    def empty(self):
        return len(self.cards) == 0
