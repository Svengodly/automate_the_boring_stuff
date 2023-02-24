# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class User:
    def __init__(self, first_name, last_name, country, birth_month):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.birth_month = birth_month
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} was born in {self.country.title()}. They were born "
              f"in the month of {self.birth_month.title()}")

    def greet_user(self):
        print(f"Hello {self.first_name.title()}! I hope that all is well.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, country, birth_month):
        super().__init__(first_name, last_name, country, birth_month)
        self.rights = Privileges()


class Privileges:
    def __init__(self, privileges=['read', 'write', 'execute']):
        self.privileges = privileges

    def show_privileges(self):
        print(f"Your privileges are: ")
        for right in self.privileges:
            print(right)


# Press
# the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    user_1 = Admin('jack', 'johnson', 'usa', 'sept')
    user_1.rights.show_privileges()
    x = '1143'
    for value in x:
        print(value)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
