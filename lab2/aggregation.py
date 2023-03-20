from requestParser import parse_equation, parse_system
from computations import check_interval, chord_method, secant_method, simple_iteration_method

def method_name(num):
    if num == 1:
        return 'метода хорд'
    if num == 2:
        return 'метода секущих'
    if num == 3:
        return 'метода простых итераций'
    return 'Это что-то не то'

def is_single_solution(intervals):
    if len(intervals) == 0:
        raise Exception('На заданном промежутке нет корней')
    if len(intervals) > 1:
        raise Exception('На заданном промежутке несколько корней в интервалах ' + str(intervals))

def equation_method(method, eq, a, b, eps):
    if method == 1:
        return chord_method(eq, a, b, eps)
    if method == 2:
        return secant_method(eq, a, eps)
    if method == 3:
        return simple_iteration_method(eq, a, b, eps)
    return 'Ошибка'

def aggregate_equation(content):
    eq_num, method, a, b, eps = parse_equation(content)

    message = 'Решено, при помощи ' + method_name(method)

    intervals = check_interval(a, b, eq_num)
    is_single_solution(intervals)

    solution = equation_method(method, eq_num, intervals[0][0], intervals[0][1], eps)

    return {'solution': solution, 'message': message, 'method': method, 'equation': eq_num}

def aggregate_system(content):
    system, a, b, eps = parse_system(content)
    return {'system': system, 'message': 'Hi, i solved this'}
