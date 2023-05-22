function duplicates(data) {
    const findDuplicates = arr => arr.filter((item, index) => arr.indexOf(item) !== index)
    const dupl = findDuplicates(data).length > 0
    if (dupl) oops('Значения x должны быть уникальными')
    return dupl
}

function checkDataSize(data) {
    if (data.length < 16) oops('Входной файл должен содержать от 8 до 12 точек')
    if (data.length % 2 !== 0) oops('Некорректный размер таблицы')
    return data.length >= 16 && data.length !== 2 
}

function isFloat(num) {
    const new_var = num.replace(',', '.')
    if (!isNaN(new_var) && new_var !== '') return parseFloat(new_var)
    oops('Входные данные должны содержать только числа')
    return false
}

function fromFileData(input) {
    let file = input.files[0]
    let reader = new FileReader()
    reader.readAsText(file)
    input.value = ''
    reader.onload = () => {correctInput(reader.result)}
    reader.onerror = () => {oops('Ошибка считывания файла')}
}

function correctInput(result) {
    let out = result.replace('\r', ' ').replace('\n', ' ').split(/\s+/)
    if (out[out.length - 1] == ' ' || out[out.length - 1] == '') out.pop()
    console.log(out)
    for (let i = 0; i < out.length; i++) {out[i] = isFloat(out[i]); if (out[i] === false)  return}

    if (!checkDataSize(out)) return
    const data = {x: out.slice(0, out.length / 2), y: out.slice(out.length / 2, out.length)}
    if (duplicates(data.x)) return
    calc(data)    
}

function readFromInput() {
    let out = new Array(), con = true
    document.querySelectorAll('.element').forEach(el => {
        const num = isFloat(el.value)
        if (num !== false) out.push(num)
        else con = false
    })
    if (!con) return
    const data = {x: out.slice(0, out.length / 2), y: out.slice(out.length / 2, out.length)}
    if (duplicates(data.x)) return
    calc(data)
}

function parsePopVal(arg, type = undefined) {
    if (arg === false) {oops('Отмена');return false}
    return type === undefined ? arg : type(arg)
}

async function getDataFunction() {
    const func = parsePopVal(await chooseFunction())
    if (func === false) return false
    const a = parsePopVal(await chooseInterval(), parseFloat)
    if (a === false) return false
    const b = parsePopVal(await chooseInterval(false), parseFloat)
    if (b === false) return false
    if (a >= b) {oops('Start must be less than end'); return false}
    return {func, a, b}
}

async function generateByFunction() {
    const data = await getDataFunction()
    if (data === false) return
    const size = document.getElementById('size')
    data.n = size.options[size.selectedIndex].value*1

    
    const points = await recieve(await requestData('/api/points', data), jsonReciever)
    const matrix = document.querySelectorAll('.element')
    for (let i = 0; i < matrix.length / 2; i++) matrix[i].value = points.x[i]
    for (let i = 0; i < matrix.length / 2; i++) matrix[i + matrix.length / 2].value = points.y[i]
    success('Values generated successfully')
}

async function chooseFunction() {
    let a = await Swal.fire({
      title: 'Select function',
      input: 'radio',
      inputOptions: {
        1: '\\(sin(x)\\)',
        2: '\\(x^2+x\\)'
      },
      didOpen: () => {setTimeout(() => MathJax.typeset(), 10)},
      inputValidator: result => {if (!result) return 'You need to select something!'}
    }).then(function(result) {
      if (result.isConfirmed) return result.value
      return false
    })
    MathJax.typeset()
    return a
  }
  
  async function chooseInterval(isStart = true) {
    return await Swal.fire({
      title: 'Select interval ' + (isStart ? 'start' : 'end'),
      input: 'text',
      inputOptions: {
        autocapitalize: 'off'
      },
      inputValidator: result => {if (isNaN(result.replace(',', '.')) || result == '') return 'Please input number'}
    }).then(
      function(result) {
        if (result.isConfirmed) return result.value.replace(',', '.')
        return false
    })
  }

  function calculateValue(link, data) {
    console.log(data)
    Swal.fire({
      title: 'Input x to define value',
      input: 'text',
      inputOptions: {
        autocapitalize: 'off'
      },
      inputValidator: result => {if (isNaN(result.replace(',', '.')) || result == '') return 'Please input number'}
    }).then(
      async function(result) {
        const answer = await recieve(
            await requestData(link, {x: data.x, y: data.y, search: parseFloat(result.value)}), jsonReciever
          )
        Swal.fire({
          icon: 'success',
          title: 'Calculated',
          text: `Value in this point is ${answer.answer}`
        })
    })
  }