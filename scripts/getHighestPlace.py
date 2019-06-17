from flask_pymongo import MongoClient
import collections
from collections import OrderedDict


client = MongoClient('mongodb://localhost:27017/')

allData ={}

db = client.safetyScore
collection = db.safetyScore
newCollection = db.safetyScoreSorted

# Get the latest item
for post in collection.find({}, {'_id': False}).limit(1).sort([( '$natural', -1 )]):
    for gebied, value in post.items():
        for wijk, value in value.items():
            # I have the data here`
            wijkData = []

            # print(wijk)
            for nameData, data in value['data'].items():
                # print(nameData)
                # print(data)
                wijkData.append(data)
            calculatedData = sum(wijkData)
            allData.update({wijk : calculatedData})
        pass
         # break to end extra looping
    pass    
# Sort the array/dict
sorted_x = sorted(allData.items(), key=lambda x: x[1], reverse = True)
# Change
sorted_dict = dict(collections.OrderedDict(sorted_x)) #Force to dictionary for mongodb

print(sorted_dict)

# add to DB
newCollection.insert_one(sorted_dict)

print("added to DB")

# Sort : https://stackoverflow.com/questions/4110665/sort-nested-dictionary-by-value-and-remainder-by-another-value-in-python

# Write psuede code
# 
# 1. Count together all the scores per wijk
# 2. check the endscore
# 3. compore this to all the different wijken
# 4. sorteer dit en zet de hoogste boven aan.   
#    
