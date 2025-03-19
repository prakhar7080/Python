# # A website requires the users to input username and password to register. Construct a program to check the validity of password input by users. Following are the criteria for checking the password.credits

# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 3. At least 1 letter between [A-Z]
# 4. At least 1 character from [$#@]
# Minimum length of transaction password : 6
# Maximum length of transaction password: 12
# Your program should accept a sequence of comma seperated passwords and will check them according to the above criteria. Passwords the match the criteria are to be printed, each seperated by a comma.
import re
def is_valid_pass(passw):
    if (6<= len(passw) <=12 and re.search(r'[a-z]',passw) and re.search(r'[A-Z]',passw) and re.search(r'[0-9]',passw) and re.search(r'[@#$]',passw)):
        return True
    return False


def check_password(password):
    password_lst = password.split(",")
    valid = [passw for passw in password_lst if is_valid_pass(passw)]
    return ",".join(valid)

password = input("Enter comma seperated passwords = ")

valid_passwords = check_password(password)
print(valid_passwords)