# This rout is for returning safety points
from flask import Blueprint, request
from bson.json_util import dumps # To dump files
import json

points_api = Blueprint('points_api', __name__)

@points_api.route("/point", methods = ["GET", "POST"])
def returnPoint():
    if request == "POST":
        # code for a post
        print("post")
    else:
        # Code for a get
        return 'LMAO we here bois'    

