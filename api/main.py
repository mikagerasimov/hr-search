from config import Config
from flask import Flask, jsonify
from flask_cors import CORS
from pipeline import working
from os import path

cfg = Config()
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"index": "hello_backend"})


@app.route('/api/data', methods=['GET'])
def data():
    return jsonify({'msg': 'init api-app'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=cfg.api_port)


#Запуск пайплайна, не работает, не знаю почему
    excel = path.join()
    results = working(excel)
    print(results)
