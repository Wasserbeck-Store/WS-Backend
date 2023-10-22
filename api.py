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
    "Leather Work":{"000" : Product("Image go here", "Leather Wallet", "This is a wallet made of leather. You can tell its made of leather by the way its made of leather. The leather wallet knows its made of leather by the way it feels like leather.", 20.00).__dict__,
                "001" : Product("Image go here", "Leather Wallet", "This is a wallet made of leather. You can tell its made of leather by the way its made of leather. The leather wallet knows its made of leather by the way it feels like leather.", 21.00).__dict__,
                "002" : Product("Image go here", "Leather Wallet", "This is a wallet made of leather. You can tell its made of leather by the way its made of leather. The leather wallet knows its made of leather by the way it feels like leather.", 22.00).__dict__,
                "003" : Product("Image go here", "Leather Wallet", "This is a wallet made of leather. You can tell its made of leather by the way its made of leather. The leather wallet knows its made of leather by the way it feels like leather.", 23.00).__dict__,
                "004" : Product("Image go here", "Leather Wallet", "This is a wallet made of leather. You can tell its made of leather by the way its made of leather. The leather wallet knows its made of leather by the way it feels like leather.", 23.00).__dict__,
                "005" : Product("Image go here", "Leather Wallet", "This is a wallet made of leather. You can tell its made of leather by the way its made of leather. The leather wallet knows its made of leather by the way it feels like leather.", 23.00).__dict__,
                "006" : Product("Image go here", "Leather Wallet", "This is a wallet made of leather. You can tell its made of leather by the way its made of leather. The leather wallet knows its made of leather by the way it feels like leather.", 23.00).__dict__,
                "007" : Product("Image go here", "Leather Wallet", "This is a wallet made of leather. You can tell its made of leather by the way its made of leather. The leather wallet knows its made of leather by the way it feels like leather.", 23.00).__dict__,

                },
    "D&D Minis":{"000" : Product("Image go here", "DnD Figure", "This is a plastic Mini This is a plastic Mini This is a plastic Mini This is a plastic Mini This is a plastic Mini", 20.00).__dict__,
                "001" : Product("Image go here", "DnD Figure", "This is a plastic Mini This is a plastic Mini This is a plastic Mini This is a plastic Mini This is a plastic Mini", 21.00).__dict__,
                "002" : Product("Image go here", "DnD Figure", "This is a plastic Mini This is a plastic Mini This is a plastic Mini This is a plastic Mini This is a plastic Mini", 22.00).__dict__,
                "003" : Product("Image go here", "DnD Figure", "This is a plastic Mini This is a plastic Mini This is a plastic Mini This is a plastic Mini This is a plastic Mini", 23.00).__dict__,
                },
    "3D Prints":{"000" : Product("Image go here", "3D Printed item", "This is a 3D Printed item This is a 3D Printed item This is a 3D Printed item This is a 3D Printed item This is a 3D Printed item", 20.00).__dict__,
                "001" : Product("Image go here", "3D Printed item", "This is a 3D Printed item This is a 3D Printed item This is a 3D Printed item This is a 3D Printed item This is a 3D Printed item", 21.00).__dict__,
                "002" : Product("Image go here", "3D Printed item", "This is a 3D Printed item This is a 3D Printed item This is a 3D Printed item This is a 3D Printed item This is a 3D Printed item", 22.00).__dict__,
                "003" : Product("Image go here", "3D Printed item", "This is a 3D Printed item This is a 3D Printed item This is a 3D Printed item This is a 3D Printed item This is a 3D Printed item", 23.00).__dict__,
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
    return jsonify(fakeDB[args.get("category")][args.get("id")])

@app.route('/categoryProducts', methods=['GET'])
def return_categoryProducts():
    args = request.args
    print("----------------------------------------")
    print(fakeDB[args.get("category")])
    print("----------------------------------------")
    return jsonify(fakeDB[args.get("category")])

if __name__ == '__main__':
    app.run(port=8888, host="0.0.0.0")

