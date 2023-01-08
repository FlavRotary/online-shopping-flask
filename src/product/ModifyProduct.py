from flask import jsonify
from flask_restful import Resource, reqparse

from mongo import mongo

parser = reqparse.RequestParser()

parser.add_argument('name', type = str, required = False)
parser.add_argument('price', type = float, required = False)
parser.add_argument('description', type = str, required = False)
parser.add_argument('stockLeft', type = int, required = False)


class ModifyProduct(Resource):
    def post(self, uuid):
        params = parser.parse_args()

        if params['name'] :
            mongo.products.update_one({'uuid': uuid }, {'$set': {'name': params['name']}})    
        
        
        if params['price'] :
            mongo.products.update_one({'uuid': uuid }, {'$set': {'price': params['price']}})

        
        if params['description'] :
            mongo.products.update_one({'uuid': uuid }, {'$set': {'description': params['description']}})

        
        if params['stockLeft'] :
            mongo.products.update_one({'uuid': uuid }, {'$set': {'stockLeft': params['stockLeft']}})

        return jsonify({'result': mongo.products.find_one_or_404({'uuid': uuid}, {'_id': 0})})

        