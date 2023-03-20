async function solveEquation() {
    const equation = parseInt(getEquation()),
        method = parseInt(getMethod()),
        interval = checkIntervals(),
        epsilon = checkEpsilon()
    
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

    equation_answer(answer)
    
}