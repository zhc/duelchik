from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel


app = FastAPI()

origins = [
    "http://localhost:8888",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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


@app.post('/api/get_message', response_model=DuelchikResponse)
def surge_request(request: DuelchikRequest):
    response = DuelchikResponse(
            state='WAITING_PLAYER',
            error_message='',
            deck=[1, 2, 3, 4, 5],
            win=0,
            size=25,
            your_index=0,
            enemy_index=24,
            stack_size=10,
            )
    return response
