import requests
from .config import apiKeyz

# In data there is start point and endpoint
def getLatLong(data):
    # url : https://api.mapbox.com/directions/v5/mapbox/driving/-122.42,37.78;-77.03,38.91?access_token=pk.eyJ1Ijoicm9lbHZvb3JkZW5kYWciLCJhIjoiY2p3dWkwaXYwMHo3ajN5cXYyeGEya3J5dyJ9.7jDGpM77HWMGOk-P6-Aqfw
    response = requests.get("https://api.mapbox.com/directions/v5/mapbox/driving/" + str(data["startPoint"]["long"]) + "," +  str(data["startPoint"]["lat"]) + ";" + str(data["endPoint"]["long"]) + "," +  str(data["endPoint"]["lat"]) +"?access_token=" + apiKey).json()

    print(response["waypoints"])
