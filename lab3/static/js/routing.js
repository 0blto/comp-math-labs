async function forward(url) {
    document.querySelector('main').innerHTML = await (await fetch(url, {method: 'POST'})).text()
    MathJax.typeset()
}