# IMPORT MODULES
from flask import Flask,jsonify,request
from data import data

# CREATE THE API BODY
app = Flask(__name__)

# CREATE THE ROUTE
@app.route("/")

# GIVE THE DATA IN THE API
def index():
    return jsonify({
        "data":data,
        "message":"success"
    }),200

# ADD THE DATA OF A PARTICULAR PLANET WHICH IS SEARCHED
@app.route("/star")

def planet():
    name = request.args.get("name")
    star_data = next(item for item in data if item["name"]== name)
    return jsonify({
        "data":star_data,
        "message":"success"
    }),200


# CODE FOR RUNNING THE API
if __name__ == "__main__":
    app.run()

