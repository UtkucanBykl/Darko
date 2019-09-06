from flask import Flask, request
from flask.json import jsonify
import json
from starter import Start
from darko import Darko
from signal_handlers import SignalHandler
from flask_cors import CORS

app = Flask(__name__)
darko = Darko()
CORS(app)


@app.route("/nodes")
def index():
    node = json.loads(darko.get_all_nodes())
    return jsonify({'data' :node})


@app.route('/create')
def create():
    data = request.args.getlist('sentence')
    try:
        status = all((map(lambda x: darko.create(sentence=x), data)))
        return jsonify({'status': status})
    except BaseException as e:
        return jsonify({'error': str(e)})


@app.route('/delete')
def delete():
    data = request.args.getlist('sentence')
    try:
        status = all((map(lambda x: darko.delete(sentence=x), data)))
        return jsonify({'status': status})
    except BaseException as e:
        return jsonify({'error': str(e)})

@app.route('/get/<name>')
def get_node(name):
    node = darko.get(name)
    if type(node) == dict:
        return jsonify({'error' :'We dont get anything'})
    return jsonify({'data' :json.loads(node)})


@app.route('/update')
def update():
    data = request.args.getlist('sentence')
    try:
        status = all((map(lambda x: darko.update(sentence=x), data)))
        return jsonify({'status': status})
    except BaseException as e:
        return jsonify({'error': str(e)})

def start():
    signal = SignalHandler()
    signal.save()
    Start.start()
    app.run(host='127.0.0.1', debug=True, port=12345, use_reloader=False)


if __name__ == "__main__":
    start()
