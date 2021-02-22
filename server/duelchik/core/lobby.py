from uuid import uuid4
from duelchik.core.game import Game


class Lobby:

    def __init__(self):
        self.games = {}
        self.players = {}

    def get_token(self, session):
        if session not in self.games:
            game = Game()
            self.games[session] = game
        game = self.sessions[session]
        if not game.has_players():
            token_uuid = str(uuid4())
            player = game.register_token(token_uuid)
            self.players[token_uuid] = player, game
            return token_uuid
        return ''

    def get_message(self, token, move_card):
        player, game = self.players[token]
        return game.turn(player, move_card)
