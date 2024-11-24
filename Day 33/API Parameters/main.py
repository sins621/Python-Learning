import requests

LAT = -33.962864
LNG = 18.409834

parameters = {"lat": LAT, "lng": LNG, "formatted":0}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise, sunset)
