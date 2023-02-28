const input_text = '<div id="text-input">\\(\\epsilon = \\)<input type="text" class="def-inp" value="0.01" id="eps"><br><br>\\(n = \\)<select class="def-inp" id="size" onchange="createMatrix()"><option selected="selected" value="3">3</option><option value="4">4</option><option value="5">5</option><option value="6">6</option><option value="7">7</option><option value="8">8</option><option value="9">9</option><option value="10">10</option><option value="11">11</option><option value="12">12</option><option value="13">13</option><option value="14">14</option><option value="15">15</option><option value="16">16</option><option value="17">17</option><option value="18">18</option><option value="19">19</option><option value="20">20</option></select> <br> <br><div id="matrix"> </div></div>',
    file_input = '<div id="file-input"><input type="file" style="z-index: 1000;" onchange="fromFileData(this)"></div>'

let file_mode = false,
    matrixA = new Array(),
    matrixB = new Array(),
    num = 3,
    E = 0.01

const E_VAL = document.getElementById('eps')

function randInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function validateE() {
    if (isNaN(E_VAL.value) || E_VAL.value == '') {
        oops('Некоректное значение \\(\\epsilon\\)')
        MathJax.typeset()
        return false
    }
    return parseFloat(E_VAL.value)
}

function createMatrix() {   
    let res = '', size = document.getElementById('size'),
        n = size.options[size.selectedIndex].value*1
        num = n
    for (let i = 0; i < n; i++) { 
        for (let j = 0; j <= n; j++) { 
            res += '<input class="element" style="width: 30px; margin-bottom: 5px" type="text" id="a'+(i+1)+(j+1)+'" />' 
            if (j != n) {
                if (j != n - 1) {
                    res += ' \\(x_{' + (j+1) + '}\\) + '
                } else {
                    res += ' \\(x_{' + (j+1) + '}\\) = '
                }
            }
        }
       res += '<br>'
     }
    document.getElementById('matrix').innerHTML = res
    MathJax.typeset()
}

function fromFileData(input) {
    let file = input.files[0]
    let reader = new FileReader()
    reader.readAsText(file)
    reader.onload = function() {
        correctInput(reader.result, input)
    }
    reader.onerror = function() {
        oops('Ошибка считывания файла')
    }
}

function correctInput(result, input) {
    let out = result.replace('\r', ' ').replace('\n', ' ').split(/\s+/)
    for (let i = 0; i < out.length; i++) {
        if (isNaN(out[i])) {
            input.value = ''
            oops('Входной файл должен содержать только числа')
            return
        }
    }
    if (out[out.length - 1] == ' ' || out[out.length - 1] == '') {
        out.pop()
    }

    if (out.length < 3) {
        input.value = ''
        oops('Данных слишком мало')
        return
    } 
    E = parseFloat(out[0])
    num = parseInt(out[1])
    
    out.shift()
    out.shift()
    if (isNaN(num) || num * num + num != out.length) { 
        input.value = ''
        oops('Некорректный размер матрицы')
        return 
    }
    fillMatrixes(parseInt(num), out)
    
}

function readFromInput() {
    let array = new Array(),
        contin = true
    document.querySelectorAll('.element').forEach(el => {
        if (!isNaN(el.value) && el.value != '') {
            array.push(el.value)
        } else {
            contin = false
            oops('Проверьте содержимое ячеек')
        }
    })
    if (contin) {
        fillMatrixes(num, array)
    } else {
        matrixA = new Array()
        matrixB = new Array()
    }
}

function fillMatrixes(n, array) {
    matrixA = new Array()
    matrixB = new Array()
    
    for (let i = 0; i < n; i++) {
        matrixA.push(new Array())
        for (let j = i * n; j <= n + i * n; j++) {
            if (j === i * n + n) {
                matrixB.push(parseFloat(array[i+j]))
            } else {
                matrixA[i].push(parseFloat(array[i+j]))
            }
        }
    }
    
}

function clr() {
    matrixA = new Array()
    matrixB = new Array()
    E = 0.01
    if (!file_mode) {
        createMatrix()
    } else {
        document.querySelector('input[type="file"]').value = ''
    }
    document.getElementById('results').innerHTML = ''
    document.getElementById('system').innerHTML = ''
}

async function calc() {
    
    if (!file_mode) {
        readFromInput()
        E = validateE()
    } 

    if (E === false || matrixA.length === 0) return
    let answers = await fetch('/exec', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({E, num, matrixA, matrixB})
    }).then(async (response) => {
    if (!response.ok) {
        errtext = await response.text()
        throw new Error(errtext)
    }
    return response.json()
    }).catch(ex => {
        oops(ex)
        return false
    })
    if (answers === false) return
    answers = answers.results
    slau(answers.A, answers.B)
    results(answers.table)
}

document.onload = createMatrix()

document.getElementById('switch').addEventListener('click', () => {
    if (!file_mode) {
        document.querySelector('.switch-container').innerHTML = file_input
    } else {
        document.querySelector('.switch-container').innerHTML = input_text
        E = 0.01
        createMatrix()
    }
    MathJax.typeset()
    file_mode = !file_mode
})



const roll = document.getElementById("roll")
    
roll.oninput = function() {
    document.getElementById('get_val').value = roll.value
}


function generate_matrix() {
    document.querySelectorAll('.element').forEach(elem => {
        elem.value = randInt(-100, 100)
    })
}


