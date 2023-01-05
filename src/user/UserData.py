from flask import jsonify
from flask_restful import Resource

from mongo import mongo


class ReturnUser(Resource):

    def get(self, uuid):
        return jsonify({'result': mongo.users.find_one_or_404({'uuid': uuid}, {'_id': 0, 'password': 0})})
