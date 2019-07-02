from flask import Blueprint, request
from bson.json_util import dumps
from flask_pymongo import MongoClient
from collections import OrderedDict
# For the blueprint export
cameras_api = Blueprint('cameras_api', __name__)

client = MongoClient('mongodb://localhost:27017/')

db = client.safetyScore
collection = db.cameras


@cameras_api.route("/cameras")
def returnCameras():
    return dumps(collection.find({}).limit(1).sort([('$natural', -1)]))
