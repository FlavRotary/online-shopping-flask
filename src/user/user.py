from flask import Flask, jsonify, current_app, g
from flask_restful import Api
from flask_pymongo import MongoClient

from Auth import Login
from CreateUser import UsersList
from UserData import ReturnUser

app = Flask(__name__)

api = Api(app)

api.add_resource(Login, '/api/auth')
api.add_resource(UsersList, 'api/users/')
api.add_resource(ReturnUser, 'api/users/<string:uuid>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')