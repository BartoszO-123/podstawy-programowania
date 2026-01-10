import re

username = input("Enter username: ")
password = input("Enter password: ")

# [a-z] - małe litery, {6,} - co najmniej 6 znaków
username_pattern = r"^[a-z]{6,}$"

# [A-Za-z0-9_] - litery, cyfry i podkreślenie, {8,} - co najmniej 8 znaków
password_pattern = r"^[A-Za-z0-9_]{8,}$"

username_match = re.match(username_pattern, username)
password_match = re.match(password_pattern, password)

if username_match and password_match:
    print("Username and password are valid!")
else:
    print("Username or password does not meet the requirements.")
