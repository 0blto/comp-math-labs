const input_text = '\\(n = \\)<select class="def-inp" id="size" onchange="createMatrix()"><option selected="selected" value="8">8</option><option value="9">9</option><option value="10">10</option><option value="11">11</option><option value="12">12</option></select> <br> <br><div id="matrix"> </div></div>',
    file_input = '<div id="file-input"><input type="file" style="z-index: 1000;" onchange="fromFileData(this)"></div>',
    controller = '<button onclick="generateByFunction()">Generate</button><button onclick="readFromInput()">Calculate</button>'

let file_mode = false

function success(msg) {
  Swal.fire({
      icon: 'success',
      title: 'Success',
      text: msg,
      showClass: {
        popup: 'animate__animated animate__fadeIn'
      },
      hideClass: {
        popup: 'animate__animated animate__fadeOut'
      }
    })
}

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
    title: 'Drain shawty',
    text: 'Lab №5, computational math',
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
        if (i === 0) res += '<td style="border: 1px solid #666666; padding: 0; margin: 0; height: 2.5em; background-color: #9b9b9b8e;">X</td>'
        else res += '<td style="border: 1px solid #666666; padding: 0; margin: 0; height: 2.5em; background-color: #9b9b9b8e;">Y</td>'
        for (let j = 0; j < n; j++) res += '<td style="border: 1px solid #666666; padding: 0; margin: 0; height: 2.5em;"><input maxlength="10" class="element" type="text" id="a'+(i+1)+(j+1)+'" /></td>'
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
    const finiteDiff = document.querySelector('.finite-diff'),
      values = answer
    html = '<table class="results"><thead><tr><th>\\(x_i\\)</th><th>\\(y_i\\)</th>'
    for (let i = 1; i < values.length - 1; i++) html += `<th>\\(\\Delta^{${i}} y_{i}\\)</th>`
    html == '</tr></thead><tbody>'
    for (let i = 0; i < values[0].length; i++) {
      html += '<tr>'
      for (let j = 0; j < values.length; j++) {
        if (j > values.length - i - 1) html += '<td></td>'
        else html += `<td>$$${values[j][i]}$$</td>`
      }
      html += '</tr>'
    }
    html += '</tbody></table>'
    finiteDiff.innerHTML = html

    MathJax.typeset()
}

function calculateButton(data) {
  document.querySelector('.method').innerHTML = '<button id="get-lagrange">Метод Лагранжа</button><button id="get-gaussian">Метод Гаусса</button>'
  document.getElementById('get-lagrange').addEventListener('click', () => {calculateValue('/api/lagrange', data)})
  document.getElementById('get-gaussian').addEventListener('click', () => {calculateValue('/api/gaussian', data)})
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
