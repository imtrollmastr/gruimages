import subprocess
import requests
def check_internet_connection():
   try:
      subprocess.check_output(["ping", "-c", "1", "8.8.8.8"])
      return True
   except subprocess.CalledProcessError:
      return False
if check_internet_connection():
    r = requests.get('https://api.ipdata.co?api-key=b6c69cd24db05d3d56e2cb4e47a51bae7775bf82f63e70ec76ff23f6').json()
    supported_countries = ["Albania", "Algeria", "Afghanistan", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada","Chad", "Chile", "Colombia", "Comoros", "Costa Rica", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Holy See (Vatican City)", "Hong Kong", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Suriname", "Sweden", "Switzerland", "Sudan", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]
    ip_address = r["ip"]
    supported = False
    v = requests.get("https://vpnapi.io/api/" + ip_address +"?key=d289659c2571426dbf1cd17f2841647b").json()
    if v["security"]["vpn"] == True or v["security"]["proxy"] == True or v["security"]["tor"] == True or v["security"]["relay"] == True:
        print("VPN/Proxy/Tor/iCloud Relay detected, please disable it and try again.")
        print("Advanced: override warning? (y/n)")
        c = input("> ")
        if c == "y":
            print("Please expect some bugs and issues when running on a VPN or proxy.")
            pass
        else:
            exit()
    for country in supported_countries:
        if r['country_name'] == country:
            supported = True
        else:
            if supported == True:
                supported = True
            else:
                supported = False

    if supported == True:
        pass
    elif supported == False:
        print("Country, region, or territory not supported.")
        exit()
else:
   print("Internet is not connected.")

print("GRU Graphics Panel has successfully loaded.")

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
print("3) Convert .gru to .png")
def askForCommand():
    command = input("> ")
    if command == "1":
        print("Enter file you want to convert:")
        inputFile = input("> ")
        print("Enter the output file name:")
        outputFile = input("> ")
        os.system("python3 resources/convert.py " + inputFile + " " + outputFile)
    elif command == "2":
        print("Enter .gru file that you want to render:")
        renderFile = input("> ")
        os.system("python3 resources/render.py " + renderFile)
    elif command == "3":
        print("We do not support decompiling yet.")
    else:
        askForCommand()

askForCommand()