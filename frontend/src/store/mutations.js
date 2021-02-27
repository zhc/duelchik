import queryString from 'query-string';

export default {
    setGameState(state, data) {
        state.game = data;
    },
    setState(state, data) {
        state.game.state = data;
    },
    setToken(state, data) {
        state.token = data;
    },
    setHost(state, data) {
        state.host = data;
    },
    setPingTimer(state, data) {
        state.pingTimer = data;
    },
    setSession(state, data) {
        state.session = data;

        const parsedQueryString = queryString.parse(location.hash);
        parsedQueryString.d = data;
        const stringquery = queryString.stringify(parsedQueryString);
        location.hash = stringquery;
    }
}
