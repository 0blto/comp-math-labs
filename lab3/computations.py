import numpy as np
import warnings
warnings.filterwarnings("error")

equations = {
    1: lambda x: 2.3 * np.power(x, 3) + 5.75 * np.power(x, 2) - 7.41 * x - 10.6,
    2: lambda x: np.power(x, 3) - x + 4,
    3: lambda x: 2 / np.exp(x),
    4: lambda x: 1/x,
    5: lambda x: (np.power(x, 2) - 4) / (x - 2)
}

antiderivatives = {
    1: lambda x: 2.3 * np.power(x, 4) / 4 + 5.75 * np.power(x, 3) / 3 - 7.41 * np.power(x, 2) / 2 - 10.6 * x,
    2: lambda x: np.power(x, 4) / 4 - np.power(x, 2) / 2 + 4 * x,
    3: lambda x: -2 * np.exp(-x),
    4: lambda x: np.log(x),
    5: lambda x: x * (x + 4) / 2
}

DEFAULT_N = 4
DEFAULT_RECT_K = 2
DEFAULT_TRAPEZE_K = 2
DEFAULT_SIMPSON_K = 4

DEFAULT_STEP = 0.01

def find_intervals(eq_num, a, b):
    step = DEFAULT_STEP
    equation = equations[eq_num]
    correct_intervals = []

    cur_start = a
    values = np.arange(a, b, step, dtype=float)

    for i in values:
        cur = round(i, 10)
        if gap_checker(equation, cur, step):
            convergence_checker(eq_num, cur, step)
            if cur_start == cur:
                cur_start += step
                continue
            correct_intervals.append([cur_start, cur - step])
            cur_start = cur + step

    if gap_checker(equation, b, step):
        if cur_start < b:
            convergence_checker(eq_num, b, step)
            correct_intervals.append([cur_start, b - step])
    else:
        correct_intervals.append([cur_start, b])

    return correct_intervals

def gap_checker(equation, x, step):
    try:
        result = equation(x)
        if abs(result) > 1e10 or np.isinf(result):
            return True
    except Exception or RuntimeWarning:
        return True
    return False


def convergence_checker(eq_num, x, step):
    try:
        result = antiderivatives[eq_num](x)
        if abs(result) > 1e10:
            raise Exception("Интеграл не существует")
    except Exception or RuntimeWarning:
        raise Exception("Интеграл не существует")

def integrate(eq_num, intervals, eps, integral_type, k):
    diff = eps
    it = 0
    last = 1e10
    n = DEFAULT_N / 2
    result = 0
    while eps <= diff and it < 500:
        result = 0
        n *= 2
        for cur in intervals:
            h = (cur[1] - cur[0]) / n
            result += integral_type(eq_num, cur[0], cur[1], h)
        diff = abs(last - result) / (pow(2, k) - 1)
        last = result
        it += 1
    return [result, n]


def integrate_rect(eq_num, a, b, h):
    return sum(equations[eq_num](np.arange(a, b, h, dtype=float))) * h

def right_rectangle(eq_num, a, b, h):
    return integrate_rect(eq_num, a + h, b + DEFAULT_STEP, h)

def left_rectangle(eq_num, a, b, h):
    return integrate_rect(eq_num, a, b, h)

def center_rectangle(eq_num, a, b, h):
    return integrate_rect(eq_num, a + h / 2, b - h / 2, h)

def trapeze_rectangle(eq_num, a, b, h):
    out = 0
    eq = equations[eq_num]
    data = np.arange(a, b + DEFAULT_STEP, h, dtype=float)
    for i in range(1, len(data)):
        out += (eq(data[i - 1]) + eq(data[i])) * (h / 2)
    return out

def the_simpsons(eq_num, a, b, h):
    out = 0
    eq = equations[eq_num]
    data = np.arange(a, b + DEFAULT_STEP, h, dtype=float)
    out += eq(data[0]) + eq(data[len(data)-1])
    for i in range(1, len(data)-1, 2):
        out += 4 * eq(data[i])
    for i in range(2, len(data) - 2, 2):
        out += 2 * eq(data[i])
    return out * h / 3

