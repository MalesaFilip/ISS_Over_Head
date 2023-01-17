import time

import requests
from datetime import datetime
import smtplib

MY_LAT = 52.229675
MY_LONG = 21.012230

my_email = "malespython@gmail.com"
password = "pjtxnsjaqxirgjsg"


# If the ISS is close to my current position
# Tworzymy funkcję, która będzie nam zwracać True, jeżeli pozycja ISS będzie wystarczająco bliska naszej
def is_close_enough():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    # Trzeba tu było konwertować na float, bo wyrażenie były stringami
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LAT + 5:
        return True


# Tworzymy funkcję, która będzie zwracać True, jeżeli obecnie jest noc
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    # Trzeba tu było konwertować na int, bo wyrażenie były stringami
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    # and it is currently dark
    if sunset + 1 < time_now < sunrise - 1:
        return True


# Then send me an email to tell me to look up.
if is_close_enough() and is_night():
    # BONUS: run the code every 60 seconds.
    time.sleep(60)
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="males77@yahoo.com",
                        msg="Subject:Look up!\n\nThe ISS is above you!")
