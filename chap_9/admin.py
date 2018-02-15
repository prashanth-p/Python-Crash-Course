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


class Admin(Users):

    def __init__(self, first_names, last_names, privilages):
        super().__init__(first_names, last_names)
        self.privilages = privilages

    def show_privilages(self):
        print("The privilages the admin has are:")
        print(self.privilages)


if __name__ == '__main__':
    privilages = []
    print("Enter the Different admin privilages:")
    print("Enter Done to quit")
    while True:
        buff = input()
        if buff == "done":
            break
        privilages.append(buff)

    print()

    newAdmin = Admin("Harsh", "Tripathi", privilages)
    newAdmin.describe_users()
    newAdmin.greet_users()
    newAdmin.inc_login_attempts()
    newAdmin.inc_login_attempts()
    print(newAdmin.login_attempts)
    newAdmin.reset_login_attempts()
    print(newAdmin.login_attempts)
    print()
    newAdmin.show_privilages()
