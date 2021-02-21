from unittest import TestCase
from duelchik.core import Game, Player, YOUR_TURN, ENEMY_TURN, WAITING_PLAYER


class TestGame(TestCase):

    def setUp(self) -> None:
        self.game = Game()

    def test_add_player(self):
        self.assertFalse(self.game.has_players())
        self.game.add_player('token_1')
        self.assertFalse(self.game.has_players())
        self.game.add_player('token_2')
        self.assertTrue(self.game.has_players())

    def test_get_player(self):
        token = 'token'
        self.game.add_player(token)
        self.assertIsNotNone(self.game.get_player(token))

    def test_add_player_same_token(self):
        token = 'token'
        self.game.add_player(token)
        self.game.add_player(token)
        self.assertFalse(self.game.has_players())

    def test_game_start_state(self):
        self.game.add_player('token_1')
        self.game.add_player('token_2')
        player = self.game.get_player('token_1')
        message = player.get_message()
        self.assertEqual(YOUR_TURN, message.status)
        player = self.game.get_player('token_2')
        message = player.get_message()
        self.assertEqual(ENEMY_TURN, message.status)

    def test_game_wait_state(self):
        self.game.add_player('token_1')
        player = self.game.get_player('token_1')
        message = player.get_message()
        self.assertEqual(WAITING_PLAYER, message.status)
