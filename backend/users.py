from werkzeug.security import generate_password_hash, \
     check_password_hash


class User():
    """ A class representing users in the system"""

    def __init__(self, username, password):
        """ (User, str, str) -> NoneType
        Inits the user with username and password.
        """
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        """ (User, str) -> str
        Given a password, hash the password """
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        """ (User, str) -> bool
        Given a password, check with the password hash of the user and see if
        it matches
        """
        return check_password_hash(self.pw_hash, password)