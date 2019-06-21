from flask import Flask, request
from flask_pymongo import PyMongo
# Import routes
from route import route_api
from points import points_api
import socket

hostname = socket.gethostname()

app = Flask(__name__)

# Setup the mongoDB
app.config["MONGO_DBNAME"] = "routeGuardian"
app.config["MONGO_URI"] = "mongodb://localhost:27017/firstDB"
# Add mongo to server
mongo = PyMongo(app)

# This blueprint adds other routes from other files
app.register_blueprint(route_api)
app.register_blueprint(points_api)


@app.route("/", methods = ["GET", "POST"])
def users():
    if request.method == 'POST':
        return 'Put something to post here'    
    else:
        return '{ "name":"John", "age":30, "city":"New York"}'
 
@app.route("/hello")
def testRoute():
    return 'ik snap python niet'

if __name__ == "__main__":
    if 'ip' in hostname:
        app.run(host="0.0.0.0")
    else:
        app.run( use_reloader = True)
