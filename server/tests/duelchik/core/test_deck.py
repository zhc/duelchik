
from unittest import TestCase
from duelchik.core import Deck


class TestDeck(TestCase):

    def setUp(self) -> None:
        self.deck = Deck([1, 2, 3, 4, 5]*5)

    def test_next_card(self):
        self.deck = Deck([5, 5])
        card = self.deck.next_card()
        self.assertEqual(5, card)
        self.assertFalse(self.deck.empty())

    def test_empty_deck(self):
        for i in range(25):
            self.deck.next_card()
        self.assertTrue(self.deck.empty())
