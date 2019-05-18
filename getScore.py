import re
import json
from pprint import pprint
# get data from json file
with open('data/rotterdam_safety_data.json') as f:
    data = json.load(f)

testData = {
    "Charlois": {
            "Tarwewijk" : {
                "id": 71,
                "data": {
                    "Veiligheidsindex" : 73,
                    "Veiligheidsindex -subjectief" : "50%"
                }
            },
            "Carnisse" : {
                "id": 71,
                "data": {
                    "Veiligheidsindex" : 50,
                    "Veiligheidsindex -subjectief" : "70%" 
                }
            },
            "ss" : {
                "id": 71,
                "data": {
                    "Veiligheidsindex" : 60,
                    "Veiligheidsindex -subjectief" : "60%" 
                }
            }
    }
}

# x -> is input value
# a,b -> hoogste en laagste van de reeks
# c,d -> in wat voor categorien moet het worden outgeput
# y de value die hij returnt,
def mapFromTo(x,a,b,c,d): 
    y=(x-a)/(b-a)*(d-c)+c
    return round(y)

for key , district in data.items():
    

    pass

# index = district["Veiligheidsindex"]
# Get started with index    
# Get highest and lowest value out of loop

i=0
j=0
allValues = {}

# In these for loops all the values get tosses in the object allValues and get added to the array where they belong
for gebied, district in data.items():
    for district, value in district.items():
        for key, value in value['data'].items():
            # change string percentages to ints
            if isinstance(value, str):
                value = int(value.strip('%'))

            if j>0:
                allValues[i].append(value)
            else:
                allValues[i] = [value]
            i+=1
        pass
        i=0
        j=1
    pass

#value to keep track of looping
a = 0 
#for loops to change the highest instance  
for gebied, district in data.items():
    for district, value in district.items():
        for key, value in value['data'].items():
            value = data[gebied][district]['data'][key]
            if isinstance(value, str):
                value = int(value.strip('%'))
            print (value)
            # Overwrite old value with new value
            data[gebied][district]['data'][key] = mapFromTo(value, min(allValues[a]), max(allValues[a]), 1, 5) # Get data from function   
            a +=1       
            pass
        a = 0
        pass
    pass

print (data)

# print (mapFromTo(20, 30, 0, 1,5))

# print (data)