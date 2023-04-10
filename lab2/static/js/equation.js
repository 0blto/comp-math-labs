function fromInputEquation() {
    solveEquation(parseInt(getEquation()), parseInt(getMethod()), checkIntervals(), checkEpsilon())
}

function fromFileEquation(input) {
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
    input.value = ''
    for (let i = 0; i < out.length; i++) {
        if (isNaN(out[i])) {
            oops('Входной файл должен содержать только числа')
            return
        }
    }
    if (out[out.length - 1] == ' ' || out[out.length - 1] == '') {
        out.pop()
    }

    if (out.length !== 5) {
        oops('Файл должен содержать 5 числел')
        return
    } 
    console.log(out)
    solveEquation(parseFloat(out[0]), parseFloat(out[1]), {min: parseFloat(out[2]), max: parseFloat(out[3])}, parseFloat(out[4]))
}


async function solveEquation(equation, method, interval, epsilon) {
    if (interval === false || 
        epsilon === false) return
    
    let data
    if (interval === true) {
        data = {equation,method,epsilon}
    } else {
        const left = interval.min, right = interval.max
        data = {equation,method,left,right,epsilon}
    }

    

    let answer = await requestData('/api/equation', data)

    if (answer === false) return

    let root = equation_answer(answer)

    const start = interval.min, end = interval.max

    let plt = await requestPlt('/api/equation_plt', {equation, root, start, end})

    if (plt === false) return

    const imageURL = URL.createObjectURL(plt)
    const answer_dom = document.querySelector('.plot')
    answer_dom.innerHTML = ''
    const img = new Image()
    img.src = imageURL
    answer_dom.appendChild(img)
}