from flask import Flask, render_template, request, make_response, jsonify
from computations import worker

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/exec', methods=['POST'])
def exec():
    try:
        content = request.get_json()
        print(content)
        return jsonify(results = worker(content['E'], content['num'], content['matrixA'], content['matrixB']))

    except Exception as ex:
        resp = make_response(str(ex), 400)
        return resp

if __name__ == '__main__':
    app.run(debug=True)
