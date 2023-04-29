from math import log, exp, sqrt

def cf_str(is_before, val):
    if round(val, 0) == val: val = int(val)
    if val == 1 and is_before: return '+'
    if val == 1 and not is_before: return ''
    if val == -1: return '-'
    if val > 0 and is_before: return '+' + str(val)
    if val > 0 and not is_before: return str(val)
    if val < 0: return str(val)


def solve_minor(matrix, i, j):
    n = len(matrix)
    return [[matrix[row][col] for col in range(n) if col != j] for row in range(n) if row != i]

def solve_det(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    det = 0
    sgn = 1
    for j in range(n):
        det += sgn * matrix[0][j] * solve_det(solve_minor(matrix, 0, j))
        sgn *= -1
    return det


def gauss_solver(matrix):
    n = len(matrix)
    det = solve_det([matrix[i][:n] for i in range(n)])
    if det == 0:
        return None


    for i in range(n - 1):
        max_i = i
        for m in range(i + 1, n):
            if abs(matrix[m][i]) > abs(matrix[max_i][i]):
                max_i = m

        if max_i != i:
            for j in range(n + 1):
                matrix[i][j], matrix[max_i][j] = matrix[max_i][j], matrix[i][j]

        for k in range(i + 1, n):
            coef = matrix[k][i] / matrix[i][i]
            for j in range(i, n + 1):
                matrix[k][j] -= coef * matrix[i][j]

    roots = [0] * n
    for i in range(n - 1, -1, -1):
        s_part = 0
        for j in range(i + 1, n):
            s_part += matrix[i][j] * roots[j]
        roots[i] = (matrix[i][n] - s_part) / matrix[i][i]

    residuals = [0] * n
    for i in range(n):
        s_part = 0
        for j in range(n):
            s_part += matrix[i][j] * roots[j]
        residuals[i] = s_part - matrix[i][n]

    return roots

def miss_level(x, y, f):
    return sum([pow(f(x[i]) - y[i], 2) for i in range(len(x))])

def sqr_average(x, y, f):
    return round(sqrt(miss_level(x, y, f) / len(x)), 3)


def linear_cf(x, y):
    n = len(x)
    sxx = sum([pow(x[i], 2) for i in range(n)])
    sxy = sum([x[i] * y[i] for i in range(n)])
    sx = sum(x)
    sy = sum(y)
    d = sxx * n - sx ** 2
    d1 = sxy * n - sx * sy
    d2 = sxx * sy - sx * sxy
    return round(d1/d, 5), round(d2/d, 5)

def linear_approximate(x, y):
    a, b = linear_cf(x, y)
    f = lambda p: a * p + b

    round(a, 3)
    round(b, 3)
    if int(a) == a: a = int(a)
    if int(b) == b: b = int(b)
    view = ''
    if a == 1:
        view = 'x'
    elif a == -1:
        view = '-x'
    else:
        view = str(a) + 'x'
    if b < 0: view += str(b)
    if b > 0: view += '+' + str(b)
    if a == 0: view = b

    return {'f': f,
            'view': view,
            'miss': miss_level(x, y, f),
            'sqr_miss': sqr_average(x, y, f),
            'type': 'linear'}

def square_approximate(x, y):
    n = len(x)
    sx = sum(x)
    sy = sum(y)
    sxx = sum([pow(x[i], 2) for i in range(n)])
    sxy = sum([x[i] * y[i] for i in range(n)])
    sxxx = sum([pow(x[i], 3) for i in range(n)])
    sxxxx = sum([pow(x[i], 4) for i in range(n)])
    sxxy = sum([pow(x[i], 2) * y[i] for i in range(n)])
    matrix = [
        [n, sx, sxx, sy],
        [sx, sxx, sxxx, sxy],
        [sxx, sxxx, sxxxx, sxxy]
    ]

    a = [round(i, 5) for i in gauss_solver(matrix)]

    if a is None: return None
    if a[2] == 0: return None

    f = lambda p: a[0] + a[1] * p + a[2] * pow(p, 2)
    is_before = False
    view = ''
    if a[0] != 0:
        view += str(int(a[0]) if round(a[0], 0) == a[0] else a[0])
        is_before = True
    if a[1] != 0:
        view += cf_str(is_before, a[1])
        is_before = True
        view += 'x'
    view += cf_str(is_before, a[2])
    view += 'x^2'

    return {'f': f,
            'view': view,
            'miss': miss_level(x, y, f),
            'sqr_miss': sqr_average(x, y, f),
            'type': 'square'}

def cube_approximate(x, y):
    n = len(x)
    sx = sum(x)
    sy = sum(y)
    sxx = sum([pow(x[i], 2) for i in range(n)])
    sxy = sum([x[i] * y[i] for i in range(n)])
    sxxx = sum([pow(x[i], 3) for i in range(n)])
    sxxxx = sum([pow(x[i], 4) for i in range(n)])
    sxxy = sum([pow(x[i], 2) * y[i] for i in range(n)])
    s5x = sum([pow(x[i], 5) for i in range(n)])
    s6x = sum([pow(x[i], 6) for i in range(n)])
    sxxxy = sum([pow(x[i], 3) * y[i] for i in range(n)])
    matrix = [
        [n, sx, sxx, sxxx, sy],
        [sx, sxx, sxxx, sxxxx, sxy],
        [sxx, sxxx, sxxxx, s5x, sxxy],
        [sxxx, sxxxx, s5x, s6x, sxxxy]
    ]

    a = [round(i, 5) for i in gauss_solver(matrix)]

    if a is None: return None
    if a[3] == 0: return None

    f = lambda p: a[0] + a[1] * p + a[2] * pow(p, 2) + a[3] * pow(p, 3)



    is_before = False
    view = ''
    if a[0] != 0:
        view += str(int(a[0]) if round(a[0], 0) == a[0] else a[0])
        is_before = True
    if a[1] != 0:
        view += cf_str(is_before, a[1])
        is_before = True
        view += 'x'
    if a[2] != 0:
        view += cf_str(is_before, a[2])
        is_before = True
        view += 'x^2'
    view += cf_str(is_before, a[3])
    view += 'x^3'

    return {'f': f,
            'view': str(a[0]) + '+' + str(a[1]) + 'x+' + str(a[2]) + 'x^2+' + str(a[3]) + 'x^3',
            'miss': miss_level(x, y, f),
            'sqr_miss': sqr_average(x, y, f),
            'type': 'cube'}

def log_approximate(x, y):
    try:
        a, b = linear_cf([log(i) for i in x], y)
    except ValueError:
        return None
    f = lambda p: a * log(p) + b
    if a == 0: return None
    view = cf_str(False, a) + 'log(x)' + cf_str(True, b)

    return {'f': f,
            'view': view,
            'miss': miss_level(x, y, f),
            'sqr_miss': sqr_average(x, y, f),
            'type': 'log'}

def exp_approximate(x, y):
    try:
        a, b = linear_cf(x, [log(i) for i in y])
    except ValueError:
        return None
    a, b = round(exp(b), 5), a
    if a == 0 or b == 0: return None
    f = lambda p: a * exp(b * p)
    view = cf_str(False, a) + 'e^{' + cf_str(False, b) + 'x}'

    return {'f': f,
            'view': view,
            'miss': miss_level(x, y, f),
            'sqr_miss': sqr_average(x, y, f),
            'type': 'exp'}

def pow_approximate(x, y):
    try:
        a, b = linear_cf([log(i) for i in x], [log(i) for i in y])
    except ValueError:
        return None
    a, b = round(exp(b), 5), a
    if b in [1, 2, 3] or a == 0 or b == 0:
        return None
    f = lambda p: a * pow(p, b)
    view = cf_str(False, a) + 'x^{' + str(b) + '}'

    return {'f': f,
            'view': view,
            'miss': miss_level(x, y, f),
            'sqr_miss': sqr_average(x, y, f),
            'type': 'power'}