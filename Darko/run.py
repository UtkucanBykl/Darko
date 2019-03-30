from config import Config
from darko import Darko
from flask import Flask, jsonify, request
from signal_handlers import SignalHandler
from starter import Start

app = Flask(__name__)
darko = Darko()


@app.route("/nodes")
def index():
    node = darko.get_all_nodes()
    return node


@app.route('/create')
def create():
    data = request.args.getlist('sentence')
    status = all(list(map(lambda x: darko.create(sentence=x), data)))
    return jsonify({'status': status})


@app.route('/delete')
def delete():
    data = request.args.getlist('sentence')
    status = all(list(map(lambda x: darko.delete(sentence=x), data)))
    return jsonify({'status': status})


@app.route('/get/<name>')
def get_node(name):
    node = darko.get(name)
    if node:
        return node
    return 'We dont get anything'


@app.route('/update')
def update():
    data = request.args.getlist('sentence')
    status = all(list(map(lambda x: darko.update(sentence=x), data)))
    return jsonify({'status': status})


def start():
    signal = SignalHandler()
    signal.save()
    Start.start()
    app.run(host='127.0.0.1', debug=True, port=12345, use_reloader=True)


if __name__ == "__main__":
    start()
