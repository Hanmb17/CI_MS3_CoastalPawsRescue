import os
import random
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for
)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date, timedelta

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Utility function to work out birthdates


def calculate_date_from_age(age):
    """
    Calculate the birthdate of a dog based on an age.

    Arguments:
        age (int): The age of dog in years.

    Returns:
        datetime: The calculated birthdate as a datetime object.
    """
    current_date = datetime.now()
    birthdate = current_date - timedelta(days=365.25 * age)
    birthdate = birthdate.replace(hour=0, minute=0, second=0, microsecond=0)
    return birthdate

# Utility function to calculate dog's age


def calculate_dog_age(dob):
    """
    Calculate the age of a dog based on its date of birth.

    Arguments:
        dob (datetime.date or None): The date of birth of the dog.

    Returns:
        string: The age of the dog in years and months or "Unknown" if the date of birth is not provided.
    """
    if dob is None:
        return "Unknown"

    today = date.today()

    # Calculate the difference in years and months
    age_years = today.year - dob.year - \
        ((today.month, today.day) < (dob.month, dob.day))
    age_months = today.month - dob.month + 12 * \
        ((today.month, today.day) < (dob.month, dob.day))

    # Format the age as "years and months"
    if age_years == 0:
        return f"{age_months} months"
    elif age_years == 1:
        return f"{age_years} year and {age_months} months"
    else:
        return f"{age_years} years and {age_months} months"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_dogs")
def get_dogs():
    dogs = list(mongo.db.dogs.find())

    # Calculate age for each dog
    for dog in dogs:
        dob = dog.get('dateOfBirth')
        dog['age'] = calculate_dog_age(dob)

    return render_template("dogs.html", dogs=dogs)


@app.route("/filter_dogs", methods=["GET", "POST"])
def filter_dogs():
    print('filter running')
    if request.method == "POST":
        breed_or_name = request.form.get("breed_or_name")
        child_friendly = request.form.get("child_friendly")
        cat_friendly = request.form.get("cat_friendly")
        dog_friendly = request.form.get("dog_friendly")
        min_age = int(request.form.get("min_age", 0))
        max_age = int(request.form.get("max_age", 10))

        print("max age:", max_age)
        print("min age:", min_age)

        query = {}

        if breed_or_name:
            query["$or"] = [
                {"name": {"$regex": breed_or_name, "$options": "i"}},
                {"breed": {"$regex": breed_or_name, "$options": "i"}},
            ]

        if child_friendly == "on":
            query["canLiveWithChildren"] = "Yes"
        else:
            query["canLiveWithChildren"] = "No"

        if cat_friendly == "on":
            query["canLiveWithCats"] = "Yes"
        else:
            query["canLiveWithCats"] = "No"

        if dog_friendly == "on":
            query["canLiveWithDogs"] = "Yes"
        else:
            query["canLiveWithDogs"] = "No"

        if min_age != 0 and max_age != 10:
            min_age = int(min_age)
            max_age = int(max_age)

            min_birthdate = calculate_date_from_age(min_age)
            max_birthdate = calculate_date_from_age(max_age)

            print(max_birthdate)
            print(min_birthdate)

            query["dateOfBirth"] = {
                "$gte": max_birthdate,
                "$lte": min_birthdate
            }

        elif min_age != "0":
            # Only min_age is set
            min_age = int(min_age)
            min_birthdate = calculate_date_from_age(min_age)

            query["dateOfBirth"] = {
                "$lte": min_birthdate
            }
        elif max_age != "10":
            # Only max_age is set
            max_age = int(max_age)
            max_birthdate = calculate_date_from_age(max_age)

            query["dateOfBirth"] = {
                "$gte": max_birthdate
            }

        print(query)

        dogs = list(mongo.db.dogs.find(query))
        print(dogs)

        # Calculate age for each dog
        for dog in dogs:
            dob = dog.get('dateOfBirth')
            dog['age'] = calculate_dog_age(dob)

        return render_template("dogs.html", dogs=dogs)


@app.route('/dogs/<dog_id>')
def dog_details(dog_id):
    # Retrieve dog data from your database or any data source
    dog = mongo.db.dogs.find_one({'_id': ObjectId(dog_id)})
    return render_template('dog_details.html', dog=dog)


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


@app.route("/adoption_form/<dog_id>", methods=["GET", "POST"])
def adoption_form(dog_id):
    if request.method == 'POST':
        username = session.get('user')
        user = mongo.db.users.find_one({'username': username})

        if user:
            user_id = user['_id']

            existing_form = mongo.db.adoptionRequests.find_one(
                {'user_id': ObjectId(user_id), 'dog_id': ObjectId(dog_id)})

            if existing_form:
                flash("Error: You already have filled in this form for this dog!")
            else:
                adoption_info = {
                    'user_id': user_id,
                    'dog_id': ObjectId(dog_id),
                    'firstName': request.form.get('first_name').capitalize(),
                    'lastName': request.form.get('last_name').capitalize(),
                    'email': request.form.get('email').lower(),
                    'phone': request.form.get('phone'),
                    'addressLine': request.form.get('address_line1').capitalize(),
                    'city': request.form.get('city').capitalize(),
                    'county': request.form.get('county').capitalize(),
                    'postCode': request.form.get('post_code').upper(),
                    'whyThisDog': request.form.get('interested_dog'),
                    'experience': request.form.get('experience'),
                    'reason': request.form.get('reason'),
                    'otherDogsOption': request.form.get('other_dogs_option'),
                    'otherDogsDetails': request.form.get('other_dogs_details') if request.form.get('other_dogs_option') == 'yes' else None,
                    'otherCatsOption': request.form.get('other_cats_option'),
                    'otherCatsDetails': request.form.get('other_cats_details') if request.form.get('other_cats_option') == 'yes' else None,
                    'otherPetsOption': request.form.get('other_pets_option'),
                    'otherPetsDetails': request.form.get('other_pets_details') if request.form.get('other_pets_option') == 'yes' else None,
                    'children': request.form.get('children'),
                    'childrenDetails': request.form.get('children_details') if request.form.get('children') == 'yes' else None,
                    'workHours': request.form.get('work_hours'),
                    'exerciseHours': request.form.get('exercise_hours'),
                    'status': "Submitted"
                }

                # Insert the adoption form data into the MongoDB collection
                adoption_request = mongo.db.adoptionRequests.insert_one(
                    adoption_info)
                flash("Thank you, we have your form")

    dog = mongo.db.dogs.find_one({'_id': ObjectId(dog_id)})

    return render_template("adoption_form.html", dog=dog)


