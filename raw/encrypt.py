import os
import sys
import base64

with open("config/password.config", "rb") as password_file:
    encrypted_password = str(base64.b64encode(password_file.read()))
    encrypted_password = str.split(encrypted_password, "b'")[1]
    encrypted_password = str.split(encrypted_password, "'")[0]
    print(encrypted_password)

with open("config/password.config", "wb") as password_file:
    password_file.write(bytes(encrypted_password.encode('utf-8')))