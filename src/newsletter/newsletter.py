import os
from flask import Flask, jsonify
from flask_pymongo import MongoClient
from flask_mail import Mail, Message
from os import path
from configparser import ConfigParser


from mongo import mongo

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
app.config['MAIL_SERVER'] = default_config['MAIL_SERVER']
app.config['MAIL_PORT'] = default_config['MAIL_PORT']
app.config['MAIL_USERNAME'] = default_config['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = default_config['MAIL_PASSWORD']
app.config['MAIL_DEFAULT_SENDER'] = default_config['MAIL_DEFAULT_SENDER']
app.config['MAIL_USE_TLS'] = default_config['MAIL_USE_TLS']
app.config['MAIL_USER_SSL'] = default_config['MAIL_USER_SSL']
mail = Mail(app)

@app.route("/")
def index():
    sent = []
    products = mongo.products.find()
    test_email = ['flavian.daniel.rotaru@gmail.com']
    # for email in mongo.users.distinct('email'):
    for email in test_email:
        msg = Message('Hello from Online-Shopping', sender = app.config['MAIL_DEFAULT_SENDER'], recipients = [email])
        msg.body = "Hi! Here is a list of all the products we currently have on stock.\n"
        for product in products:
            msg.body += "- " + product['name'] + "\n  " + str(product['price']) + '\n'
        msg.body += "\nSee you online!"
        mail.send(msg)
        sent.append(email)
    
    return jsonify({'result': sent})
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')