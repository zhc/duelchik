from unittest import TestCase
from duelchik.core import Game


class TestGame(TestCase):

    def setUp(self) -> None:
        self.game = Game()

    def test_auth(self):
        session = '123'
        token1 = self.game.get_token(session)
        token2 = self.game.get_token(session)
        token3 = self.game.get_token(session)
        self.assertTrue(len(token1) > 0)
        self.assertTrue(len(token2) > 0)
        self.assertEqual(0, len(token3))
        self.assertNotEqual(token1, token2)
