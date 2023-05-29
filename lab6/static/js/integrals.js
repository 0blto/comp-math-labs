async function solveIntegral() {
    const equation = parseInt(getEquation()),
        method = parseInt(getMethod()),
        interval = checkIntervals(),
        epsilon = checkEpsilon(),
        len = checkLen(),
        h = checkH()
    const x = interval.min, y = interval.max
    if (interval === false || 
        epsilon === false) return
    
    const data = {equation,method,x,y,epsilon, len, h}

    let answer = await recieve(await requestData('/api/diff_equation_solver', data), jsonReciever)

    if (answer === false) return

    resultTable(answer)

    let plt = await recieve(await requestData('/api/plot_equation', data), imageReciever)

    if (plt === false) return

    drawPlot(plt)
}

