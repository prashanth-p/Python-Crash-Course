import sys
print(sys.version)


class Users():

    def __init__(self, first_names, last_names):
        self.first_names = first_names
        self.last_names = last_names
        self.login_attempts = 0

    def describe_users(self):
        print('The name of the user is ' + self.first_names.title() + " " +
              self.last_names.title())

    def greet_users(self):
        print("Hello", self.first_names.title(), self.last_names.title(),
              " Have a nice day")

    def inc_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


if __name__ == '__main__':
    sam = Users("samridh", "saluja")
    prashanth = Users("prashanth", "pradeep")
    jayashree = Users("jayashree", "pradeep")

    sam.describe_users()
    sam.greet_users()
    sam.inc_login_attempts()
    sam.inc_login_attempts()
    print(sam.login_attempts)
    sam.reset_login_attempts()
    print(sam.login_attempts)

"""
    prashanth.describe_users()
    prashanth.greet_users()
    print()

    jayashree.describe_users()
    jayashree.greet_users()
    print()
"""
