from uuid import uuid4
from duelchik.core.game import Game


class Lobby:

    def __init__(self):
        self.games = {}
        self.players = {}
        self.game_overs = {}

    def get_token(self, session):
        if session not in self.games:
            game = Game()
            game.session = session
            self.games[session] = game
        game = self.games[session]
        if not game.has_players():
            token_uuid = str(uuid4())
            player = game.create_player()
            self.players[token_uuid] = player, game
            return token_uuid
        return ''

    def get_message(self, token, move_card):
        player, game = self.players[token]
        player = game.turn(player, move_card)
        if player.is_someone_dead():
            if game.session not in self.game_overs:
                self.game_overs[game.session] = set()
            self.game_overs[game.session].add(token)
            self.clean_games()
        return player

    def clean_games(self):
        for session, token_set in list(self.game_overs.items()):
            if len(token_set) >= 2:
                for token in token_set:
                    del self.players[token]
                del self.games[session]
                del self.game_overs[session]
