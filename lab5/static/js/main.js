async function calc(data) {
    const answers = await recieve(await requestData('/api/interpolate', data), jsonReciever)
    if (answers === false) return
    const plt = await recieve(await requestData('/api/plot', data), imageReciever)
    drawPlot(plt)
    results(answers.finiteDiff)
    calculateButton(data)
}

