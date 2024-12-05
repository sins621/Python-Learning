from datetime import datetime
from dateutil.relativedelta import relativedelta
import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

current_date = datetime.now()
current_date_only = current_date.date()

date_in_6_months = current_date_only + relativedelta(months=6)

AMADEUS_KEY = os.getenv("AMADEUS_KEY")
AMADEUS_SECRET = os.getenv("AMADEUS_SECRET")
AMADEUS_TOKEN = os.getenv("AMADEUS_TOKEN")
PATH = "./Day 39/Flight Notifier"

amadeus_city_get = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
amadeus_flight_offer_get = "https://test.api.amadeus.com/v2/shopping/flight-offers"


class FlightData:
    def __init__(self):
        self.token = self.get_access_token()

    def get_access_token(self):
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        body = {
            "grant_type": "client_credentials",
            "client_id": AMADEUS_KEY,
            "client_secret": AMADEUS_SECRET,
        }
        try:
            response = requests.post(url, headers=headers, data=body)
            response.raise_for_status()
            return response.json()["access_token"]
        except requests.exceptions.RequestException as err:
            print(f"Error fetching access token: {err}")
            return None

    def get_city_info(self, city):
        if not self.token:
            print("No valid token available.")
            return None

        body = {"keyword": city, "max": 1}
        headers = {"Authorization": f"Bearer {self.token}"}
        try:
            city_get = requests.get(url=amadeus_city_get, headers=headers, params=body)
            city_get.raise_for_status()
            city_data = city_get.json()["data"][0]
            return city_data
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.RequestException as err:
            print(f"Request Error: {err}")

    def get_test_city_info(self):
        try:
            with open(f"{PATH}/city_get.json", "r") as test_file:
                test_data = json.load(test_file)
            return test_data
        except FileNotFoundError as errf:
            print(f"File Not Found, Error: {errf}")
            return None

    def get_flight_deal(self, origin_iata, destination_iata, max_price):
        if not self.token:
            print("No valid token available.")
            return None

        body = {
            "originLocationCode": origin_iata,
            "destinationLocationCode": destination_iata,
            "departureDate": current_date_only,
            "returnDate": date_in_6_months,
            "adults": 1,
            "currencyCode": "EUR",
            "maxPrice": max_price,
        }
        headers = {"Authorization": f"Bearer {self.token}"}
        try:
            response = requests.get(
                url=amadeus_flight_offer_get, headers=headers, params=body
            )
            response.raise_for_status()
            flight_deal_data = response.json()
            return flight_deal_data
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
            return None
        except requests.exceptions.RequestException as err:
            print(f"Request Error: {err}")
            return None
