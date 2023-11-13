import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for
)
from flask_pymongo import PyMongo
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
    return render_template("index.html")


@app.route("/get_dogs")
def get_dogs():
    dogs = mongo.db.dogs.find()
    return render_template("dogs.html", dogs=dogs)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {
                "$or": [
                    {"username": request.form.get("username").lower()},
                    {"email": request.form.get("email").lower()},
                ]
            }
        )
        # check if username and email already exists in db
        if existing_user:
            if (
                existing_user.get("username") == request.form.get(
                    "username").lower()
                and existing_user.get("email") == request.form.get(
                    "email").lower()
            ):
                flash(
                    "Both username and email already exist. "
                    "Please log in or use different username and email to "
                    "create a new account."
                )
            elif existing_user.get("username") == request.form.get(
                    "username").lower():
                flash("Username already exists. Please choose a different "
                      "one.")
            elif existing_user.get("email") == request.form.get(
                    "email").lower():
                flash(
                    "This email is already registered. "
                    "Please log in or use a different email to create a "
                    "new account."
                )
        else:
            register = {
                "username": request.form.get("username").lower(),
                "email": request.form.get("email").lower(),
                "password": generate_password_hash(request.form.get(
                    "password")),
            }
            mongo.db.users.insert_one(register)

            # put the new user into 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("Registration Successful!")

    return render_template("signup.html")


@app.route("/get_login_signup", methods=["GET", "POST"])
def get_login_signup():
    if request.method == "POST":
        # Check if the username exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Check if the provided password matches the stored hashed password
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = existing_user["username"].lower()
                flash("Login Successful!")
                return redirect(url_for("home"))
            else:
                flash("Incorrect password. Please try again.")
        else:
            flash("Username not found. "
                  "Please check your username or register.")

    return render_template("login_signup.html")


@app.route("/logout")
def logout():
    # Remove the user from the session
    session.pop("user", None)
    flash("You have been logged out.")
    return redirect(url_for("home"))


@app.route("/adoption_form")
def adoption_form():
    return render_template("adoption_form.html")

@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(
        os.environ.get("PORT")), debug=True)
