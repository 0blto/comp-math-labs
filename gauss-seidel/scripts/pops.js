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

  tableHTML = '<div class="block" style="overflow-x: auto;"><table style=" border: 2px solid #EEEEEE; width: 100%; text-align: center;"><tr><th>N</th>'
  for (let i = 0; i < table[1].length; i++) {
    tableHTML += '<th>'
    tableHTML += (i+1 <= table[1].length / 2) ? '\\(x_{' + (i+1) + '}\\)' : '\\(\\delta_{' + (i+1-table[1].length/2) + '}\\)'
    tableHTML += '</th>'
  }
  for (let i = 0; i < table.length; i++) {
    tableHTML += '<tr><td>' + i + '</td>'
    for (let j = 0; j < table[i].length; j++) {
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
  let html = '<div style="overflow-x: auto;"><table style="text-align: center; width: 100%">', n = A.length
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
  Swal.fire({
    title: 'Преобразованная система',
    html: html,
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
    imageUrl: 'resources/achi-kochi.gif',
    padding: '3em',
    color: '#716add',
    timer: 10000,
    timerProgressBar: true
    })
}