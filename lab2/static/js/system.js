async function solveSystem() {
    const system = parseInt(getSystem()),
        interval = checkIntervals(),
        epsilon = checkEpsilon()
    
    if (interval === false || 
        epsilon === false) return
    
    const left = interval.min, right = interval.max
    const data = {system,left,right,epsilon}

    let answers = await requestData('/api/system', data)

    console.log(answers)
}