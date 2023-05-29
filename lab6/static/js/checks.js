function checkNumber(num) {
    return (!isNaN(num.replace(',', '.')) && num != '') ? parseFloat(num.replace(',', '.')) : false
}

function checkIntervals() {
    const int1 = checkNumber(getInt1()),
        int2 = checkNumber(getInt2())

    if (int1 === false || int2 === false) {
        oops('Интервал должен содержать числа')
        return false
    }

    return {min: int1, max: int2}
}

function checkEpsilon() {
    const retEps = checkNumber(getEps())
    if (retEps === false) oops('Проверьте значение epsilon')
    return retEps
}

function checkLen() {
    const retLen = checkNumber(getLen())
    if (retLen === false) oops('Проверьте значение длины промежутка')
    return retLen
}

function checkH() {
    const retH = checkNumber(getH())
    if (retH === false) oops('Проверьте значение длины шага')
    return retH
}