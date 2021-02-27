export default {
    setGameState(state, data) {
        state.game = data;
    },
    setToken(state, data) {
        state.token = data;
    },
    setHost(state, data) {
        state.host = data;
    },
    setPingTimer(state, data) {
        state.pingTimer = data;
    }
}
