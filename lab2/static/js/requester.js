function requestData(url, data) {

    const attr = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    }

    return fetch(url, attr)
    .then(async (response) => {
        if (!response.ok) {
            errtext = await response.text()
            throw new Error(errtext)
        }
        return response.json()
    }).catch(ex => {
        oops(ex)
        return false
    })
}