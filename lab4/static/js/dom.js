const input_text = '\\(n = \\)<select class="def-inp" id="size" onchange="createMatrix()"><option selected="selected" value="8">8</option><option value="9">9</option><option value="10">10</option><option value="11">11</option><option value="12">12</option></select> <br> <br><div id="matrix"> </div></div>',
    file_input = '<div id="file-input"><input type="file" style="z-index: 1000;" onchange="fromFileData(this)"></div>',
    controller = '<button onclick="readFromInput()">Calculate</button>'

let file_mode = false

function oops(msg) {
    Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: msg,
        showClass: {
          popup: 'animate__animated animate__fadeIn'
        },
        hideClass: {
          popup: 'animate__animated animate__fadeOut'
        }
      })
}

function share() {
  Swal.fire({
    title: 'Drainer',
    text: 'Lab №4, computational math',
    imageUrl: '../static/resources/achi-kochi.gif',
    padding: '3em',
    color: '#716add',
    timer: 10000,
    timerProgressBar: true
    })
}

function createMatrix() {   
    let res = '<table>', size = document.getElementById('size'),
        n = size.options[size.selectedIndex].value*1
        num = n
    
    for (let i = 0; i < 2; i++) {
        res += '<tr style="border: 1px solid #eeeee;">'
        if (i === 0) res += '<td style="border: 1px solid #eeeeee; padding: 0; margin: 0; height: 2.5em; background-color: #9b9b9b8e;">X</td>'
        else res += '<td style="border: 1px solid #eeeeee; padding: 0; margin: 0; height: 2.5em; background-color: #9b9b9b8e;">Y</td>'
        for (let j = 0; j < n; j++) res += '<td style="border: 1px solid #eeeeee; padding: 0; margin: 0; height: 2.5em;"><input maxlength="10" class="element" type="text" id="a'+(i+1)+(j+1)+'" /></td>'
        res += '</tr>'
    }
    res += '</table>'
    document.getElementById('matrix').innerHTML = res
}

document.getElementById('switch').addEventListener('click', () => {
  if (!file_mode) {
      document.querySelector('.switch-container').innerHTML = file_input
      document.querySelector('.controller').innerHTML = ''
  } else {
      document.querySelector('.switch-container').innerHTML = input_text
      document.querySelector('.controller').innerHTML = controller
      createMatrix()
  }
  MathJax.typeset()
  file_mode = !file_mode
})

function results(answer) {
    const best = document.querySelector('.best'),
      functions = document.querySelector('.functions')
    best.innerHTML = `Best approximation type: ${answer.best}`
    html = '<table class="results"><thead><tr><th>Type</th><th>Function</th><th>$$\\sigma$$</th></tr></thead><tbody>'
    funcs = answer.functions
    for (let i = 0; i < funcs.length; i++) html += `<tr><td>${funcs[i].type}</td><td>$$y=${funcs[i].view}$$</td><td>${funcs[i].sqr}</td></tr>`
    html += '</tbody></table>'
    functions.innerHTML = html

    MathJax.typeset()
}

function drawPlot(plot) {
    const imageURL = URL.createObjectURL(plot)
    const answer_dom = document.querySelector('.plot')
    answer_dom.innerHTML = ''
    const img = new Image()
    img.src = imageURL
    answer_dom.appendChild(img)
}

function clr() {
    if (!file_mode) createMatrix()
    else document.querySelector('input[type="file"]').value = ''
    document.querySelector('.plot').innerHTML = ''
    document.querySelector('.functions').innerHTML = ''
    document.querySelector('.best').innerHTML = ''
}

document.onload = createMatrix()