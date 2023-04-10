function fromInputSystem() {
    solveSystem(parseInt(getSystem()), checkIntervals(), checkEpsilon())
}

function systemFromFile(input) {
    let file = input.files[0]
    let reader = new FileReader()
    reader.readAsText(file)
    reader.onload = function() {
        correctInputSystem(reader.result, input)
    }
    reader.onerror = function() {
        oops('Ошибка считывания файла')
    }
}

function correctInputSystem(result, input) {
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

    if (out.length !== 4) {
        oops('Файл должен содержать 4 числа')
        return
    } 
    console.log(out)
    solveSystem(parseFloat(out[0]), {min: parseFloat(out[1]), max: parseFloat(out[2])}, parseFloat(out[3]))
}

async function solveSystem(system, interval, epsilon) {
    
    if (interval === false || 
        epsilon === false) return
    
    const left = interval.min, right = interval.max
    console.log(interval, left, right)
    const data = {system,left,right,epsilon}

    console.log(data)

    let answer = await requestData('/api/system', data)

    if (answer === false) return
    console.log (answer)

    let root = system_answer(answer)

    let x = root[0]

    let y = root[1]

    let plt = await requestPlt('/api/system_plt', {system, x, y})

    if (plt === false) return

    const imageURL = URL.createObjectURL(plt)
    const answer_dom = document.querySelector('.plot')
    answer_dom.innerHTML = ''
    const img = new Image()
    img.src = imageURL
    answer_dom.appendChild(img)
}