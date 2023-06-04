import numpy as np
import warnings
warnings.filterwarnings("error")


def detFunctionValues(solution, x, length, step):
    return [solution(i) for i in getXes(x, length, step)]

def getDiffValues(eq, x, y, length, step):
    temp_x = getXes(x, length, step)
    return [eq(temp_x[i], y[i]) for i in range(0, len(temp_x))]

def getXes(x, length, step):
    return np.arange(x, x+length+0.01, step)

def calc_eps(cur, nxt, p):
    return abs(cur - nxt) / (pow(2, p) - 1)

def extendedEkler(eq, x, y, eps, length, h):
    try:
        temp_x = getXes(x, length, h)
        temp_y = [y]
        for i in range(1, len(temp_x)):
            yp = temp_y[i-1]
            yc = 1e10
            while calc_eps(yp, yc, 2) > eps:
                yc = yp + h / 2 * \
                     (eq(temp_x[i - 1], yp) +
                      eq(temp_x[i], yp + h * eq(x, yp)))
                yp = yc
            temp_y.append(yc)
        return temp_y
    except RuntimeWarning:
        raise Exception('Усовершенствованный метод Эйлера не понял, как считать бесконечно большие, или малые значения')


def rungeKutta(equation, x, y, eps, length, h):
    try:
        temp_x = getXes(x, length, h)
        temp_y = [y]
        for i in range(1, len(temp_x)):
            yc = temp_y[i-1]
            yp = 1e10
            while calc_eps(yp, yc, 4) > eps:
                yp = yc
                k1 = h * equation(temp_x[i - 1], yp)
                k2 = h * equation(temp_x[i - 1] + h / 2, yp + k1 / 2)
                k3 = h * equation(temp_x[i - 1] + h / 2, yp + k2 / 2)
                k4 = h * equation(temp_x[i - 1] + h, yp + k3)
                yc = yp + (k1 + 2 * k2 + 2 * k3 + k4) / 6
            temp_y.append(yc)
        return temp_y
    except RuntimeWarning:
        raise Exception('Метод Рунге-Кутты устремился в небеса')

def milne(equation, x, y, eps, length, h):
    try:
        def prediction():
            tmp = 2 * equation(temp_x[i - 3], temp_y[i - 3]) - equation(temp_x[i - 2], temp_y[i - 2]) + 2 * equation(
                temp_x[i - 1], temp_y[i - 1])
            return temp_y[i - 4] + 4 * h * tmp / 3

        def correction():
            tmp = equation(temp_x[i - 2], temp_y[i - 2]) + 4 * equation(temp_x[i - 1], temp_y[i - 1]) + equation(temp_x[i],
                                                                                                                 predicted)
            return temp_y[i - 2] + h * tmp / 3

        temp_x = getXes(x, length, h)
        if len(temp_x) < 4:
            raise ValueError("Число точек интервала должно быть не меньше 4, для метода Милна")

        starter = rungeKutta(equation, x, y, eps, length, h)
        temp_y = starter[:4]

        for i in range(4, len(temp_x)):
            predicted = round(prediction(), 5)
            corrected = round(correction(), 5)

            while abs(corrected - predicted) > eps:
                predicted = round(corrected, 5)
                corrected = round(correction(), 5)

            temp_y.append(corrected)
    except RuntimeWarning:
        raise Exception('Метод Милна устремился в бесконечность на данных значениях')


    return temp_y


