import traceback
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel
from duelchik.core import Lobby


app = FastAPI()
lobby = Lobby()

origins = [
    'http://localhost:8888',
    'http://80.78.248.143:8888',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Message:

    def __init__(self, player):
        self.player = player

    def response(self):
        state = 'WAITING_PLAYER'
        if self.player.is_active:
            state = 'YOUR_TURN'
        elif self.player.enemy and self.player.enemy.is_active:
            state = 'ENEMY_TURN'
        elif self.player.is_game_over():
            state = 'GAME_OVER'
        error_message = ''
        win = 0
        if self.player.enemy and self.player.enemy.is_dead:
            win = 1
        enemy_index = self.player.size - 1
        if self.player.enemy:
            enemy_index = self.player.size - self.player.enemy.position - 1
        return DuelchikResponse(
                state=state,
                error_message=error_message,
                deck=self.player.cards,
                win=win,
                size=self.player.size,
                your_index=self.player.position,
                enemy_index=enemy_index,
                stack_size=23
                )


class TokenRequest(BaseModel):
    session: str


class TokenResponse(BaseModel):
    token: str


class DuelchikResponse(BaseModel):
    state: str
    error_message: str
    deck: List[int]
    win: int
    size: int
    your_index: int
    enemy_index: int
    stack_size: int


class DuelchikRequest(BaseModel):
    token: str
    move_card: int


@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.post('/api/get_token', response_model=TokenResponse)
def get_token(request: TokenRequest):
    session = str(request.session)
    token = lobby.get_token(session)
    return TokenResponse(token=token)


@app.post('/api/get_message', response_model=DuelchikResponse)
def surge_request(request: DuelchikRequest):
    try:
        token = request.token
        move_card = request.move_card
        player = lobby.get_message(token, move_card)
        message = Message(player)
        response = message.response()
        return response
    except Exception:
        msg = traceback.format_exc()
        print(msg)
        return DuelchikResponse(
                state='ERROR',
                error_message=msg,
                deck=[],
                win=0,
                size=0,
                your_index=0,
                enemy_index=0,
                stack_size=0
                )
