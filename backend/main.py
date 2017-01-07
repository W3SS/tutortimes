from flask import Flask, request, session, redirect, url_for, escape
from users import *
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
def new_user():
    """() -> str
    Creates a new user
    """

    # get username and password from the form
    username = request.form['username']

    # TODO: encrypt password
    password = request.form['password']

    # create a new user object


    # returns the success message
    return "User is now registered as {}".format(username)


@app.route("/login", methods=['POST'])
def login():
    """() -> redirect
    Logs in a user to the system
    """
    # check if it is a post method
    if request.method == "POST":

        # get the username in the field
        username = request.form['username']

        # get the password in the field
        password = request.form['password']


        # if the password matches the one in the database

        # initiate a session
        session['username'] = username

    # redirect them back to home
    # TODO: make this redirect somewhere else
    return redirect(url_for('home'))


@app.route("/logout")
def logout():
    """Logs out the user and removes them from the session"""
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run()