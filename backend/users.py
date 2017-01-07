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
        it matches
        """
        return check_password_hash(self.pw_hash, password)

    def get_email(self):
        """ (User) -> str
        Returns the email of the user
        """
        return self._email
