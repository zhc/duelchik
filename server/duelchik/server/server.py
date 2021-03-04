import traceback
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from duelchik.core import Lobby
from duelchik.server.models import TokenRequest, TokenResponse,\
        DuelchikRequest, DuelchikResponse
from duelchik.server.message import Message, ErrorMessage


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


@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.post('/api/get_token', response_model=TokenResponse)
def api_get_token(request: TokenRequest):
    session = str(request.session)
    token = lobby.get_token(session)
    return TokenResponse(token=token)


@app.post('/api/get_message', response_model=DuelchikResponse)
def api_get_message(request: DuelchikRequest):
    try:
        player = lobby.get_message(request.token, request.move_card)
        return Message(player).response()
    except Exception:
        msg = traceback.format_exc()
        return ErrorMessage(msg).response()
