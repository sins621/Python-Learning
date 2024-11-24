import requests
import smtplib
from datetime import datetime
from math import isclose
from time import sleep

with open("./Keys/keys.txt") as keys:
    sender_mail = keys.readline().strip()
    sender_key = keys.readline().strip()

# print(isclose(1,-7, abs_tol = 5))

MY_LAT = 23.6107 # Your latitude
MY_LONG = -91.5275  # Your longitude
MY_LAT_LNG = (MY_LAT, MY_LONG)


def check_iss_lat_lng():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return (iss_latitude, iss_longitude)


# Your position is within +5 or -5 degrees of the ISS position.
def is_close_to_iss(your_lat_lng, iss_lat_lng):
    return isclose(your_lat_lng[0], iss_lat_lng[0], abs_tol=5) and isclose(
        your_lat_lng[1], iss_lat_lng[1], abs_tol=5
    )


def is_dark(time_hour, sunrise_sunset):
    return time_hour < sunrise_sunset[0] or time_hour > sunrise_sunset[1]


def check_sunrise_sunset():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    return (sunrise, sunset)


def send_mail():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender_mail, password=sender_key)
        connection.sendmail(
            from_addr=sender_mail,
            to_addrs="bradlycarpenterza@gmail.com",
            msg=f"Subject:ISS Overhead\n\nLook above, you may be able to see the ISS!",
        )


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

time_now = datetime.now()
hour_now = time_now.hour
sunrise_sunset = check_sunrise_sunset()

while True:
    if is_close_to_iss(MY_LAT_LNG, check_iss_lat_lng()) and is_dark(
        hour_now, sunrise_sunset
    ):
        print("Sending Mail")
        send_mail()
    else:
        print("Either not dark or the ISS is too far away")
    sleep(60)

# # If the ISS is close to my current position
# # and it is currently dark
# # Then send me an email to tell me to look up.
# # BONUS: run the code every 60 seconds.
