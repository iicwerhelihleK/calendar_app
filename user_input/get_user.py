import re

def check_email(email):
    """Checks if emila is valid.
    return: True if valid. False if invalid, username"""

    valid_characters = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    if not(re.search(valid_characters,email)):  
        print("Email Invalid")
        return False
    else:
        print("Email Valid")
        return True

def get_email():
    """Gets valid email address from user.
    return: email address, username"""

    email = input("Please enter valid email address: ")

    while not check_email(email):
        email = input("Please enter valid email address: ")

    return email, email.split('@')[0]

    # Used for prototyping
# print (get_email())
