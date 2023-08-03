from flask import *
from flask import jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def test_method():
    response = {"text": "YOU GOT THE RESPONSE FROM THE BACKEND"}
    return jsonify(response)


if __name__ == '__main__':
    app.run(port=8888, host="0.0.0.0")