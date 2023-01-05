from configparser import ConfigParser
from os import path
from flask import Flask, jsonify
from flask_pymongo import MongoClient

app = Flask(__name__)

config = ConfigParser()
config.read([
    path.abspath('config.ini'),
    path.abspath('sample_config.ini')
])

default_config = config['DEFAULT']
app.config.update(default_config)

def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                        authSource="admin")
    db = client["products"]
    return db

@app.route("/")
def hello_world():
    return "<p>Hello from product!</p>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')