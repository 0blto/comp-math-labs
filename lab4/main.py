from flask import Flask, render_template, request, make_response, jsonify, Response
import worker as wk

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/approximate', methods=['POST'])
def approximate():
    try:
        content = request.get_json()
        print(content)
        return jsonify(wk.approximate(content))
    except Exception as ex:
        resp = make_response(str(ex), 400)
        return resp

@app.route('/api/plot', methods=['POST'])
def get_last_plot():
    try:
        return Response(wk.last_plot.getvalue(), mimetype='image/png')
    except Exception as ex:
        return make_response(str(ex), 400)

if __name__ == '__main__':
    app.run(debug=True)
