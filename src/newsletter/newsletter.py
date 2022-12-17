from flask import Flask, jsonify
from flask_pymongo import MongoClient

app = Flask(__name__)

def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                        authSource="admin")
    db = client["users"]
    return db

@app.route("/")
def hello_world():
    return "<p>Hello from newsletter!</p>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')