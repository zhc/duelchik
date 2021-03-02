from typing import List
from pydantic import BaseModel


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
