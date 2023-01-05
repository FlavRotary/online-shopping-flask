from configparser import ConfigParser
from os import path
from flask import Flask, jsonify, current_app, g
from flask_restful import Api
from flask_pymongo import MongoClient

from auth import Login
from CreateUser import UsersList
from UserData import ReturnUser

app = Flask(__name__)

config = ConfigParser()
config.read([
    path.abspath('config.ini'),
    path.abspath('sample_config.ini')
])

default_config = config['DEFAULT']
app.config['MONGO_URI'] = default_config['DB_URI']
app.config['JWT_SECRET'] = default_config['JWT_SECRET']
# app.config.update(default_config)

api = Api(app)

api.add_resource(Login, '/api/auth')
api.add_resource(UsersList, '/api/users/')
api.add_resource(ReturnUser, '/api/users/<string:uuid>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')