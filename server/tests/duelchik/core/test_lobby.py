from unittest import TestCase
from duelchik.core import Lobby


class TestLobby(TestCase):

    def setUp(self) -> None:
        self.lobby = Lobby()

    def test_auth(self):
        session = '123'
        token1 = self.lobby.get_token(session)
        token2 = self.lobby.get_token(session)
        token3 = self.lobby.get_token(session)
        self.assertTrue(len(token1) > 0)
        self.assertTrue(len(token2) > 0)
        self.assertEqual(0, len(token3))
        self.assertNotEqual(token1, token2)

    def test_get_player_none(self):
        game = self.lobby.get_player('nonexisttoken')
        self.assertIsNone(game)

    def test_get_player(self):
        session = '123'
        token1 = self.lobby.get_token(session)
        game = self.lobby.get_player(token1)
        self.assertIsNotNone(game)
