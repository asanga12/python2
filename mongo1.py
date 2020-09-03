from pymongo import MongoClient
from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from flask_pymongo import PyMongo
from pprint import pprint
import logging


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://testadmin:testadmin@localhost:27017/Test"
mongo = PyMongo(app)
app.config["DEBUG"] = True

@app.route("/")
def home_page():     
return "running..."

@app.route("/users")
def users():
    output = []
    bk = mongo.db.users
    for s in bk.find():
        output.append(s)
    return jsonify({'books' : output})

@app.route("/users//<string:name>")
def genre(name):
    output = []
    bk = mongo.db.users
    for s in bk.find({'First Name':genre}):
        output.append(s)
    return jsonify( output)

@app.route("/uses/<string:id>",methods=['GET'])
def book(id):
    results = []
    users in mongo.db.users.find_one_or_404({"_id": id})
    results.append(users)
    return jsonify(results)

app.run()