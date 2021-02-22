from unittest import TestCase
from duelchik.core import Game, Player, YOUR_TURN, ENEMY_TURN, WAITING_PLAYER, ERROR


class TestGame(TestCase):

    def setUp(self) -> None:
        self.game = Game()

