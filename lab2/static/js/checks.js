function checkNumber(num) {
    return (!isNaN(num) && num != '') ? parseFloat(num) : false
}

function checkIntervals() {
    if (getAutoIntervals()) return true
    const int1 = checkNumber(getInt1()),
        int2 = checkNumber(getInt2())

    if (int1 === false || int2 === false) {
        oops('Интервал должен содержать числа')
        return false
    }

    if (int1 >= int2) {
        oops('Начало интервала должно быть меньше конца')
        return false
    }

    return {min: int1, max: int2}
}

function checkEpsilon() {
    const ret_eps = checkNumber(getEps())
    if (ret_eps === false) oops('Проверьте значение epsilon')
    return ret_eps
}