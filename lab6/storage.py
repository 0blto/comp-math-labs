from numpy import exp

equations = {
    1: {
        'equation': lambda x, y: x + y,
        'solution': lambda x, c: c * exp(x) - x - 1,
        'c': lambda x, y: (y + x + 1) / exp(x)
    },
    2: {
        'equation': lambda x, y: x * y,
        'solution': lambda x, c: c * exp(x ** 2 / 2),
        'c': lambda x, y: y / exp(x ** 2 / 2)
    },
    3: {
        'equation': lambda x, y: y + (1 + x) * (y ** 2),
        'solution': lambda x, c: -(exp(x)) / (c + exp(x) * x),
        'c': lambda x, y: -((exp(x) * (x * y + 1)) / y)
    }
}
