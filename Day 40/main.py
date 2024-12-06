import requests
import os

from dotenv import load_dotenv

load_dotenv()


class AmadeusHandler:
    def __init__(self):
        key = os.getenv("AMADEUS_KEY")
        secret = os.getenv("AMADEUS_SECRET")
        self.token = self.get_access_token(key, secret)

    def get_access_token(self, key, secret):
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        body = {
            "grant_type": "client_credentials",
            "client_id": key,
            "client_secret": secret,
        }
        print("Attempting to fetch Amadeus Access Token")
        try:
            response = requests.post(url, headers=headers, data=body)
            response.raise_for_status()
            print("Attempt to fetch Amadeus Access Token successful")
            return response.json()["access_token"]
        except requests.exceptions.RequestException as err:
            print(f"Error fetching access token: {err}")
            return None


class SheetyHandler:
    def __init__(self):
        auth = os.getenv("SHEETY_AUTH")
        self.sheety_headers = {"Authorization": f"Bearer {auth}"}
        self.flight_data = self.get_flight_data()

    def get_flight_data(self):
        flight_data_endpoint = (
            "https://api.sheety.co/bc2d347620e0173a47d425cfc87639fd/flightDeals/prices"
        )
        print("Attempting to get flight data")
        try:
            flight_data_response = requests.get(
                url=flight_data_endpoint, headers=self.sheety_headers
            )
            flight_data_response.raise_for_status()
            print(f"Attempt to access flight data successful")
            return flight_data_response.json()
        except requests.exceptions.RequestException as err:
            print(f"Attempt to access flight data unsuccessful, error {err}")
            return None
