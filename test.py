data = {
    "Charlois": {
            "Tarwewijk" : {
                "id": 71,
                "data": {
                    "Veiligheidsindex" : 73,
                    "Veiligheidsindex -subjectief" : 54
                }
            },
            "Carnisse" : {
                "id": 71,
                "data": {
                    "Veiligheidsindex" : 86,
                    "Veiligheidsindex -subjectief" : 68
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

for gebied, district in data.items():
    for district, value in district.items():
        for key, value in value['data'].items():
            # print(key)
            # print(value)
            # overwrite value with new calulated index
            # print (key)
            print(key)
            print(data[gebied][district][key])
            # data[gebied][district][key] 
            # print(data)
            pass
        pass
    pass



# print (mapFromTo(20, 30, 0, 1,5))

# print (data)