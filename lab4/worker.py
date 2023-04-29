import computations as cp
from canvas import plot
from matplotlib.backends.backend_agg import FigureCanvasAgg
from io import BytesIO

last_plot = BytesIO()

types = [
    cp.linear_approximate,
    cp.square_approximate,
    cp.cube_approximate,
    cp.log_approximate,
    cp.exp_approximate,
    cp.pow_approximate
]

def packPlot(fig):
    global last_plot
    last_plot = BytesIO()
    FigureCanvasAgg(fig).print_png(last_plot)

def approximate(data):
    X = data['x']
    Y = data['y']
    out = []
    for appr in types:
        res = appr(X, Y)
        if res is not None: out.append(res)

    packPlot(plot([{'f': i['f'], 'legend': i['type']} for i in out], data))
    best = min(out, key=lambda z: z['sqr_miss'])
    return {'best': best['type'],
            'functions': [{'view': i['view'], 'type': i['type'], 'sqr': i['sqr_miss']} for i in out]}
