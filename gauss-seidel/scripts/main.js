const input_text = '<div id="text-input">\\(\\epsilon = \\)<input type="text" class="def-inp" value="0.01" id="eps"><br><br><select id="size" onchange="createMatrix()"><option selected="selected" value="3">3</option><option value="4">4</option><option value="5">5</option><option value="6">6</option><option value="7">7</option><option value="8">8</option><option value="9">9</option><option value="10">10</option><option value="11">11</option><option value="12">12</option><option value="13">13</option><option value="14">14</option><option value="15">15</option><option value="16">16</option><option value="17">17</option><option value="18">18</option><option value="19">19</option><option value="20">20</option></select> <br> <br><div id="matrix"> </div></div>',
    file_input = '<div id="file-input"><input type="file" style="z-index: 1000;" onchange="fromFileData(this)"></div>'

let file_mode = false,
    matrixA = new Array(),
    matrixB = new Array(),
    num = 3,
    E = 0.01

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
        correctInput(reader.result)
    }
    reader.onerror = function() {
        oops('Ошибка считывания файла')
    }
}

function correctInput(result) {
    let out = result.replace('\r', ' ').replace('\n', ' ').split(/\s+/)
    for (let i = 0; i < out.length; i++) {
        if (isNaN(out[i])) {
            oops('Проверьте входной файл')
            return
        }
    }
    if (out[out.length - 1] == ' ' || out[out.length - 1] == '') {
        out.pop()
    }

    if (out.length < 3) {
        oops('Данных слишком мало')
        return
    } 
    E = parseFloat(out[0])
    num = parseInt(out[1])
    
    out.shift()
    out.shift()
    if (isNaN(num) || num * num + num != out.length) { 
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
                matrixB.push(array[i+j])
            } else {
                matrixA[i].push(array[i+j])
            }
        }
    }
    
}



function method() {
    if (!validateE(E)) {
        return
    }
    
    let indexes = isDiagonalResponsive(matrixA)
    if (indexes === false) {
        return
    } else {
        matrixA = translate(matrixA, indexes)
        slau(matrixA, matrixB)
    }
    

    let n = matrixA.length,
    X = new Array(),
    x = new Array(),
    table = new Array()
    table.push(new Array())
    for (let i = 0; i < n; i++) {
        x[i] = 0
        X[i] = matrixB[i] / matrixA[i][i];
        table[0].push(X[i]) 
    }
    contin = true
     
    let limit = 500, 
        k = 1
    while (contin && k < limit ) {
        table.push(new Array())
        for (let i=0; i < n; i++) {
            let sum = 0
            for (let j = 0; j < i; j++) {
                    sum = sum + matrixA[i][j] * x[j]
            }
            for (let j = i + 1; j < n; j++) {
                    sum = sum + matrixA[i][j] * X[j]
            }
            x[i] = (matrixB[i] - sum) / matrixA[i][i]
            table[k].push(x[i])
        }
        
        let sum1 = 0.0
        let sum2 = 0.0
        for (let i = 0; i < n; i++) {
            sum1 += x[i]
            sum2 += X[i]
            table[k].push(Math.abs(x[i] - X[i]))
        }
        

        if (parseFloat(Math.abs(sum1 - sum2)) < E) {
            contin = false;
        } else {
            X=x.slice(0);
        }
        k++;
    }
    results(table)
}

function clr() {
    matrixA = new Array()
    matrixB = new Array()
    if (!file_mode) {
        createMatrix()
    } else {
        document.querySelector('input[type="file"]').value = ''
    }
    document.getElementById('results').innerHTML = ''
}

function calc() {
    if (file_mode) {
        method()
    } else {
        readFromInput()
        method()
    }
}

document.onload = createMatrix()

document.getElementById('switch').addEventListener('click', () => {
    if (!file_mode) {
        document.querySelector('.switch-container').innerHTML = file_input
    } else {
        document.querySelector('.switch-container').innerHTML = input_text
        createMatrix()
    }
    MathJax.typeset()
    file_mode = !file_mode
})

document.getElementById('eps').oninput = function() {
    E = document.getElementById('eps').value
}

const roll = document.getElementById("roll")
    
roll.oninput = function() {
    document.getElementById('get_val').value = roll.value
}


