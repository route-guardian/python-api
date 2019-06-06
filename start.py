from flask import Flask
from flask import request
from route import route_api
from flask_pymongo import PyMongo
import socket

hostname = socket.gethostname()

app = Flask(__name__)

# Setup the mongoDB
app.config["MONGO_DBNAME"] = "testing"
app.config["MONGO_URI"] = "mongodb://localhost:27017/firstDB"
# Add mongo to server
mongo = PyMongo(app)

# This blueprint adds other routes from other files
app.register_blueprint(route_api)


@app.route("/", methods = ["GET", "POST"])
def hello():
    if request.method == 'POST':
        return 'Dit is een post'    
    else:
        return '{ "name":"John", "age":30, "city":"New York"}'
 
@app.route("/hello")
def test():
    return 'ik snap python niet'

if __name__ == "__main__":
    if 'ip' in hostname:
        app.run(host="0.0.0.0", port=80)
    else:
        app.run( use_reloader = True)
