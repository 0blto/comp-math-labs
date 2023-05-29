from flask import Flask, render_template, request, make_response, jsonify, Response
import worker as wk
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/diff_equation_solver', methods=['POST'])
def integrate_controller():
    try:
        return jsonify(wk.diff_equation_worker(request.get_json()))
    except Exception as ex:
        return make_response(str(ex), 400)

@app.route('/api/plot_equation', methods=['POST'])
def plot():
    try:
        return Response(wk.plot_solution(request.get_json()), mimetype='image/png')
    except Exception as ex:
        return make_response(str(ex), 400)


if __name__ == '__main__':
    app.run(debug=True)
