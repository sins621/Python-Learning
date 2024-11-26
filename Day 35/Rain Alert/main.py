import json
import requests
from twilio.rest import Client


KEY_PATH = "./Keys/keys.json"
PROJECT_PATH = "./Day 35/Rain Alert"
CPT_LATLON = (-33.918861, 18.423300)

with open(KEY_PATH, "r") as file:
    api_keys = json.load(file)

account_sid = api_keys["twilio"]["sid"]
auth_token = api_keys["twilio"]["auth_token"]

parameters = {
    "lat": CPT_LATLON[0],
    "lon": CPT_LATLON[1],
    "appid": api_keys["openweathermap"],
    "cnt": 4,
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast", params=parameters
)

response.raise_for_status()
weather_data = response.json()
forecast_ids = [id["weather"][0]["id"] for id in weather_data["list"]]

will_rain = False

for id in forecast_ids:
    if id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="+17753682906", body="It will rain today.", to="+27765261782"
    )
    print(message.status)
