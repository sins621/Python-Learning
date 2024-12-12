import datetime
import json
import os
import smtplib

import requests
from dotenv import load_dotenv

load_dotenv()


class Mail:
    def __init__(self):
        self.my_email = "fl0586114@gmail.com"
        self.my_password = os.getenv("MAIL")

    def send_mail(self, message, to_address):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.my_password)
            connection.sendmail(
                from_addr=self.my_email,
                to_addrs=to_address,
                msg=message,
            )
            print(f"Sending Flight Offer Mail to {to_address}")


class AmadeusHandler:
    def __init__(self):
        amadeus_key = os.getenv("AMADEUS_KEY")
        amadeus_secret = os.getenv("AMADEUS_SECRET")
        self.amadeus_token = self.get_access_token(amadeus_key, amadeus_secret)

    def get_access_token(self, key, secret):
        access_token_query_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        access_token_query_headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        access_token_query_body = {
            "grant_type": "client_credentials",
            "client_id": key,
            "client_secret": secret,
        }
        print("Attempting to fetch Amadeus Access Token")
        try:
            access_token_query_response = requests.post(
                url=access_token_query_url,
                headers=access_token_query_headers,
                data=access_token_query_body,
            )
            access_token_query_response.raise_for_status()
            print("Attempt to fetch Amadeus Access Token successful")
            return access_token_query_response.json()["access_token"]
        except requests.exceptions.RequestException as err:
            print(f"Error fetching access token: {err}")
            return None

    def get_flight_offers(self, **flight_details):
        flight_offer_query_endpoint = (
            "https://test.api.amadeus.com/v1/shopping/flight-dates"
        )

        flight_offer_query_body = {
            "origin": flight_details.get("origin"),
            "destination": flight_details.get("destination"),
            "departureDate": flight_details.get("departure_date"),
            "maxPrice": flight_details.get("max_price"),
            "duration": "1,180",
            "oneWay": False,
            # "nonStop": True,
            "viewBy": "WEEK",
        }

        flight_offer_query_headers = {"Authorization": f"Bearer {self.amadeus_token}"}

        print(f"Attempting to access {flight_offer_query_endpoint}")
        try:
            flight_offer_query_response = requests.get(
                url=flight_offer_query_endpoint,
                params=flight_offer_query_body,
                headers=flight_offer_query_headers,
            )
            flight_offer_query_response.raise_for_status()
            print(f"Attempt to access {flight_offer_query_endpoint} successful")
        except requests.exceptions.RequestException as err:
            if hasattr(err.response, "text"):
                print(f"Error details: {err.response.text}")
            print(
                f"Attempt to access {flight_offer_query_endpoint} unsuccessful, error: {err}"
            )
        else:
            flight_offer_data = flight_offer_query_response.json()
            flight_offers = []
            for flight in flight_offer_data["data"]:
                offer = {
                    "origin": flight["origin"],
                    "destination": flight["destination"],
                    "departure_date": flight["departureDate"],
                    "return_date": flight["returnDate"],
                    "price": flight["price"]["total"],
                }
                flight_offers.append(offer)
            return flight_offers

    def calculate_lowest_price(self, data):
        flights = data["data"]
        lowest_price = flights[0]["price"]["total"]
        for flight in flights:
            flight_price = flight["price"]["total"]
            if flight_price < lowest_price:
                lowest_price = flight_price
        return lowest_price


class SheetyHandler:
    def __init__(self):
        sheety_auth = os.getenv("SHEETY_AUTH")
        self.sheety_headers = {"Authorization": f"Bearer {sheety_auth}"}

    def get_city_data(self):
        return self.get_sheet_data(
            "https://api.sheety.co/bc2d347620e0173a47d425cfc87639fd/flightDeals/prices"
        )

    def get_user_data(self):
        return self.get_sheet_data(
            "https://api.sheety.co/bc2d347620e0173a47d425cfc87639fd/flightDeals/users"
        )

    def get_sheet_data(self, endpoint):
        sheety_data_endpoint = endpoint
        print(f"Attempting to access {endpoint}")
        try:
            sheety_data_response = requests.get(
                url=sheety_data_endpoint, headers=self.sheety_headers
            )
            sheety_data_response.raise_for_status()
            print(f"Attempt to access {endpoint} successful")
            return sheety_data_response.json()
        except requests.exceptions.RequestException as err:
            print(f"Attempt to access {endpoint} unsuccessful, error {err}")
            return None


sheety = SheetyHandler()


def parse_raw_city_data(raw_city_data):
    formatted_city_data = {}
    for city_data in raw_city_data["prices"]:
        formatted_city_data[city_data["city"]] = {
            "iata_code": city_data["iataCode"],
            "lowest_price": city_data["lowestPrice"],
        }
    return formatted_city_data


sheety_city_data = sheety.get_city_data()
city_data = parse_raw_city_data(sheety_city_data)

amadeus = AmadeusHandler()

today = datetime.date.today().isoformat()
six_months_from_now = (
    datetime.date.today() + datetime.timedelta(6 * 365 / 12)
).isoformat()

mail = Mail()

for city, details in city_data.items():
    flight_data = amadeus.get_flight_offers(
        origin="LON",
        destination=details["iata_code"],
        departure_date=f"{today},{six_months_from_now}",
        max_price=details["lowest_price"],
    )
    if flight_data is not None:
        for flight in flight_data:
            message = (
                f'Low price alert! Only {flight["price"]} Euros to fly from {flight["origin"]} to '
                f'{flight["destination"]}, departing on {flight["departure_date"]} '
                f'and returning on {flight["return_date"]}'
            )


            mail.send_mail(message, "bradlycarpenterza@gmail.com")
