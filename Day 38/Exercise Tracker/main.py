import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

NUTRITION_ID = os.getenv("NUTRITION_ID")
NUTRITION_API = os.getenv("NUTRITION_AUTH")

