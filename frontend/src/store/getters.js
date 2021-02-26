"use strict";
export const token = state => state.token;
export const state = state => state.game.state;
export const playerIndex = state => state.game.your_index;
export const enemyIndex = state => state.game.enemy_index;
export const deck = state => state.game.deck;
export const size = state => state.game.size;
export const win = state => state.game.win;
export const errorMessage = state => state.game.error_message;
