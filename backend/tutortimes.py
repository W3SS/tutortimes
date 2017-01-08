# imports
from users import *
from Course import *
import random
import string


class NoCourseError(Exception):
    """ An Error raised when no course is found"""
    pass


class TutorTimes:
    """ A class for the TutorTimes app """

    def __init__(self):
        """ (TutorTimes) -> NoneType
        Inits the TutorTimes App
        """
        # create empty lists
        self._users = []
        self._course_code_to_course = {}

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

    def add_course(self, admin, name):
        """(TutorTimes, Admin, str) -> NoneType
        Given an admin and the name of the course, generate a auth code for the course, and add
        it to the system.
        """
        # create an 5 letter auth code for the course
        course_code = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits)
                            for _ in range(5))

        # while the auth_code exists already in system
        while course_code in self._course_code_to_course:

            # generate a new auth code
            course_code = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits)
                                for _ in range(5))

        # create the course object
        new_course = Course(admin, self, name)

        # add the course to the dict
        self._course_code_to_course[course_code] = new_course

    def get_course(self, course_code):
        """(TutorTimes, str) -> Course
        Given a course code, return the Course that correspond to the course code stored
        in the system.
        RAISES: NoCourseError when a course cannot be found in the dict
        """
        if course_code in self._course_code_to_course:
            course = self._course_code_to_course[course_code]
        else:
            raise NoCourseError("There is no such course")

        # return the course
        return course
