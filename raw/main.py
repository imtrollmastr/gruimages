import os
import sys
import base64

print("Welcome to GRU.")

# read configuration files
with open("config/username.config", "rb") as username_file:
    username = str(username_file.read())
    username = str.split(username, "b'")[1]
    username = str.split(username, "'")[0]

with open("config/password.config", "rb") as password_file:
    password = str(password_file.read())
    password = str.split(password, "b'")[1]
    password = str.split(password, "'")[0]
    password = base64.b64decode(password)
    password = str(password)
    password = str.split(password, "b'")[1]
    password = str.split(password, "'")[0]

print("Enter your password:")
command = input("> ")
if command == password:
    os.system("python3 home.py")
else:
    print("401 Unauthorized")