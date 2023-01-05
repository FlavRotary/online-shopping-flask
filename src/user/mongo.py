from flask import current_app, g
from flask_pymongo import PyMongo
from werkzeug.local import LocalProxy


def get_mongo():
    mongo_instance = getattr(g, 'mongodb', None)

    if mongo_instance is None:
        mongo_instance = g.mongodb = PyMongo(current_app).db

    return mongo_instance


mongo = LocalProxy(get_mongo)
