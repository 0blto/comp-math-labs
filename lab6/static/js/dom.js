function drawPlot(plot) {
    const imageURL = URL.createObjectURL(plot)
    const answer_dom = document.querySelector('.plot')
    answer_dom.innerHTML = ''
    const img = new Image()
    img.src = imageURL
    answer_dom.appendChild(img)
}

function resultTable(data) {
    console.log(data)
    html = '<table class="results"><thead><tr><th>$$x$$</th><th>$$y$$</th><th>$$y\'$$</th><th>$$F(x, y)$$</th></thead><tbody>'
    for (let i = 0; i < data.x.length; i++) html += `<tr><td>${data.x[i]}</td><td>${data.y[i]}</td><td>${data.dy[i]}</td><td>${data.real[i]}</td>`
    html += '</tbody></table>'
    document.querySelector('.table').innerHTML = html
    MathJax.typeset()
}

function clr() {
    document.querySelector('.table').innerHTML = ''
    document.querySelector('.plot').innerHTML = ''
    document.getElementById('int1').value = ''
    document.getElementById('int2').value = ''
    document.getElementById('eps').value = '0.01'
    document.getElementById('h').value = ''
    document.getElementById('interval').value = ''
}