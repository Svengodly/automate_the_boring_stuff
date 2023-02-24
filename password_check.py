import re


def pass_check(name):
    # Check for spaces. The below line searches the string for spaces. Returns an empty list if there are no spaces.
    # Empty lists return a boolean value of False.
    # The boolean evaluation also checks the length is at least 8.
    # Made two different RegExes: One for lower and another for uppercase.

    lowerReg = re.compile("[a-z]+")
    upperReg = re.compile("[A-Z]+")
    numReg = re.compile("[0-9]+")

    if not re.findall(r'\s', name) and len(name) >= 8:
        if lowerReg.search(name) and upperReg.search(name) and numReg.search(name):
            print("Password created.")
            return True
        else:
            print("Missing Reqs:")
            if not lowerReg.search(name) or not upperReg.search(name):
                print("upper and lower")
            if not numReg.search(name):
                print("number")
            return False
    else:
        print("invalid")
        return False


def my_input():

    return input("Enter Pass: ")


while not pass_check(my_input()):
    pass_check(my_input())

