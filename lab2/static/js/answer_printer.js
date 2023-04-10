function generate_tbody(answer) {
    let to_fill = ''
    to_fill += '<tbody>'
    for (let i = 0; i < answer.length; i++) {
        to_fill += '<tr>'
        to_fill += `<td>${i}</td>`
        for (let j = 0; j < answer[0].length; j++) {
            to_fill += `<td>${parseFloat(answer[i][j]).toFixed(3)}</td>`
        }
        to_fill += '</tr>'
    }
    to_fill += '</tbody>'
    return to_fill
}

function equation_answer(json) {
    success(json.message)
    const place = document.querySelector('.table'),
        result_place = document.querySelector('.result')
    let equation = '<div>',
        result = '<div>',
        iter = '<div>'


    place.innerHTML = ''

    switch(json.equation) {
        case 1:
            equation += '$$2.3x^3+5.75x^2-7.41x-10.6$$'
            break
        case 2:
            equation += '$$x^3-x+4$$'
            break
        case 3:
            equation += '$$sin(2x)+cos(x)$$'
            break
        default:
            oops('error')
    }
    equation += '</div>'

    result += `$$x=${parseFloat(json.solution.result).toFixed(3)}$$</div>`

    iter += '<table style="width: 100%; table-layout: fixed;">'
    iter += '<thead>'
    iter += '<tr>'
    switch(json.method) {
        case 1:
            iter += '<th>№</th>'
            iter += '<th>a</th>'
            iter += '<th>b</th>'
            iter += '<th>x</th>'
            iter += '<th>F(a)</th>'
            iter += '<th>F(b)</th>'
            iter += '<th>F(x)</th>'
            iter += '<th>\\(\\delta\\)</th>'
            break
        case 2:
            iter += '<th>№</th>'
            iter += '<th>\\(x_{i-1}\\)</th>'
            iter += '<th>\\(x_{i}\\)</th>'
            iter += '<th>\\(x_{i+1}\\)</th>'
            iter += '<th>\\(f(x_{i+1})\\)</th>'
            iter += '<th>\\(\\delta\\)</th>'
            break
        case 3:
            iter += '<th>№</th>'
            iter += '<th>\\(x_{i}\\)</th>'
            iter += '<th>\\(x_{i+1}\\)</th>'
            iter += '<th>\\(\\varphi(x_{i+1})\\)</th>'
            iter += '<th>\\(f(x_{i+1})\\)</th>'
            iter += '<th>\\(\\delta\\)</th>'
            break
        default:
            oops('error')
    }
    iter += '</tr>'
    iter += '</thead>'
    iter += generate_tbody(json.solution.table)
    console.log(json.solution.table[0].length)
    iter += '</table>'
    iter += '</div>'

    result_place.innerHTML = equation + result
    
    place.innerHTML = iter

    MathJax.typeset()

    return json.solution.result
}


function system_answer(json) {
    success(json.message)

    const place = document.querySelector('.table'),
        res = document.querySelector('.result')
    let equation = '<div>',
        result = '<div>',
        iter = '<div>'
    
    place.innerHTML = ''

    switch(json.system) {
        case 1:
            equation += '$$\\begin{cases}0.1x^2 + x + 0.2y^2 - 0.3 = 0\\\\0.2x^2 + y + 0.1xy - 0.7 = 0\\end{cases}$$'
            break
        case 2:
            equation += '$$\\begin{cases}x^2 + y^2 + x = 4\\\\y = 3x^2\\end{cases}$$'
            break
        default:
            oops('error') 
    }

    result += `$$x=${parseFloat(json.solution.result.x).toFixed(3)}$$ $$y=${parseFloat(json.solution.result.y).toFixed(3)}$$</div>`
    iter += '<table style="width: 100%; table-layout: fixed;">'
    iter += '<thead>'
    iter += '<tr>'
    iter += '<th>№</th>'
    iter += '<th>\\(x_{i-1}\\)</th>'
    iter += '<th>\\(y_{i-1}\\)</th>'
    iter += '<th>\\(x_{i}\\)</th>'
    iter += '<th>\\(y_{i}\\)</th>'
    iter += '<th>\\(\\delta_x\\)</th>'
    iter += '<th>\\(\\delta_y\\)</th>'
    iter += generate_tbody(json.solution.table)
    iter += '</table>'
    iter += '</div>'
    
    place.innerHTML = iter
    res.innerHTML = equation + result

    MathJax.typeset()

    return [json.solution.result.x, json.solution.result.y]
}