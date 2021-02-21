"use strict";

import * as api from '../api';

export const getMessage = ({commit, state}, payload) => {
    return api.getMessage(
        payload,
        (json) => {
            console.log(json);
            commit('setGameState', json);
        },
        (er) => {
            console.error(er);
        },

    );
};