import requests
import json
from .config import APPCODE
from .config import APPID


avoidAreas = []

with open('data/crime.json') as data_file:
    crime = json.load(data_file)
i = 0
for long, lat in crime["points"]:
    avoidAreas.append(str(lat))
    avoidAreas.append(",")
    avoidAreas.append(str(long))
    if(i == 1):
       avoidAreas.append("!")
       i=0
    else:
        avoidAreas.append(";") 
        i+=1


avoidAreas.pop()

stringAvoidArreas = ''.join(avoidAreas)

print(stringAvoidArreas)

with open('data/cameras.json') as data_file:
    cameras = json.load(data_file)

# In data there is start point and endpoint
def getLatLong(data):
    # url : https://api.mapbox.com/directions/v5/mapbox/driving/-122.42,37.78;-77.03,38.91?access_token=pk.eyJ1Ijoicm9lbHZvb3JkZW5kYWciLCJhIjoiY2p3dWkwaXYwMHo3ajN5cXYyeGEya3J5dyJ9.7jDGpM77HWMGOk-P6-Aqfw
    response = requests.get("https://route.api.here.com/routing/7.2/calculateroute.json?app_id=" + APPID + "&app_code=" + APPCODE + "&waypoint0=geo!" + str(data["startPoint"]["lat"]) + "," + str(data["startPoint"]["long"]) + "&waypoint1=geo!"+ str(data["endPoint"]["lat"]) + "," + str(data["endPoint"]["long"]) + "&mode=fastest;pedestrian;traffic:disabled&avoidareas=" + str(stringAvoidArreas)).json()

    return response
