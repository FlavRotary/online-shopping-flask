from flask import jsonify, current_app
from flask_restful import Resource,  reqparse
from mongo import mongo
from exceptions import ProductAlreadyInDatabase
from uuid import uuid4


parser = reqparse.RequestParser()

parser.add_argument('name', type = str, required = True)
parser.add_argument('price', type = float, required = True)
parser.add_argument('description', type = str, required = False)
parser.add_argument('stockLeft', type = int, required = True)

class AddProduct(Resource):
    def post(self):
        params = parser.parse_args()

        if mongo.users.find_one({'name': params['name']}, {'name': 1}):
            raise ProductAlreadyInDatabase

        doc = {
            'uuid': str(uuid4()),
            'name': params['name'],
            'price': params['price'],
            'description': params['description'],
            'stockLeft': params['stockLeft']
        }

        mongo.products.insert_one(doc)

        return jsonify({'result': doc})
