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