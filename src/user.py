# user.py

class User:
    def __init__(self, username, password, age):
        self.username = username
        self._password = password  # _password is used to indicate that it is "private" (convention)
        self.age = age
        self.logged_in = False

    def show_password(self):
        return self._password  # This is to reveal the password if needed

    def login(self, password):
        if self._password == password:
            self.logged_in = True
        else:
            raise ValueError("Incorrect password.")

    def logout(self):
        self.logged_in = False
