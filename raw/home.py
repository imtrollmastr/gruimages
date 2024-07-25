print("GRU image panel has successfully loaded.")

import os
import sys
import base64

with open("config/username.config", "rb") as username_file:
    username = str(username_file.read())
    username = str.split(username, "b'")[1]
    username = str.split(username, "'")[0]
print("Welcome, " + username + ".")
print("1) Convert .png to .gru")
print("2) Display .gru image")
def askForCommand():
    command = input("> ")
    if command == "1":
        print("Enter file you want to convert:")
        inputFile = input("> ")
        print("Enter output filename:")
        outputFile = input("> ")
        os.system("python3 resources/convert.py " + inputFile + " " + outputFile)
    elif command == "2":
        print("Enter .gru file that you want to render:")
        renderFile = input("> ")
        os.system("python3 resources/render.py " + renderFile)
    else:
        askForCommand()

askForCommand()