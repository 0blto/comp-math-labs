import numpy as np

equations = {
    '1': lambda x: np.sin(x),
    '2': lambda x: x**2+x
}

def generate(eq, a, b, n):
    f = equations[eq]
    step = (b - a) / (n - 1)
    x = [round(i, 3) for i in np.arange(a, b + step, step)]
    y = [round(f(i), 3) for i in x]
    return {'x': [round(i, 3) for i in x], 'y': [round(i, 3) for i in y]}
