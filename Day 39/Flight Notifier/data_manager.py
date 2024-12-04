import os

import requests
from dotenv import load_dotenv

load_dotenv()

SHEETY_KEY = os.getenv("SHEETY")

get_url = "https://api.sheety.co/bc2d347620e0173a47d425cfc87639fd/flightDeals/prices"
post_url = "https://api.sheety.co/bc2d347620e0173a47d425cfc87639fd/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    pass
