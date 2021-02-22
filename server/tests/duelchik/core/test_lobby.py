from unittest import TestCase
from duelchik.core import Lobby


class TestLobby(TestCase):

    def setUp(self) -> None:
        self.lobby = Lobby()
