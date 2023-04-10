from math import sin, cos, sqrt

equations = {
    1: lambda x: 2.3 * pow(x, 3) + 5.75 * pow(x, 2) - 7.41 * x - 10.6,
    2: lambda x: pow(x, 3) - x + 4,
    3: lambda x: sin(2*x)+cos(x)
}

equations_derivative = {
    1: lambda x: 6.9 * pow(x, 2) + 11.5 * x - 7.41,
    2: lambda x: 2*pow(x, 2)-1,
    3: lambda x: 2 * cos(2*x) - sin(x)
}

systems = {
    1: [
        lambda x, y:  0.3 - 0.1*x**2 - 0.2*y**2,
        lambda x, y: 0.7 - 0.2 * x**2 - 0.1 * x * y
    ],
    2: [
        lambda x, y: 0.4-0.5*x**2-0.2*y**2,
        lambda x, y: 0.3 * x**2
    ]
}

systems_drawable = {
    1: [
        lambda x, y: 0.1 * x ** 2 + x + 0.2 * y ** 2 - 0.3,
        lambda x, y: 0.2 * x ** 2 + y + 0.1 * x * y - 0.7
    ],
    2: [
        lambda x, y: 0.5*x**2 + 0.2*y**2 - 0.4 + x,
        lambda x, y: -0.3 * x**2 + y
    ]
}


def check_interval(a, b, eq):
    left, right = a, b
    intervals = []
    while left < right:
        left_value = equations[eq](left)
        if left + 0.5 >= right:
            new_left = right
            right_value = equations[eq](new_left)
        else:
            new_left = left + 0.5
            right_value = equations[eq](new_left)
        if left_value*right_value <= 0:
            intervals.append([left, new_left])
        left = new_left
    return intervals


def chord_method(eq, a, b, eps):
    solution_table = []
    equation = equations[eq]
    k = 0
    cur_a = a
    cur_b = b
    cur_x = 0
    while k < 500:
        solution_table.append([])

        fa = equation(cur_a)
        fb = equation(cur_b)
        cur_x = (cur_a * fb - cur_b * fa) / (fb - fa)
        fx = equation(cur_x)

        solution_table[k].append(cur_a)
        solution_table[k].append(cur_b)

        if fa*fx < 0:
            cur_def = abs(cur_b - cur_x)
            cur_b = cur_x
        else:
            cur_def = abs(cur_a - cur_x)
            cur_a = cur_x

        solution_table[k].append(cur_x)
        solution_table[k].append(fa)
        solution_table[k].append(fb)
        solution_table[k].append(fx)
        solution_table[k].append(cur_def)
        k += 1
        if cur_def < eps:
            return {'table': solution_table, 'result': cur_x}
    return None


def secant_method(eq, a, eps):
    solution_table = []
    equation = equations[eq]
    x0 = a; x1 = a + 0.001; x2 = 0; k = 0
    while k < 500:
        x2 = x1 - (x1 - x0) / (equation(x1) - equation(x0)) * equation(x1)
        criteria = abs(x2 - x1)
        solution_table.append([x0, x1, x2, equation(x2), criteria])

        if criteria < eps:
            return {'table': solution_table, 'result': x2}
        k += 1
        x0 = x1
        x1 = x2
    return None


def simple_iteration_method(eq, a, b, eps):
    solution_table = []
    equation = equations[eq]
    derivative = equations_derivative[eq]

    a_der = derivative(a); b_der = derivative(b)
    l = -1/max(a_der, b_der)
    phi = lambda x: x + l * equation(x)
    phi_der = lambda x: 1 + l * derivative(x)

    start = a
    q = abs(phi_der(start))
    while start < b:
        if q < abs(phi_der(start)):
            q = abs(phi_der(start))
        start += 0.01

    if q > 1:
        raise Exception('Достаточное условие сходимости не выполнено')

    x0 = a
    x1 = 0
    k = 0
    while k < 6:
        x1 = phi(x0)
        criteria = abs(x1 - x0)

        solution_table.append([x0, x1, phi(x1), equation(x1), criteria])

        if criteria < eps:
            return {'table': solution_table, 'result': x1}

        k += 1
        x0 = x1
    return {'table': solution_table, 'result': x1}


def system_simple_iteration(system, a, b, eps):
    try:
        cur_system = systems[system]
        solution_table = []
        x0 = a; y0 = b; x1 = cur_system[0](x0, y0); y1 = cur_system[1](x0, y0); k = 0
        while k < 10:
            dx = abs(x1 - x0)
            dy = abs(y1 - y0)
            solution_table.append([x0, y0, x1, y1, dx, dy])
            if dx < eps or dy < eps:
                return {'table': solution_table, 'result': {'x': x1, 'y': y1}}

            x0, y0 = x1, y1

            x1 = cur_system[0](x0, y0)
            y1 = cur_system[1](x0, y0)

            k += 1

        raise Exception('Не выполнено достаточное условие сходимости')
    except OverflowError:
        raise Exception('Не выполнено достаточное условие сходимости')
