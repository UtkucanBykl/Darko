from flask import Flask, jsonify, request
from darko import Darko

app = Flask(__name__)
darko = Darko()

@app.route("/nodes")
def index():
    node = [x.name for x in darko.get_all_nodes()]
    return jsonify({'node': node})

@app.route('/create')
def create():
    data = request.args.get('sentence')
    darko.create(data)
    return jsonify({'status': 'success'})

@app.route('/<name>')
def get_node(name):
    node = darko.get(name)
    if node:
        return node.name
    return 'We dont get anything'


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, port=12345, use_reloader=True)