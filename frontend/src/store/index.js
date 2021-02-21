"use strict";

import Vue from 'vue';
import Vuex from 'vuex';
import * as actions from './actions.js';
import * as getters from './getters.js';
import mutations from './mutations.js';

Vue.use(Vuex);

const state = {
    game: {
        state: '',
        error_message: ',',
        size: 25,
        deck: [1, 4, 6, 1],
        win: -1,
        your_index: 0,
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