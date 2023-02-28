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

function results(table) {

  tableHTML = '<h2>Таблица итераций</h2><div class="block" style="overflow-x: auto;"><table style="width: 100%; text-align: center;"><tr><th>N</th>'
  for (let i = 0; i < table[1].length; i++) {
    tableHTML += '<th>'
    tableHTML += (i+1 <= table[1].length / 2) ? '\\(x_{' + (i+1) + '}\\)' : '\\(\\delta_{' + (i+1-table[1].length/2) + '}\\)'
    tableHTML += '</th>'
  }
  for (let i = 0; i < table.length - 1; i++) {
    tableHTML += '<tr><td>' + i + '</td>'
    for (let j = 0; j < table[i].length; j++) {
    if (i === 0 && j >= table[0].length / 2) continue
      tableHTML += '<td>'
      tableHTML += parseFloat(table[i][j]).toFixed(document.getElementById('get_val').value)
      tableHTML += '</td>'
    }
    tableHTML += '</tr>'
  }
  tableHTML += '</table></div>'

  document.getElementById('results').innerHTML = tableHTML
  MathJax.typeset()
}

function slau(A, B) {
  let html = '<h2>Преобразованная система</h2><div class="block" style="overflow-x: auto;"><table style="text-align: left; width: 100%;">', n = A.length
  for (let i = 0; i < n; i++) {
    html += '<tr><td>'
    for (let j = 0; j <= n; j++) {
      if (j != n) {
        if (A[i][j] > 0 && j != 0) {
          html += '+ '
        }
        if (j != n - 1) {
          
          html += ' \\(' + A[i][j] + 'x_{' + (j+1) + '}\\) '
          
        } else {
          html += ' \\(' + A[i][j] + 'x_{' + (j+1) + '}\\) = '
        }
      } else {
        html += B[i]
      }
      
    }
    html += '</td></tr>'
  }
  html += '</table></div>'

  document.getElementById('system').innerHTML = html

  Swal.fire({
    title: 'Система преобразована и решена',
    icon: 'success',
    showClass: {
      popup: 'animate__animated animate__fadeIn'
    },
    hideClass: {
      popup: 'animate__animated animate__fadeOut'
    }
  })
  MathJax.typeset()
}

function share() {
  Swal.fire({
    title: 'thebigone',
    text: 'Лабораторная работа №1 по дисциплине "вычислительная математика"',
    imageUrl: '../static/resources/achi-kochi.gif',
    padding: '3em',
    color: '#716add',
    timer: 10000,
    timerProgressBar: true
    })
}