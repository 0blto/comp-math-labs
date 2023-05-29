function imageReciever(response) {
    return response.blob()
}

function jsonReciever(response) {
    return response.json()
}

async function recieve(response, type) {
    try {
        if (!response.ok) {errtext = await response.text(); throw new Error(errtext)}
        return type(response)
    } catch (ex) {
        oops(ex)
        return false
    }
}