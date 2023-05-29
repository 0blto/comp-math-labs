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
    temp_x = getXes(x, length, h)
    temp_y = [y]
    yp = y + h * eq(x, y)
    for i in range(1, len(temp_x)):
        yc = 1e10
        while calc_eps(yp, yc, 2) > eps:
            yc = temp_y[i - 1] + h / 2 * \
                 (eq(temp_x[i - 1], temp_y[i - 1]) +
                  eq(temp_x[i], yp))
            yp = yc
        temp_y.append(yc)
    return temp_y


def rungeKutta(equation, x, y, eps, length, h):
    temp_x = getXes(x, length, h)
    temp_y = [y]
    for i in range(1, len(temp_x)):
        yc = 1e10
        yp = temp_y[i-1]
        while calc_eps(yp, yc, 4) > eps:
            yp = yc
            k1 = h * equation(temp_x[i - 1], temp_y[i - 1])
            k2 = h * equation(temp_x[i - 1] + h / 2, temp_y[i - 1] + k1 / 2)
            k3 = h * equation(temp_x[i - 1] + h / 2, temp_y[i - 1] + k2 / 2)
            k4 = h * equation(temp_x[i - 1] + h, temp_y[i - 1] + k3)
            yc = temp_y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        temp_y.append(yc)
    return temp_y

def milne(equation, x, y, eps, length, h):
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
        raise ValueError("For Milan differentiation num of intervals has to be at least 4!")

    starter = rungeKutta(equation, x, y, eps, length, h)
    temp_y = starter[:4]

    for i in range(4, len(temp_x)):
        predicted = round(prediction(), 5)
        corrected = round(correction(), 5)

        while abs(corrected - predicted) > eps:
            predicted = round(corrected, 5)
            corrected = round(correction(), 5)

        temp_y.append(corrected)


    return temp_y


#print(rungeKutta(storage.equations[3]['equation'], 1, -1, 0.01, 0.5, 0.1))
