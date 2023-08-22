from flask import *
from flask import jsonify
from flask_cors import CORS

class Product:
    def __init__(self, image, name, description, price):
        self.image = image
        self.name = name
        self.description = description
        self.price = price


fakeDB = {
    "products":{ "000" : Product("Image go here", "Leather Wallet", "This is a Leather Wallet", 20.00),
                
                }
}

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def test_method():
    response = {"text": "YOU GOT THE RESPONSE FROM THE BACKEND"}
    return jsonify(response)


if __name__ == '__main__':
    app.run(port=8888, host="0.0.0.0")

