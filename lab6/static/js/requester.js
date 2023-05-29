async function requestData(api, data) {
    return fetch(api, {
        method: 'POST',
        headers: {'Content-Type': 'application/json',},
        body: JSON.stringify(data)
    })
}