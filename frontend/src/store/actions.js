"use strict";

import * as api from '../api';

export const ping = ({commit, state}) => {
    return api.ping(
        state.token,
        (json) => {
            console.log(json);
            commit('setGameState', json);
        },
        (err) => {
            console.error(err);
        }
    );
};

export const getMessage = ({commit, state}, moveCard) => {
    return api.getMessage(
        state.token,
        moveCard,
        (json) => {
            console.log(json);
            commit('setGameState', json);
        },
        (er) => {
            console.error(er);
        },
    );
};

export const getToken = ({commit, state}, sessionId) => {
    return api.getToken(
        sessionId,
        (json) => {
            console.log(json);
            commit('setToken', json.token);
        }, (err) => {
            console.error(err);
        })
};
