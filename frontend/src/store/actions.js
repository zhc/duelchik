"use strict";

import * as api from '../api';
import store from "./index";

export const ping = ({commit, state}) => {
    return api.ping(
        state.token,
        (json) => {
            console.log(json);
            commit('setGameState', json);
            commit('setPingTimer', setTimeout(() => {
                store.dispatch('ping');
            }, 3000));
        },
        (err) => {
            console.error(err);
        }
    );
};

export const pong = ({commit, state}) => {
    console.log('pong');
    clearTimeout(store.getters.pingTimer);
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

export const getToken = ({commit, state}) => {
    return api.getToken(
        store.getters.session,
        (json) => {
            console.log(json);
            if (json.token !== '') {
                commit('setToken', json.token);
                store.dispatch('ping');
            } else {
                commit('setState', 'EMPTY_TOKEN');
            }
        }, (err) => {
            console.error(err);
        })
};
