from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient
from auth import auth
from views import views

app = Flask(__name__)

def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                        authSource="admin")
    db = client["users"]
    return db

#@app.route("/")
#def hello_world():
#    return "<p>Hello from user!</p>"

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')