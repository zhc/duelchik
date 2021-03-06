"use strict";

import Vue from 'vue';
import Vuex from 'vuex';
import * as actions from './actions.js';
import * as getters from './getters.js';
import mutations from './mutations.js';
import queryString from 'query-string';

Vue.use(Vuex);

const parsedQueryString = queryString.parse(location.hash);

const state = {
    host: 'http://' + window.location.hostname + ':8080',
    session: parsedQueryString.d,
    token: '',
    pingTimer: null,
    game: {
        state: '',
        error_message: '',
        size: 25,
        deck: [1, 4, 6, 1],
        win: 0,
        your_index: 8,
        enemy_index: 24,
        stack_size: 20,
    }
};

const store = new Vuex.Store({
    state,
    getters,
    actions,
    mutations,
});

export default store;
