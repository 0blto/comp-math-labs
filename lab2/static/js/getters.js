function unpack(name) {
    const val = document.getElementById(name)
    if (val) return val.value
    oops(`Ошибка распаковки ${name}`)
    return undefined
}

function getInt1() {
    return unpack('int1')
}

function getInt2() {
    return unpack('int2')
}

function getEps() {
    return unpack('eps')
}

function getAutoIntervals() {
    return document.querySelectorAll('#search:checked').length != 0
}


function getEquation() {
    try {
        return document.querySelectorAll('input[name="equations"]:checked')[0].value
    } catch(ex) {
        oops(ex)
    }
}

function getSystem() {
    try {
        return document.querySelectorAll('input[name="systems"]:checked')[0].value
    } catch(ex) {
        oops(ex)
    }
}

function getMethod() {
    try {
        return document.querySelectorAll('input[name="method"]:checked')[0].value
    } catch(ex) {
        oops(ex)
    }
}