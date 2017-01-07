# imports
from users import *


class TutorTimes:
    """ A class for the TutorTimes app """

    def __init__(self):
        """ (TutorTimes) -> NoneType
        Inits the TutorTimes App
        """
        # create empty lists
        self._users = []
        self._courses = []

    def add_user(self, user):
        """ (TutorTimes, User) -> NoneType
        Given a user, add it to the list of students or admin
        """
        self._users.append(user)

    def is_registered(self, email):
        """ (TutorTimes, str) -> bool
        Given an email, returns True of email is associated with user object in
        system, False otherwise
        """
        if email in self._users:
            result = True
        else:
            result = False

        # return the result
        return result

    def get_user(self, email):
        """ (TutorTimes, str) -> User
        Given an email, return the user object that is associated with that email

        REQ: self.is_registered(email)
        """
        for user in self._users:
            if email == user.get_email():
                return user

    def add_course(self, course):
        """(TutorTimes, Course) -> NoneType
        Given a course, add it to the list of courses
        """
        self._courses.append(course)
