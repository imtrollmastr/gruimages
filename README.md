# GRU Documentation
## About GRU
GRU is a image file extension that can store image data the same way as .png or .jpg files do. The system allows you to convert .png or .jpg files to .gru files. This is a more unique and secure way of storing image data by sending a person a .gru file as they require a special password that is configured by you.
## Installation
To install GRU Image Panel on your desktop, you will need to install the latest version of Python.
To install Python on your computer, enter the following command in your terminal/command prompt:

``
sudo apt install python3
``

You will then be required to install pip, a extension for installing additional packages.

``
sudo apt install python3-pip
``

After, you will need to install Git, in order to download GRU.

``
sudo apt install git
``

Then, proceed to download GRU.

``
git clone "https://github.com/imtrollmastr/gruimages.git"
``

You may be asked to install extension using pip. If so, please follow the commands below:

``
pip3 freeze > "requirements.txt"
``

``
pip3 install -r requirements.txt
``

Locate the GRU directory:

``
cd gruimages
``

Change the credentials of your account:

``
cd config
``

``
echo "YOUR_USERNAME_HERE" > username.config
``

``
echo "YOUR_PASSWORD_HERE" > password.config
``

``
cd ..
``

Encrypt your credentials:

``
python3 encrypt.py
``

Login and start your journey:

``
python3 main.py
``

## Usage
After installing the necessary extensions, proceed to enter your credentials. Once logged in, you will be asked to convert an image or display an image. 

### Steps for converting an image
Enter a .PNG or .JPG filename into the command line. It will ask you for an output name. That means the filename for the .gru file. A .gru file will appear in your directory and you may proceed to display it.

### Steps for displaying/rendering an image
Enter a .gru filename and a application should pop out showing the image converted to a .gru file.

## Developers
1. [imtrollmastr](https://github.com/imtrollmastr/)
