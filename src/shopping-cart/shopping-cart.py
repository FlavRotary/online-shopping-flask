from flask import Flask, jsonify, current_app, g
from flask_restful import Api
from flask_pymongo import MongoClient
from configparser import ConfigParser
from os import path


from contents import Contents
from add_to_cart import AddToCart
from modify_cart_item import ModifyCartItem
from checkout import Checkout

app = Flask(__name__)

api = Api(app)

config = ConfigParser()
config.read([
    path.abspath('config.ini'),
    path.abspath('sample_config.ini')
])

default_config = config['DEFAULT']
app.config['MONGO_URI'] = default_config['DB_URI']
app.config['JWT_SECRET'] = default_config['JWT_SECRET']


api.add_resource(Contents, '/api/contents')
api.add_resource(AddToCart, '/api/add-to-cart')
api.add_resource(ModifyCartItem, '/api/modify-cart-item')
api.add_resource(Checkout, '/api/checkout')


app.app_context().push()
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')