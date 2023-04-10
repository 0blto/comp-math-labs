from requestParser import parse_equation
from computations import right_rectangle, left_rectangle, center_rectangle, trapeze_rectangle, find_intervals,\
    the_simpsons, integrate, DEFAULT_RECT_K, DEFAULT_TRAPEZE_K, DEFAULT_SIMPSON_K

def method_name(num):
    if num == 1:
        return 'метода прямоугольников (л)'
    if num == 2:
        return 'метода прямоугольников (п) '
    if num == 3:
        return 'метода прямоугольников (ср) '
    if num == 4:
        return 'метода трапеций '
    if num == 5:
        return 'метода Симпсона'
    return 'Это что-то не то'

def integrate_method(eq_num, method, intervals, eps):
    if method == 1:
        return integrate(eq_num, intervals, eps, right_rectangle, DEFAULT_RECT_K)
    if method == 2:
        return integrate(eq_num, intervals, eps, left_rectangle, DEFAULT_RECT_K)
    if method == 3:
        return integrate(eq_num, intervals, eps, center_rectangle, DEFAULT_RECT_K)
    if method == 4:
        return integrate(eq_num, intervals, eps, trapeze_rectangle, DEFAULT_TRAPEZE_K)
    if method == 5:
        return integrate(eq_num, intervals, eps, the_simpsons, DEFAULT_SIMPSON_K)
    return 'Ошибка'

def aggregate_integral(content):
    eq_num, method, a, b, eps = parse_equation(content)
    intervals = find_intervals(eq_num, a, b)
    result = integrate_method(eq_num, method, intervals, eps)
    return {'answer': round(float(result[0]), 3), 'n': int(result[1])}
