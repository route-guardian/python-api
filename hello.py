from flask import Flask
from flask import request
from route import route_api
app = Flask(__name__)
 
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
    app.run( use_reloader = True)