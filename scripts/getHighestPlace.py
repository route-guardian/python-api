from flask_pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.safetyScore
collection = db.safetyScore

for post in collection.find({}):
    print(post)