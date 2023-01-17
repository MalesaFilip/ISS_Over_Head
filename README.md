# ISS_Over_Head
Checks if the ISS is currently above us

This program allows you to track the ISS, basically any satellite that interests us and inform us when it is near us.
The idea is to look up on the sky and try to find it, that's why the program is going to send us notofications only during night.
Now it's following the ISS but you can follow any satellity if it has an API, you can replace API of ISS on any other one.

<h1> Prerequisites </h1>
You will need Pycharm to run the program [PyCharm](https://www.jetbrains.com/help/pycharm/installation-guide.html).

<h2>Installing</h2>
After that, open file `main.py`.

```
import time
import requests
from datetime import datetime
import smtplib
```

You need to intstall only `requests`, because the rest is already built into python.
[Reqests instalation](https://www.geeksforgeeks.org/how-to-install-requests-in-python-for-windows-linux-mac/)

<h2>Usage</h2>

```
MY_LAT = "Your latitude as float"
MY_LONG = "Your longitude as float"
```
Replace that two strings by yours latitude and longitude

```
my_email = "Your Email as a string"
password = "Your Email password as string"
```
Add your Email and password of email, from which you want to send the message

>response = requests.get(url="http://api.open-notify.org/iss-now.json")
If you want to check other satelite, just replace thah API with other one and remember to change this values also
```
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
```
If you are using other email than Gmail, remember to change domain.
[SMTPLIB Documentation](https://docs.python.org/3/library/smtplib.html)
```
connection = smtplib.SMTP("smtp.gmail.com")
```


You must also add the e-mail address to which the message should be sent
```
to_addrs="Mail to send notification as string"
```

<h2>Working</h2>
After hit Run, you wont see any final code that it's done, it's going to run all the time untill you stop it. 
Every 60 seconds it will check if the satellite is in the area, if it meets its condition, then it will send a message
