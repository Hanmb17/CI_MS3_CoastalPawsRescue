import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def home():
    return render_template('index.html')
    
@app.route("/get_dogs")
def get_dogs():
    dogs = mongo.db.dogs.find()
    return render_template("dogs.html", dogs=dogs)

@app.route("/get_login_signup")
def get_login_signup():
    return render_template('login_signup.html')

@app.route("/adoption_form")
def adoption_form():
    return render_template('adoption_form.html')

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)