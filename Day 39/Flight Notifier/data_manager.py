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
post_endpoint = (
    "https://api.sheety.co/bc2d347620e0173a47d425cfc87639fd/flightDeals/prices"
)

sheety_header = {"Authorization": f"Bearer {SHEETY_AUTH}"}


class DataManager:
    def __init__(self):
        #################################################################
        #                        Sheety Get                             #
        #################################################################

        # try:
        #     self.sheety_get = requests.get(url=get_endpoint, headers=sheety_header)
        #     self.sheety_get.raise_for_status()
        # except requests.exceptions.HTTPError as errh:
        #     print(f"HTTP Error: {errh.args[0]}")

        # print(f"Response: {self.sheety_get}")
        # print(json.dumps(self.sheety_get.json(), indent=2))

        #################################################################
        #                       Import Test Json                        #
        #################################################################
        try:
            with open(f"{PATH}/sheety_get.json", "r") as test_file:
                self.test_data = json.load(test_file)
        except FileNotFoundError as errf:
            print(f"File Not Found, Error: {errf}")
