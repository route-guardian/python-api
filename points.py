# This rout is for returning safety points
from scripts import getLatLong
from flask import Blueprint, request
from bson.json_util import dumps # To dump files
import json

points_api = Blueprint('points_api', __name__)

@points_api.route("/point", methods = ["GET", "POST"])
def returnPoint():
    if request.method == "POST":
        data = json.loads(request.data)
        if  data['endPoint'] and data['startPoint']:
            # Create data end get all poitns
            route = getLatLong.getLatLong(data) # Get lat en Long from other function

        return dumps(route)
    else:
        # Code for a get
        return 'LMAO we here bois'    

