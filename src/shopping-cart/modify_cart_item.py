from flask import jsonify, g
from flask_restful import Resource, reqparse

from mongo import mongo

from decorators import authenticate

test_email = "user1@example.com"

parser = reqparse.RequestParser()
parser.add_argument('product_id', type=int, required=True)
parser.add_argument('quantity', type = int, required=False)

class ModifyCartItem(Resource):
    method_decorators = [authenticate]
    def post(self):
        
        params = parser.parse_args()
        email = g.logged_in_user
        quantity = params['quantity'] if params['quantity'] else 0
        
        
        # target_product = (product for product in mongo.users.find_one({'email': email}, {'cart_items': 1})['cart_items'] if product['id']==id)
        # target_product []
        
        if quantity !=0:
            mongo.users.update_one({'email': email, 'cart_items.id': params['product_id']}, {'$set': {'cart_items.$.quantity': quantity}})
        else:
            mongo.users.update_one({'email':email}, {'$pull': {'cart_items': {'id': params['product_id']}}})
        
        return jsonify({
            'results': {'contents': mongo.users.find_one({'email': email}, {'cart_items': 1})['cart_items']}
        })