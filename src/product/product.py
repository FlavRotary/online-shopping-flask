from configparser import ConfigParser
from os import path
import os
from flask import Flask, jsonify
from flask_pymongo import MongoClient
from flask_restful import Api

from AddProduct import AddProduct
from GetProduct import ReturnProduct

app = Flask(__name__)

config = ConfigParser()
config.read([
    path.abspath('config.ini'),
    path.abspath('sample_config.ini')
])

username = os.environ['MONGO_INITDB_ROOT_USERNAME']
password = os.environ['MONGO_INITDB_ROOT_PASSWORD']
db_name = os.environ['MONGO_INITDB_DATABASE']

default_config = config['DEFAULT']
app.config['MONGO_URI'] =  'mongodb://' + username + ':' + password + '@mongo/' + db_name
app.config['JWT_SECRET'] = default_config['JWT_SECRET']

api = Api(app)

api.add_resource(AddProduct, '/api/products/add_product')
api.add_resource(ReturnProduct, '/api/products/<string:uuid>')


if __name__ == '__main__':
    app.run(debug=True)