@app.route("/adoption_request/<request_id>", methods=["GET", "POST"])
def adoption_request_details(request_id):
    adoption_request = (mongo.db.adoptionRequests.find_one(
        {'_id': ObjectId(request_id)}))

    return render_template("adoption_request.html", adoption_request=adoption_request)


@app.route("/add_dog", methods=['POST', 'GET'])
def add_dog():
    if request.method == "POST":
        dob_str = request.form.get('dob')
        dob_date = datetime.strptime(dob_str, '%d/%m/%Y')

        existing_dog = mongo.db.dogs.find_one({
            'Name': request.form['name'],
            'Breed': request.form['breed'],
            'DateOfBirth': dob_date
        })

        if existing_dog:
            flash(
                "Error: Dog with the same name, breed, and date of birth already exists!")

        dog_info = {
            'name': request.form.get('name'),
            'breed': request.form.get('breed'),
            'dateOfBirth': dob_date,
            'gender': request.form.get('gender'),
            'size': request.form.get('size'),
            'description': request.form.get('description'),
            'canBeLeftAlone': request.form.get('left_alone'),
            'canLiveWithDogs': request.form.get('live_with_dogs'),
            'canLiveWithCats': request.form.get('live_with_cats'),
            'canLiveWithChildren': request.form.get('live_with_children'),
            'dailyExerciseRequired': request.form.get('exercise_required'),
            'imageURL': request.form.get('image_url')
        }

        dogs = mongo.db.dogs.insert_one(dog_info)
        flash("Dog Successfully Added")

    return render_template("add_dog.html")


@app.route("/admin_profile")
def admin_profile():
    return render_template("admin_profile.html")


@app.route("/edit_dog/<dog_id>", methods=["POST", "GET"])
def edit_dog(dog_id):
    dog = mongo.db.dogs.find_one({'_id': ObjectId(dog_id)})

    # Access dateOfBirth from the MongoDB document
    dob = dog.get('dateOfBirth')

    # Calculating the age using the utility function
    dog_age = calculate_dog_age(dob)

    # Format the date in the desired format
    formatted_dob = dob.strftime('%d/%m/%Y') if dob else None

    if request.method == "POST":
        dob_str = request.form.get('dob')
        dob_date = datetime.strptime(dob_str, '%d/%m/%Y')

        print(f"Updating dog with ID: {dog_id}")

        result = mongo.db.dogs.update_one(
            {'_id': ObjectId(dog_id)},
            {
                '$set': {
                    'name': request.form.get('name'),
                    'breed': request.form.get('breed'),
                    'dateOfBirth': dob_date,
                    'gender': request.form.get('gender'),
                    'size': request.form.get('size'),
                    'description': request.form.get('description'),
                    'canBeLeftAlone': request.form.get('left_alone'),
                    'canLiveWithDogs': request.form.get('live_with_dogs'),
                    'canLiveWithCats': request.form.get('live_with_cats'),
                    'canLiveWithChildren': request.form.get('live_with_children'),
                    'dailyExerciseRequired': request.form.get('exercise_required'),
                    'imageURL': request.form.get('image_url')
                }
            }
        )

        print(f"Modified count: {result.modified_count}")

        if result.modified_count > 0:
            flash('Dog listing updated successfully', 'success')
        else:
            flash('Failed to update dog listing', 'danger')

        return redirect(request.url)  # Redirect to the current URL

    return render_template("edit_dog.html", dog=dog, dog_age=dog_age, formatted_dob=formatted_dob)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    dogs = list(mongo.db.dogs.find(
        {"name": {"$regex": query, "$options": "i"}}))
    # Calculate age for each dog based on date of birth
    for dog in dogs:
        dob = dog.get('dateOfBirth')
        dog['age'] = calculate_dog_age(dob)

    display_results = True
    return render_template("admin_profile.html", dogs=dogs, display_results=display_results)


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Grab the user's information from the database
    user = mongo.db.users.find_one({"username": session["user"]})

    # Check if the user exists
    if not user:
        flash("User not found.")
        return redirect(url_for("home"))

    # Get the user's ID
    user_id = user['_id']

    # Query adoption requests for the user
    adoption_requests = list(mongo.db.adoptionRequests.find(
        {'user_id': ObjectId(user_id)}))

    for request in adoption_requests:
        dog_info = mongo.db.dogs.find_one({'_id': request['dog_id']})
        request['dog_info'] = dog_info

    return render_template("profile.html", user=user, adoption_requests=adoption_requests)


@app.route('/random_dog')
def random_dog():
    all_dogs = list(mongo.db.dogs.find())

    if not all_dogs:
        flash("No dogs found.")
        return redirect(url_for("home"))

    random_dog = random.choice(all_dogs)

    random_dog_id = str(random_dog['_id'])

    return redirect(url_for('dog_details', dog_id=random_dog_id))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(
        os.environ.get("PORT")), debug=True)
