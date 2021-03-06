from unittest import TestCase
from duelchik.core import Player


class TestPlayer(TestCase):

    def setUp(self) -> None:
        size = 23
        self.player = Player(size)
        self.player.start(Player(size))

    def test_take_card(self):
        self.assertTrue(self.player.empty())
        self.player.take(1)
        self.assertListEqual([1], self.player.cards)
        self.assertFalse(self.player.empty())

    def test_move_backward(self):
        self.player.position = 3
        self.player.take(2)
        self.player.backward(2)
        self.assertEqual(1, self.player.position)
        self.assertListEqual([], self.player.cards)
        self.assertFalse(self.player.is_active)
        self.assertTrue(self.player.enemy.is_active)

    def test_move_forward(self):
        self.player.take(2)
        self.player.forward(2)
        self.assertEqual(2, self.player.position)
        self.assertListEqual([], self.player.cards)
        self.assertFalse(self.player.is_active)
        self.assertTrue(self.player.enemy.is_active)

    def test_move_forward_limit(self):
        self.player.enemy.position = 21
        self.player.take(2)
        self.player.forward(2)
        self.assertEqual(0, self.player.position)
        self.assertListEqual([2], self.player.cards)
        self.assertTrue(self.player.is_active)

    def test_move_backward_limit(self):
        self.player.take(2)
        self.player.backward(2)
        self.assertEqual(0, self.player.position)
        self.assertListEqual([2], self.player.cards)
        self.assertTrue(self.player.is_active)

    def test_forward_without_card(self):
        self.player.forward(2)
        self.assertEqual(0, self.player.position)

    def test_hurt(self):
        self.player.take(1)
        self.player.enemy.position = 21
        self.player.forward(1)
        self.assertFalse(self.player.is_active)
        self.assertFalse(self.player.enemy.is_active)
        self.assertTrue(self.player.enemy.is_dead)

    def test_no_moves(self):
        self.assertFalse(self.player.has_moves())

    def test_can_move_forward(self):
        self.player.take(100)
        self.player.take(1)
        self.player.take(100)
        self.assertTrue(self.player.has_moves())

    def test_no_moves_with_card(self):
        self.player.take(100)
        self.assertFalse(self.player.has_moves())

    def test_player_is_blocked(self):
        self.assertTrue(self.player.is_blocked())
        self.player.take(1)
        self.assertFalse(self.player.is_blocked())

    def test_both_has_empty_hands(self):
        self.assertTrue(self.player.are_empty_hands())
        self.player.take(1)
        self.assertFalse(self.player.are_empty_hands())

    def test_both_hurt(self):
        self.player.hurt_on_game_over()
        self.assertTrue(self.player.is_dead)
        self.assertTrue(self.player.enemy.is_dead)

    def test_hurt_on_low_position(self):
        self.player.enemy.position = 1
        self.player.hurt_on_game_over()
        self.assertTrue(self.player.is_dead)
        self.assertFalse(self.player.enemy.is_dead)
