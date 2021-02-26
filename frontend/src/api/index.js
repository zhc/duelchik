export function getMessage(token, moveCard, cb, errCb) {
    return fetch('http://localhost:8080/api/get_message', {
        method: 'POST',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'token': token,
            'move_card': moveCard
        })
    }).then((response) => {
        return response.json();
    }).then(json => {
        cb(json);
    }).catch(er => {
        errCb(er);
    });
}

export function ping(token, cb, errCb) {
    return fetch('http://localhost:8080/api/get_message', {
        method: 'POST',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'token': token,
            'move_card': 0
        })
    }).then((response) => {
        return response.json();
    }).then(json => {
        cb(json);
    }).catch(er => {
        errCb(er);
    });
}

export function getToken(cb, errCb) {
    return fetch('http://localhost:8080/api/get_token', {
        method: 'POST',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'session': 'string',
        })
    }).then((response) => {
        return response.json();
    }).then(json => {
        cb(json);
    }).catch(er => {
        errCb(er);
    });
}
