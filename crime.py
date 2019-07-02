from flask import Blueprint, request
from bson.json_util import dumps
from flask_pymongo import MongoClient
from collections import OrderedDict
# For the blueprint export
crime_api = Blueprint('crime_api', __name__)

client = MongoClient('mongodb://localhost:27017/')

db = client.safetyScore
collection = db.crime


@crime_api.route("/crime")
def returnCrime():
    return dumps(collection.find({}).limit(1).sort([('$natural', -1)]))
