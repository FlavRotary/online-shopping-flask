from flask import Flask, jsonify, current_app, g
from flask_restful import Api
from flask_pymongo import MongoClient

from auth import Login

app = Flask(__name__)

api = Api(app)

api.add_resource(Login, '/api/auth')

#@app.route("/")
#def hello_world():
#    return "<p>Hello from user!</p>"

#app.register_blueprint(views, url_prefix='/')
#app.register_blueprint(auth, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')