import os

from flask import Flask, jsonify

API_PORT = int(os.getenv('API_PORT', '8000'))

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return jsonify({"index": "index"})


@app.route('/api/data', methods=['GET'])
def data():
    return jsonify({'msg': 'init api-app'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=API_PORT)
