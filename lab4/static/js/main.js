async function calc(data) {
    const answers = await recieve(await requestData('/api/approximate', data), jsonReciever)
    if (answers === false) return
    results(answers)

    const plot = await recieve(await requestData('/api/plot', {}), imageReciever)
    if (plot === false) return
    drawPlot(plot)
}

