from flask_pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.safetyScore
collection = db.safetyScore
# Get the latest item
for post in collection.find({}, {'_id': False}).limit(1).sort([( '$natural', -1 )]):
    for gebied, value in post.items():
        for wijk, value in value.items():
            print(value['data'])
        pass
    pass    

# Sort : https://stackoverflow.com/questions/4110665/sort-nested-dictionary-by-value-and-remainder-by-another-value-in-python

# Write psuede code
# 
# 1. Count together all the scores per wijk
# 2. check the endscore
# 3. compore this to all the different wijken
# 4. sorteer dit en zet de hoogste boven aan.   
#    
