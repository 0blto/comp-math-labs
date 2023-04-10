from flask import Flask, render_template, request, make_response, jsonify, Response
from aggregation import aggregate_equation, aggregate_system, draw_function, draw_system
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/equation', methods=['POST'])
def equation():
    return render_template('equations.html')

@app.route('/system', methods=['POST'])
def system():
    return render_template('systems.html')

@app.route('/equation_file', methods=['POST'])
def equation_file():
    return render_template('equation_file.html')

@app.route('/system_file', methods=['POST'])
def system_file():
    return render_template('system_file.html')

@app.route('/start', methods=['POST'])
def start():
    return render_template('start.html')

@app.route('/api/equation', methods=['POST'])
def equation_solver():
    content = request.get_json()

    try:
        return jsonify(aggregate_equation(content))
    except Exception as ex:
        return make_response(str(ex), 400)

@app.route('/api/system', methods=['POST'])
def system_solver():
    content = request.get_json()
    try:
        return jsonify(aggregate_system(content))
    except Exception as ex:
        return make_response(str(ex), 400)

@app.route('/api/equation_plt', methods=['POST'])
def equation_plt():
    content = request.get_json()
    try:
        return Response(draw_function(content), mimetype='image/png')
    except Exception as ex:
        return make_response(str(ex), 400)

@app.route('/api/system_plt', methods=['POST'])
def system_plt():
    content = request.get_json()
    try:
        return Response(draw_system(content), mimetype='image/png')
    except Exception as ex:
        return make_response(str(ex), 400)


if __name__ == '__main__':
    app.run(debug=True)
    #print(aggregate_system({'system': 1, 'left': 1, 'right': 2, 'epsilon': 0.01}))
