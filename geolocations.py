from flask import Blueprint, request
from bson.json_util import dumps
from flask_pymongo import MongoClient
from collections import OrderedDict
# For the blueprint export
geolocations_api = Blueprint('geolocations_api', __name__)

client = MongoClient('mongodb://localhost:27017/')

db = client.safetyScore
collection = db.geolocations


@geolocations_api.route("/geolocations")
def returnGeolocations():
    return dumps(collection.find({}).limit(1).sort([('$natural', -1)]))
