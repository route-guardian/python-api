from flask import Blueprint

route_api = Blueprint('route_api', __name__)

@route_api.route("/route")
def accountList():
    return "roel is slm"