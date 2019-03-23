from flask import Flask, jsonify, request
from darko import Darko
from signal_handlers import SignalHandler
from config import Config
from starter import *
app = Flask(__name__)
darko = Darko()


@app.route("/nodes")
def index():
    node = darko.get_all_nodes()
    return node


@app.route('/create')
def create():
    data = request.args.get('sentence')
    darko.create(sentence=data)
    return jsonify({'status': 'success'})


@app.route('/<name>')
def get_node(name):
    node = darko.get(name)
    if node:
        return node.name
    return 'We dont get anything'


if __name__ == "__main__":
    signal = SignalHandler()
    signal.save()
    Start.start()
    app.run(host='127.0.0.1', debug=True, port=12345, use_reloader=True)
