from flask import Blueprint , request
from bson.json_util import dumps
import json
# For the blueprint export
route_api = Blueprint('route_api', __name__)
from route import mongo
# Setuo db in route
user = mongo.db.users

@route_api.route("/route", methods = ["GET", "POST"])
def accountList():
    if request.method == "POST":
        # Get the data from the request 
        data = json.loads(request.data)
        username = data['name']
        # Check if request was filled and insert in db
        if username: 
            user.insert({
                "name" : username,
            })
        return "Dit is een POST",201
    else:
        # Find all the user in the DB
        users = mongo.db.users.find({})
        return dumps(users)