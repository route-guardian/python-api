from flask_pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.safetyScore
collection = db.safetyScore
# Get the latest item
for post in collection.find({}).limit(1).sort([( '$natural', -1 )]):
    for key, value in post.items():
        print(key, value)
    pass

# Sort : https://stackoverflow.com/questions/4110665/sort-nested-dictionary-by-value-and-remainder-by-another-value-in-python