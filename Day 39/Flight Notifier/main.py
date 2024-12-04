# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData

data_manager = DataManager()
flight_data = FlightData()
print(flight_data.test_data[0]["iataCode"])
