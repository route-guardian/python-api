from flask_pymongo import MongoClient
from collections import OrderedDict
import json

client = MongoClient('mongodb://localhost:27017/')

db = client.safetyScore
collection = db.safetyScore

with open('../data/crimeMapMarkers.json') as data_file:
    geolocations = json.load(data_file)

    crimeCollection = db.crime

    # Force to dictionary for mongodb
    sorted_dict = dict(geolocations)

    print(sorted_dict)

    # add to DB
    crimeCollection.insert_one(sorted_dict)

    print("added (updated) crime data to DB")

with open('../data/cameras.json') as data_file:
    geolocations = json.load(data_file)

    camerasCollection = db.cameras

    # Force to dictionary for mongodb
    sorted_dict = dict(geolocations)

    print(sorted_dict)

    # add to DB
    camerasCollection.insert_one(sorted_dict)

    print("added (updated) cameras data to DB")
