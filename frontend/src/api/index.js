export function getMessage(moveCard, cb, errCb) {
    return fetch('http://localhost:8080/api/get_message', {
        method: 'POST',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'token': 'string',
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