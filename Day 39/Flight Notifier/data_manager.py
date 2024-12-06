import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

SHEETY_AUTH = os.getenv("SHEETY_AUTH")
PATH = "./Day 39/Flight Notifier"

get_endpoint = (
    "https://api.sheety.co/bc2d347620e0173a47d425cfc87639fd/flightDeals/prices"
)
put_endpoint = (
    "https://api.sheety.co/bc2d347620e0173a47d425cfc87639fd/flightDeals/prices"
)

sheety_header = {"Authorization": f"Bearer {SHEETY_AUTH}"}


class DataManager:
    def __init__(self):
        pass

    def get_sheet_data(self):
        try:
            self.sheety_get = requests.get(url=get_endpoint, headers=sheety_header)
            self.sheety_get.raise_for_status()
            print(f"Response: {self.sheety_get}")
            return self.sheety_get.json()
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh.args[0]}")
            return None

    def get_test_sheet_data(self):
        test_data = None
        try:
            with open(f"{PATH}/sheety_get.json", "r") as test_file:
                test_data = json.load(test_file)
            return test_data
        except FileNotFoundError as errf:
            print(f"File Not Found, Error: {errf}")
            return None

    def get_test_updated_sheet_data(self):
        test_data = None
        try:
            with open(f"{PATH}/sheety_updated.json", "r") as test_file:
                test_data = json.load(test_file)
            return test_data
        except FileNotFoundError as errf:
            print(f"File Not Found, Error: {errf}")
            return None
    
    def update_sheet_data(self, city, id):
        body = {
            "price": city
        }
        try:
            response = requests.put(url=f"{put_endpoint}/{id}", json=body, headers=sheety_header)
            print(f"Response is: {response}")
            response.raise_for_status()
            print("Put Request Successful")
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh.args[0]}")
