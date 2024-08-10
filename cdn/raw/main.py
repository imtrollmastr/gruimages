# main.py (GRU Graphics Panel)
# Made by Eddie Stockton (aka "imtrollmastr")

# Import required libraries
import os
import subprocess
import requests
import webbrowser
import base64
import getpass

# Check for security and internet connection
def check_internet_connection():
   try:
      subprocess.check_output(["ping", "-c", "1", "8.8.8.8"])
      return True
   except subprocess.CalledProcessError:
      return False
if check_internet_connection():
    r = requests.get('https://api.ipdata.co?api-key=b6c69cd24db05d3d56e2cb4e47a51bae7775bf82f63e70ec76ff23f6').json()
    countries = ['Abkhazia', 'Afghanistan', 'Åland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua & Barbuda', 'Argentina', 'Armenia', 'Artsakh', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia & Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Caribbean Netherlands', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos', 'Colombia', 'Comoros', 'Congo', 'Cook Islands', 'Costa Rica', 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czechia', 'Côte d’Ivoire', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Falkland Islands', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard & McDonald Islands', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao SAR China', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'North Korea', 'North Macedonia', 'Northern Cyprus', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territories', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn Islands', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Réunion', 'Sahrawi Arab Democratic Republic', 'Samoa', 'San Marino', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'Somaliland', 'South Africa', 'South Georgia & South Sandwich Islands', 'South Korea', 'South Ossetia', 'South Sudan', 'Spain', 'Sri Lanka', 'St. Barthélemy', 'St. Helena', 'St. Kitts & Nevis', 'St. Lucia', 'St. Martin', 'St. Pierre & Miquelon', 'St. Vincent & Grenadines', 'Sudan', 'Suriname', 'Svalbard & Jan Mayen', 'Sweden', 'Switzerland', 'Syria', 'São Tomé & Príncipe', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Transnistria', 'Trinidad & Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks & Caicos Islands', 'Tuvalu', 'U.S. Outlying Islands', 'U.S. Virgin Islands', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Wallis & Futuna', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']
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
    for country in countries:
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

# Show loaded message
print("GRU Graphics Panel has successfully loaded.")

# Start command entry panel
print("Welcome, " + getpass.getuser() + ".")
print("1) Convert .png to .gru")
print("2) Display .gru image")
print("3) Convert .gru to .png")
print("4) Join GRU Members")
print("5) Enter GRU Member ID")
print("6) View Rewards")

# Command function
def askForCommand():
    command = input("> ")
    if command == "1":
        # Run convert.py
        print("Enter file you want to convert:")
        inputFile = input("> ")
        print("Enter the output file name:")
        outputFile = input("> ")
        os.system("python3 resources/convert.py " + inputFile + " " + outputFile)
    elif command == "2":
        # Run render.py
        print("Enter .gru file that you want to render:")
        renderFile = input("> ")
        os.system("python3 resources/render.py " + renderFile)
    elif command == "3":
        # Show unsupported message
        print("We do not support decompiling yet.")
    elif command == "4":
        # Redirect to GRU Membership Registration
        print("Enter a username: ")
        command = input("> ")
        webbrowser.open_new_tab("https://grugraphics.vercel.app/profile?u=" + command)
    elif command == "5":
        # Decode GRU Membership ID
        print("Enter your GRU Member ID:")
        memberID = input("> ")
        memberID = str(base64.b64decode(memberID))
        memberID = memberID.split("b'")[1]
        memberID = memberID.split("'")[0]
        print("Welcome, " + memberID)
        print("Your membership has been validated.")
        print("Are you sure? Your current rewards will be erased. (y/n)")
        command = input("> ")
        # Create rewards file
        if command == "y":
            with open("resources/cache.txt", "wb") as rewards:
                rewards.write(bytes("0".encode('utf-8')))
                print("You may proceed to collect rewards.")
        else:
            print("Process aborted.")
    elif command == "6":
        try:
            # Find cache file and read
            with open("resources/cache.txt", "rb") as cache:
                reward_count = str(cache.read())
                reward_count = reward_count.split("b'")[1]
                reward_count = reward_count.split("'")[0]
                reward_count = int(reward_count)
                print("Rewards: " + str(reward_count))
        except:
            print("Join GRU Members to view your rewards!")
    elif command == "7":
        x = str(base64.b64encode(bytes(getpass.getuser().encode("utf-8"))))
        x = x.split("b'")[1]
        x = x.split("'")[0]
        print("Please email the following code to 'grustreaming@protonmail.com': " + x)
        import time
        print("Redirecting you to the livestream in 5 seconds...")
        time.sleep(1)
        print("Redirecting you to the livestream in 4 seconds...")
        time.sleep(1)
        print("Redirecting you to the livestream in 3 seconds...")
        time.sleep(1)
        print("Redirecting you to the livestream in 2 seconds...")
        time.sleep(1)
        print("Redirecting you to the livestream in 1 seconds...")
        time.sleep(1)
        webbrowser.open("https://grugraphics.vercel.app/stream/")

# Run command function
askForCommand()
