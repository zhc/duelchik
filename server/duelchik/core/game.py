from uuid import uuid4


class Game:

    def __init__(self):
        self.sessions = {}

    def get_token(self, session):
        if session not in self.sessions:
            self.sessions[session] = []
        if len(self.sessions[session]) < 2:
            token_uuid = str(uuid4())
            self.sessions[session].append(token_uuid)
            return token_uuid
        return ''
