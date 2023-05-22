import computations as cp
from canvas import plot
from matplotlib.backends.backend_agg import FigureCanvasAgg
from io import BytesIO
import pointsGenerator as pg
import computations as cp

def createPoints(data):
    eq, a, b, n = data['func'], data['a'], data['b'], data['n']
    return pg.generate(eq, a, b, n)

def interpolate(data):
    X = data['x']
    Y = data['y']
    return {'finiteDiff': cp.finiteDiff(X, Y)}

def lagrange(data):
    X = data['x']
    Y = data['y']
    SEARCH = data['search']
    return {'answer': cp.lagrangeMethod(X, Y, SEARCH)}

def gaussian(data):
    X = data['x']
    Y = data['y']
    SEARCH = data['search']
    return {'answer': cp.gaussianMethod(X, Y, SEARCH)}

def graphics(data):
    X = data['x']
    Y = data['y']
    bts = BytesIO()
    FigureCanvasAgg(plot(cp.lagrangeFunc(X, Y), cp.gaussianFunc(X, Y), X, Y)).print_png(bts)
    return bts.getvalue()

