from werkzeug.security import generate_password_hash, \
     check_password_hash
from Course import *


class User:
    """ A class representing users in the system"""

    def __init__(self, name, email, password, user_type):
        """ (User, str, str, str, str) -> NoneType
        Inits the user given name, email, password and user type.
        """
        self._name = name
        self._email = email
        self._pw_hash = None
        self.set_password(password)

    def __str__(self):
        """ (Users) -> str
        Returns the email of the user
        """
        return self._email

    def get_name(self):
        """ (User) -> str
        Returns the full name of the user
        """
        return self._name

    def set_password(self, password):
        """ (User, str) -> str
        Given a password, hash the password """
        self._pw_hash = generate_password_hash(password)

    def check_password(self, password):
        """ (User, str) -> bool
        Given a password, check with the password hash of the user and see if
        it matches.
        """
        return check_password_hash(self._pw_hash, password)

    def get_email(self):
        """ (User) -> str
        Returns the email of the user
        """
        return self._email


class Student:
    """ A class for Student permissions for a user"""
    def __init__(self):
        """ (Student) -> NoneType

        """
        # set of courses that the Student is enrolled in, as Course objects
        self._courses = set()

    def enroll_course(self, Course):
        '''(Student, Course) -> NoneType
        Enrolls the student into the course specified.

        '''

        # if the Student is already enrolled in the course,
        # don't let them enroll again
        if Course not in self._courses:

            # add course to Student's enrolled courses
            self._courses.update(Course)

            # add Student into that Course
            Course.add_student(self)

    def drop_course(self, Course):
        '''(Student, Course) -> NoneType
        Unenrolls the student from the course specified.

        '''
        # Students can only drop courses they are enrolled in
        if Course in self._courses:

            # remove the Course from Student's list of enrolled courses
            self._courses.remove(Course)

            # remove Student from that Course
            Course.remove_student(self)

    def get_courses(self):
        '''(None) -> list of Courses
        Returns the courses the Student is enrolled in as a list.

        '''
        course_list = []

        for Course in self._courses:
            course_list.append(Course)

        return course_list

    def get_course(self, Course):
        '''(Student, Course) -> set of Events
        Returns all the Events (ie. office hours) for the specified Course.

        '''
        event_list = Course.get_events()

        return event_list


class Admin:

    def __init__(self, name):

        # list of Events this Admin has created
        self._events = set()

        # list of Courses this Admin is part of
        self._courses = set()

        # name of the Admin (that will appear on the timetable)
        self._name = name

    def get_courses(self):
        '''(Admin) -> list of str
        Returns list of all courses the Admin is part of.

        '''
        course_list = self._courses

        return course_list

    def add_course_event(self, Course, start_time, end_time, room):
        '''(Admin, Course, int, int, str) -> NoneType
        Creates an Event for the specified course at the specified time. Start
        time and end time are in milliseconds (Unix time).
        '''
        # name of Admin
        name = self._name

        # create new Event object
        New_Event = Event(start_time, end_time, room, name)

        # add the Event to the Course
        Course.add_event(New_Event)

    def remove_course_event(self, Event):
        '''(Admin, Event) -> NoneType
        Deletes the Event (ie. cancelling an office hour).

        '''

        Course.remove_event()
