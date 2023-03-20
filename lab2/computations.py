from math import sin, cos

equations = {
    1: lambda x: 2.3 * pow(x, 3) + 5.75 * pow(x, 2) - 7.41 * x - 10.6,
    2: lambda x: x**2,
    3: lambda x: sin(2*x)+cos(x)
}

equations_derivative = {
    1: lambda x: 6.9 * pow(x, 2) + 11.5 * x - 7.41,
    2: lambda x: 2*x,
    3: lambda x: 3*x**2
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
    x0 = a
    x1 = a + 0.03
    x2 = 0
    k = 0
    while k < 500:
        solution_table.append([])
        x2 = x1 - (x1 - x0) / (equation(x1) - equation(x0)) * equation(x1)
        solution_table[k].append(x0)
        solution_table[k].append(x1)
        solution_table[k].append(x2)
        solution_table[k].append(equation(x2))
        criteria = abs(x2 - x1)
        solution_table[k].append(criteria)
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
    a_der = derivative(a)
    b_der = derivative(b)
    l = 1/max(a_der, b_der)
    phi = lambda x: x - l * equation(x)

    x0 = b
    x1 = 0
    k = 0
    while k < 500:
        x1 = phi(x0)
        criteria = abs(x1 - x0)

        solution_table.append([])
        solution_table[k].append(x0)
        solution_table[k].append(x1)
        solution_table[k].append(phi(x1))
        solution_table[k].append(equation(x1))
        solution_table[k].append(criteria)
        if criteria < eps:
            return {'table': solution_table, 'result': x1}
        k += 1
        x0 = x1
    return None



