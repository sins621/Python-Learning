# This file will need to use the DataManager,FlightSearch, FlightData, 
# NotificationManager classes to achieve the program requirements.
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_KEY = os.getenv('SHEETY')
