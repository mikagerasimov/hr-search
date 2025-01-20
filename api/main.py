from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/data", methods=['GET'])
def data ():
    return  jsonify({"msg": "init api-app"}), 200

if __name__ == "__main__":
    app.run(port=8000)