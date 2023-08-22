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
    "leatherwork":{"000" : Product("Image go here", "Leather Wallet", "This is a Leather Wallet", 20.00),
                "001" : Product("Image go here", "Leather Wallet", "This is not Leather Wallet", 21.00),
                "002" : Product("Image go here", "Leather Wallet", "This is a Leather Wallet", 22.00),
                "003" : Product("Image go here", "Leather Wallet", "This is a Leather Wallet", 23.00),
                },
    "dndminis":{"000" : Product("Image go here", "DnD Figure", "This is a plastic Mini", 20.00),
                "001" : Product("Image go here", "DnD Figure", "This is a plastic Mini", 21.00),
                "002" : Product("Image go here", "DnD Figure", "This is a plastic Mini", 22.00),
                "003" : Product("Image go here", "DnD Figure", "This is a plastic Mini", 23.00),
                },
    "3Dprints":{"000" : Product("Image go here", "3D Printed item", "This is a 3D Printed item", 20.00),
                "001" : Product("Image go here", "3D Printed item", "This is a 3D Printed item", 21.00),
                "002" : Product("Image go here", "3D Printed item", "This is a 3D Printed item", 22.00),
                "003" : Product("Image go here", "3D Printed item", "This is a 3D Printed item", 23.00),
                },
}

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def test_method():
    response = {"text": "YOU GOT THE RESPONSE FROM THE BACKEND"}
    return jsonify(response)

# GET Requests for Database
@app.route('/product', methods=['GET'])
def return_product():
    args = request.args
    return jsonify(vars(fakeDB[args.get("category")][args.get("id")]))

if __name__ == '__main__':
    app.run(port=8888, host="0.0.0.0")

