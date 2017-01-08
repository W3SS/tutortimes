# imports
from flask import Flask, request, session, redirect, url_for, escape, jsonify
from users import *
import tutortimes


# initializes the flask app
app = Flask(__name__)
app.secret_key = 'HACKVALLEY2017FDU*AUHFDAOIJDA^*&(.'

# create a tutortimes object
server = tutortimes.TutorTimes()

# create a new admin
root = Admin("Brian Harrington")

# Testing code

# create a new course in tutortimes
course_code = server.add_course(root, "CSCA08 - Introduction to Computer Science")
# get the course code
print(course_code)


# end testing code

@app.route("/")
def home():
    """() -> str
    The main page for Tutor Times
    """
    return "Welcome to Tutor Times"


@app.route("/api")
def api():
    """() -> str
    API Page
    """
    return "Tutor Times API"


@app.route("/api/register", methods=['POST'])
def register():
    """() -> json
    Creates a new user
    """
    json_data = request.json

    # get fields from form
    email = json_data['email']
    name = json_data['name']
    password = json_data['password']
    user_type = json_data['user_type']

    # if the user email is not registered yet
    if server.get_user(email) is None:

        # create a new user object
        new_user = User(name, email, password, user_type)

        # add the user to TutorTimes
        server.add_user(new_user)

        status = "success"

    # else do not allow them to register
    else:
        status = "User email already exists in database"

    # returns the success message
    return jsonify({'result': status})


@app.route("/api/login", methods=['POST'])
def login():
    """() -> json
    Logs in a user by giving them a session
    """

    json_data = request.json

    # check if it is a post method
    if request.method == "POST":

        # get the email in the field
        email = json_data['email']

        # get the password in the field
        password = json_data['password']

        # CASE 1: User is registered
        if server.get_user(email) is not None:

            # obtain their user object
            login_user = server.get_user(email)

            # If password matches
            if login_user.check_password(password):

                # Initiate a session for them
                # initiate a session
                session['email'] = email
                status = True

            # If password does not match
            else:
                status = False
                print("Passwords do not match")

        # CASE 2: User is not registered
        else:
            status = False
            print("User is not registered")

    # return json of result
    return jsonify({'result': status})


@app.route('/api/notify')
def notify():
    """() -> json
    Notifies users by push notifications
    """
    pass


@app.route('/api/new_course', methods=['POST'])
def new_course():
    """() -> json
    Creates a new course iff user is logged in
    """

    # check if user is in session
    if 'email' in session:

        # get the admin that is creating the course
        admin = server.get_user(escape(session['email']))

        # get the course name from json
        json_data = request.json
        course_name = json_data['course_name']

        email_session = escape(session['email'])
        print(email_session)

        # get the admin that is creating the course
        admin_user = server.get_user(email_session)

        # create a new admin object for that user
        admin = Admin(admin_user.get_name())

        # create the course from the system, and get the course code
        course_code = server.add_course(admin, course_name)

    else:
        course_code = "ERROR"

    # return the json of the course code
    return jsonify({'course_code': course_code})


@app.route('/api/course/<coursecode>', methods=['POST', 'GET'])
def view_course(coursecode):
    """ (str) -> json
    Get all the details of a course with json
    """
    # load the course from the system
    requested_course = server.get_course(coursecode)

    # get the information of the course
    course_name = requested_course.get_name()
    tutor_events = list(requested_course.get_TutorEvents())
    instructors = requested_course.get_admins()

    # return the tutor events as json
    return jsonify({'name': course_name,
                    'instructors': instructors,
                    'events': tutor_events})


@app.route('/api/logout')
def logout():
    """() -> json
    Logs out the user and removes them from the session
    """
    session.pop('logged_in', None)

    # return the json of the result
    return jsonify({'result': 'success'})


if __name__ == "__main__":
    app.run()