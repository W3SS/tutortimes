# imports
from flask import Flask, request, session, redirect, url_for, escape, jsonify
from users import *
import tutortimes


# initializes the flask app
app = Flask(__name__)
app.secret_key = 'HACKVALLEY2017FDU*AUHFDAOIJDA^*&(.'


@app.route("/")
def home():
    """() -> str
    Return whether or not they are logged in or not.

    """
    # if the person is in the session, then show they are logged in
    if 'username' in session:
        msg = "You are logged in as {}".format(escape(session['username']))
    # if the person is not logged in, show they are not logged in
    else:
        msg = "You are not logged in yet."

    # return the msg
    return msg

@app.route("/register", methods=['POST'])
def register():
    """() -> str
    Creates a new user
    """

    # get fields from form
    email = request.form['email']
    name = request.form['name']
    password = request.form['password']
    user_type = request.form['user_type']

    # create a new user object
    new_user = User(name, email, password, user_type)

    # add the user to TutorTimes
    tutortimes.add_user(new_user)

    # returns the success message
    return jsonify("User is now registered as {}".format(email))


@app.route("/login", methods=['POST'])
def login():
    """() -> NoneType
    Logs in a user by giving them a session
    """
    # check if it is a post method
    if request.method == "POST":

        # get the email in the field
        email = request.form['email']


        # get the password in the field
        password = request.form['password']


        # CASE 1: User is registered
        if tutortimes.is_registered(email):

            # obtain their user object
            login_user = tutortimes.get_user(email)

            # If password matches
            if password == login_user.check_password(password):

                # Initiate a session for them
                # initiate a session
                session['email'] = email

            # If password does not match
            else:

                # do something
                print("passwords do not match")

        # CASE 2: User is not registered
        else:

            # redirect them
            print("user does not exist in database")

    # return redirect(url_for('home'))


@app.route("/logout")
def logout():
    """Logs out the user and removes them from the session"""
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run()