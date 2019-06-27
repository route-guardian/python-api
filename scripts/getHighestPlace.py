import operator
from flask_pymongo import MongoClient
from collections import OrderedDict


client = MongoClient('mongodb://localhost:27017/')

allData = {}

# x -> is input value
# a,b -> hoogste en laagste van de reeks
# c,d -> in wat voor categorien moet het worden outgeput
# y de value die hij returnt,
def mapFromTo(x,a,b,c,d): 
    y=(x-a)/(b-a)*(d-c)+c
    return round(y)



db = client.safetyScore
collection = db.safetyScore
newCollection = db.safetyScoreSorted
# Get the latest item
for post in collection.find({}, {'_id': False}).limit(1).sort([( '$natural', -1 )]):
    for gebied, value in post.items():
        for wijk, value in value.items():
            # I have the data here`
            wijkData = []

            for nameData, data in value['data'].items():
                wijkData.append(data)
            calculatedData = sum(wijkData)
            allData.update({wijk : calculatedData})
        pass
    pass  
# Sort the array/dict
sorted_x = sorted(allData.items(), key=lambda x: x[1], reverse = True)
# Change
sorted_dict = dict(OrderedDict(sorted_x)) #Force to dictionary for mongodb

testing = {}

print(allData[min(allData.items(), key=operator.itemgetter(1))[0]]);
print(allData[max(allData.items(), key=operator.itemgetter(1))[0]]);
# get it to 1, 100
for name ,value in allData.items():
    testing[name] = mapFromTo(value , allData[min(allData.items(), key=operator.itemgetter(1))[0]], allData[max(allData.items(), key=operator.itemgetter(1))[0]], 1, 100)

print(testing)
# add to DB
newCollection.insert_one(testing)

print("added to DB")

# Sort : https://stackoverflow.com/questions/4110665/sort-nested-dictionary-by-value-and-remainder-by-another-value-in-python

# Write psuede code
# 
# 1. Count together all the scores per wijk
# 2. check the endscore
# 3. compore this to all the different wijken
# 4. sorteer dit en zet de hoogste boven aan.   
#    
