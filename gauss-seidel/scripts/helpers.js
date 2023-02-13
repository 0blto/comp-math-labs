function validateE(e) {
    if (isNaN(e) || e == '') {
        oops('Некоректное значение \\(\\epsilon\\)')
        return false
    }
    return true
}

function isNorm(array, index) {
    let sum = 0;
    for (let i = 0; i < array.length; i++) {
        if (index !== i) {
            sum += Math.abs(array[i])
        }
    }
    return Math.abs(array[index]) > sum
    
}

function isDiagonalResponsive(matrix) {
    let n = matrix.length
    let array = new Array()
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (isNorm(matrix[i], j)) {   
                if (array.includes(j)) {
                    oops('Матрица не диагонально преобладающая')
                    return false
                }
                array.push(j)
                break
            }
        }
    }

    const answer = (array.length === matrix.length) ? array : false
    if (answer === false) {
        oops('Матрица не диагонально преобладающая')
    }
    return answer
}

function translate(matrix, array) {
    let m = new Array(),
        b = Array()
    for (let i = 0; i < matrix.length; i++) {
        m[array[i]] = matrix[i] 
        b[array[i]] = matrixB[i]
    }
    matrixB = b
    return m
}

