from flask_pymongo import MongoClient
from collections import OrderedDict
import json

client = MongoClient('mongodb://localhost:27017/')


with open('../data/rotterdam_geolocations.json') as data_file:
    geolocations = json.load(data_file)

    db = client.safetyScore
    collection = db.safetyScore
    newCollection = db.geolocations

    # Force to dictionary for mongodb
    sorted_dict = dict(geolocations)

    print(sorted_dict)

    # add to DB
    newCollection.insert_one(sorted_dict)

    print("added (updated) geolocations to DB")
