from flask import Flask, render_template, request, make_response, jsonify, Response
from aggregation import aggregate_integral
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main', methods=['POST'])
def equation():
    return render_template('main.html')

@app.route('/start', methods=['POST'])
def start():
    return render_template('start.html')

@app.route('/api/integrate', methods=['POST'])
def integrate_controller():
    try:
        return jsonify(aggregate_integral(request.get_json()))
    except Exception as ex:
        return make_response(str(ex), 400)

if __name__ == '__main__':
    app.run(debug=True)
    #print(aggregate_integral({'equation': 5, 'method': 1, 'left': -1, 'right': 3, 'epsilon': 0.01}))
