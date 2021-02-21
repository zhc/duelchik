
from uuid import uuid4
from duelchik.core.game import Game


class Lobby:

    def __init__(self):
        self.sessions = {}
        self.tokens = {}

    def get_token(self, session):
        if session not in self.sessions:
            game = Game()
            self.sessions[session] = game
        game = self.sessions[session]
        if not game.has_players():
            token_uuid = str(uuid4())
            game.add_player(token_uuid)
            self.tokens[token_uuid] = game
            return token_uuid
        return ''

    def get_player(self, token):
        if token in self.tokens:
            game = self.tokens[token]
            return game.get_player(token)
        return None
