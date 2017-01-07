from werkzeug.security import generate_password_hash, \
     check_password_hash


class User:
    """ A class representing users in the system"""

    def __init__(self, name, email, password, user_type):
        """ (User, str, str, str, str) -> NoneType
        Inits the user given name, email, password and user type.
        """
        self._name = name
        self._email = email
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
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        """ (User, str) -> bool
        Given a password, check with the password hash of the user and see if
        it matches.
        """
        return check_password_hash(self.pw_hash, password)

    def get_email(self):
        """ (User) -> str
        Returns the email of the user
        """
        return self._email


class Student:
    """ A class for Student permissions for a user"""
    def __init__(self, course):
        """ (Student, Course) -> NoneType
        Given a course, assign the course to the student
        """

        # store the course that the student is part of


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
        Drops the student from the course specified.

        '''
        # Students can only drop courses they are enrolled in
        if Course in self._courses:

            # remove the Course from Student's list of enrolled courses
            self._courses.remove(Course)

            # remove Student from that Course
            Course.remove_student(self)

    def get_courses():
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
        pass
