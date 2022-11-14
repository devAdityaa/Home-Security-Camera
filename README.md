# Home-Security-Camera
![alt text](https://github.com/DennisNewton/Home-Security-Camera/blob/main/Preview.png)


This Uses Python 3.10 as its main development language and uses the following dependencies: OpenCV, Twilio REST API. This project is a miniature version of a home security camera that detects any human faces and sends alerts to your mobile phone which might catch a potential intruder and stop a burglary.

# For Further Development
If you want to add new features or want to use it for testing then this is what you need. First install the dependencies using terminal of your PC (neglect if already installed) :

**Note**
As all of the code is done in  Python primarily, it is supposed that you already have an upgraded version of python and pip. If not then refer the link below to install them :
### Install PIP 
> https://pip.pypa.io/en/stable/installation/
### Install Python
> refer to google based on your desktop environment (Windows, Linux,etc.)
### OpenCV Library
> _pip install cv2_
### Twilio API
> _pip install twilio_

## authKeys.py
You must have a twilio account (free or paid) to avail the alert feature whenever a face gets detected (updated every 60s).
From your twiio account dashboard, copy and paste your account sid,tolken and twilio-provided number in the authKeys.py file. The input areas are marked with _* (asterix)_

Then run the main file and your own alert system will send you a message if a face gets detected in your webcam within 60s.

# Updating The Alert Message or Update time
> To change the alert message refer to the comment at line 42 of the main.py file

> To change the update time refer to the comment at line 36 of main.py file
