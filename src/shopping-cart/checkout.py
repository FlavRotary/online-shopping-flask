from flask import jsonify, g
from flask_restful import Resource, reqparse

from mongo import mongo

from decorators import authenticate

test_email = "user1@example.com"


class Checkout(Resource):
    method_decorators = [authenticate]
    
    def post(self):
        
        email = g.logged_in_user
        
        current_order_number = len(mongo.users.find_one({'email': email})['past_orders']) + 1
        
        order = mongo.users.find_one({'email': email}, {'cart_items': 1})['cart_items']
        past_order = {'id': current_order_number, 'ordered_items': order}
        mongo.users.update_one({'email': email}, {'$addToSet': {'past_orders': past_order}})
        mongo.users.update_many({'email':email}, {'$pull': {'cart_items': {}}})
        
        return jsonify({
            'results': {'contents': mongo.users.find_one({'email': email}, {'cart_items': 1})['cart_items']}
        })