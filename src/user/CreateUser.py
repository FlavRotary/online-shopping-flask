from flask import jsonify
from flask_restful import Resource, reqparse
from uuid import uuid4

import hashlib

from mongo import mongo
from exceptions import EmailAlreadyRegistered

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('email', type=str, required=True)
parser.add_argument('password', type=str, required=True)


class UsersList(Resource):
    def post(self):
        params = parser.parse_args()

        if mongo.users.find_one({'email': params['email']}, {'email': 1}):
            raise EmailAlreadyRegistered

        doc = {
            'uuid': str(uuid4()),
            'name': params['name'],
            'email': params['email'],
            'password': hashlib.sha256(params['password'].encode('utf-8')).hexdigest()
        }

        mongo.users.insert_one(doc)

        doc.pop('_id', None)
        doc.pop('password', None)
        return jsonify({'result': doc})
