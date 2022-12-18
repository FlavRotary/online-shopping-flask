from flask import jsonify, g
from flask_restful import Resource, reqparse

from mongo import mongo

test_email = "user1@example.com"

class Contents(Resource):
    # method_decorators = [authenticate]
    
    def get(self):
        # email = g.logged_in_user
        email = test_email
        
        return jsonify({
            'results': {'contents': mongo.users.find_one({'email': email}, {'cart_items': 1})['cart_items']}
        })
        
        
        