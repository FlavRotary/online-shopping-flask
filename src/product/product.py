from configparser import ConfigParser
from os import path
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

default_config = config['DEFAULT']
app.config['MONGO_URI'] = default_config['DB_URI']
app.config['JWT_SECRET'] = default_config['JWT_SECRET']

api = Api(app)

api.add_resource(AddProduct, '/api/products/add_product')
api.add_resource(ReturnProduct, '/api/products/<string:uuid>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')