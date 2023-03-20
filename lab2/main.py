from flask import Flask, render_template, request, make_response, jsonify
from aggregation import aggregate_equation, aggregate_system
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
    print('4')
    content = request.get_json()
    try:
        return jsonify(aggregate_system(content))
    except Exception as ex:
        return make_response(str(ex), 400)


if __name__ == '__main__':
    app.run(debug=True)
