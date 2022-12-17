import jwt
from flask import jsonify, current_app
from flask_restful import Resource, reqparse
import hashlib
from mongo import mongo

parser = reqparse.RequestParser()
parser.add_argument('email')
parser.add_argument('password', type=str, required=True)

class Login(Resource):
    def post(self):
        params = parser.parse_args()

        user = mongo.users.find_one({
            'email': params['email'],
            'password': hashlib.sha256(params['password'].encode('utf-8')).hexdigest()
        })

        jwt_token = jwt.encode({'sub': user['email']}, current_app.config['JWT_SECRET'], algorithm='HS256')

        return jsonify({
            'result': {
                'token': jwt_token.decode('utf-8')
            }
        })
