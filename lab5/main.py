from flask import Flask, render_template, request, make_response, jsonify, Response
import worker as wk

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/points', methods=['POST'])
def generatePoints():
    try:
        return jsonify(wk.createPoints(request.get_json()))
    except Exception as ex:
        resp = make_response(str(ex), 400)
        return resp

@app.route('/api/interpolate', methods=['POST'])
def interpolate():
    try:
        return jsonify(wk.interpolate(request.get_json()))
    except Exception as ex:
        resp = make_response(str(ex), 400)
        return resp

@app.route('/api/lagrange', methods=['POST'])
def lagrange():
    try:
        return jsonify(wk.lagrange(request.get_json()))
    except Exception as ex:
        resp = make_response(str(ex), 400)
        return resp

@app.route('/api/gaussian', methods=['POST'])
def gaussian():
    try:
        return jsonify(wk.gaussian(request.get_json()))
    except Exception as ex:
        resp = make_response(str(ex), 400)
        return resp

@app.route('/api/plot', methods=['POST'])
def getPlot():
    try:
        return Response(wk.graphics(request.get_json()), mimetype='image/png')
    except Exception as ex:
        return make_response(str(ex), 400)


if __name__ == '__main__':
    app.run(debug=True)
