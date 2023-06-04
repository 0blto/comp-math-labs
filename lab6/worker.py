from requestParser import parse_request
import computations as cp
import storage as store
from matplotlib.backends.backend_agg import FigureCanvasAgg
from io import BytesIO
from canvas import plotWithoutWarn

FORMAT = 3

def chooseConst(eq_num, x, y):
    c = store.equations[eq_num]['c'](x, y)

    def f(positional_x):
        return store.equations[eq_num]['solution'](positional_x, c)

    return f


def chooseMethod(num):
    if num == 1:
        return cp.extendedEkler
    if num == 2:
        return cp.rungeKutta
    if num == 3:
        return cp.milne


def diff_equation_worker(data):
    eq_num, method, x, y, eps, length, h = parse_request(data)
    return {'x': [round(i, FORMAT) for i in cp.getXes(x, length, h)],
            'y': [round(i, FORMAT) for i in chooseMethod(method)(store.equations[eq_num]['equation'], x, y, eps, length, h)],
            'dy': [round(i, FORMAT) for i in cp.getDiffValues(store.equations[eq_num]['equation'], x,
                                   chooseMethod(method)(store.equations[eq_num]['equation'], x, y, eps, length, h),
                                   length, h)],
            'real': [round(i, FORMAT) for i in cp.detFunctionValues(chooseConst(eq_num, x, y), x, length, h)]}


def plot_solution(data):
    eq_num, method, x, y, eps, length, h = parse_request(data)
    bts = BytesIO()
    FigureCanvasAgg(
        plotWithoutWarn(chooseConst(eq_num, x, y),
             cp.getXes(x, length, h),
             chooseMethod(method)(store.equations[eq_num]['equation'], x, y, eps, length, h)
             )
    ).print_png(bts)
    return bts.getvalue()

#print(diff_equation_worker({'x': 1, 'y': -1, 'epsilon': 0.0000001, 'len': 5, 'h': 1, 'equation': 3, 'method': 3}))