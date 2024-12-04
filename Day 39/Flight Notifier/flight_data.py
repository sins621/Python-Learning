import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

AMADEUS_KEY = os.getenv("AMADEUS_KEY")
AMADEUS_SECRET = os.getenv("AMADEUS_SECRET")
AMADEUS_TOKEN = os.getenv("AMADEUS_TOKEN")
PATH = "./Day 39/Flight Notifier"

amadeus_city_get = "https://test.api.amadeus.com/v1/reference-data/locations/cities"


class FlightData:
    def __init__(self, **kw):
        self.params = {"keyword": kw.get("city"), "max": 1}
        self.headers = {"Authorization": f"Bearer {AMADEUS_TOKEN}"}
        #################################################################
        #                          City Get                             #
        #################################################################
        # try:
        #     self.city_get = requests.get(
        #         url=amadeus_city_get, headers=self.headers, params=self.params
        #     )
        #     self.city_get.raise_for_status()
        # except requests.exceptions.HTTPError as errh:
        #     print(f"HTTP Error: {errh.args[0]}")
        # else:
        #     print(self.city_get)
        #     print(json.dumps(self.city_get.json(), indent=2))

        #################################################################
        #                       Import Test Json                        #
        #################################################################
        try:
            with open(f"{PATH}/city_get.json", "r") as test_file:
                self.test_data = json.load(test_file)["data"]
        except FileNotFoundError as errf:
            print(f"File Not Found, Error: {errf}")
