from unittest import TestCase
from duelchik.core import Game


class TestGame(TestCase):

    def setUp(self) -> None:
        self.game = Game()
