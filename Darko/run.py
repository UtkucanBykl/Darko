from flask import Flask, request
from flask.json import jsonify
import json
from starter import Start
from darko import Darko
from signal_handlers import SignalHandler

app = Flask(__name__)
darko = Darko()


@app.route('/nodes/', methods=['POST', 'PUT', 'GET', 'PATCH', 'DELETE'])
def retrieve_create_update():
    if request.method == 'POST':
        data = request.json.get('sentence', [])
        try:
            status = all((map(lambda x: darko.create(sentence=x), data)))
            return jsonify({'status': status})
        except BaseException as e:
            return jsonify({'error': str(e)})
    elif request.method == 'GET':
        node = json.loads(darko.get_all_nodes())
        return jsonify({'data': node})

    elif request.method in ('PUT', 'PATCH'):
        try:
            data = request.json.get('sentence', [])
            status = all((map(lambda x: darko.update(sentence=x), data)))
            return jsonify({'status': status})
        except BaseException as e:
            return jsonify({'error': str(e)})

    elif request.method == 'DELETE':
        try:
            data = request.json.get('sentence', [])
            status = all((map(lambda x: darko.delete(sentence=x), data)))
            return jsonify({'status': status})
        except BaseException as e:
            return jsonify({'error': str(e)})
    return {}  # Todo Exceptions


@app.route('/nodes/<name>')
def get_node(name):
    node = darko.get(name)
    if type(node) == dict:
        return jsonify({'error': 'We dont get anything'})
    return jsonify({'data': json.loads(node)})


def start():
    signal = SignalHandler()
    signal.save()
    Start.start()
    app.run(host='127.0.0.1', debug=True, port=12345, use_reloader=False)


if __name__ == "__main__":
    start()
