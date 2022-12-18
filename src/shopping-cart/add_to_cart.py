from flask import jsonify, g
from flask_restful import Resource, reqparse

from mongo import mongo

test_email = "user1@example.com"

parser = reqparse.RequestParser()
parser.add_argument('product_id', type=int, required=True)
parser.add_argument('quantity', type = int, required=False)

class AddToCart(Resource):
    # method_decorators = [authenticate]
    
    def post(self):
        
        params = parser.parse_args()
        email = test_email
        quantity = params['quantity'] if params['quantity'] else 0
        
        query = {'email': email}
        
        # mongo.products.find_one_or_404({'id': params['product_id']}, {'_id': 1})
        
        product = mongo.products.find_one({'id': params['product_id']}, {'_id': 0})
        product.pop('_id', None)
        product['quantity'] = quantity
        
        mongo.users.update_one(query, {'$addToSet': {'cart_items': product}})
        
        return jsonify({
            'results': {'contents': mongo.users.find_one({'email': email}, {'cart_items': 1})['cart_items']}
        })
        
        
        
        