from data_manager import DataManager
from flight_data import FlightData

data_manager = DataManager()
flight_data = FlightData()
sheet_data = data_manager.get_test_updated_sheet_data()

##### This Step Has Been Completed
# sheet_data = data_manager.get_test_sheet_data()
# for city in sheet_data["prices"]:
#     city_info = flight_data.get_city_info(city["city"])
#     city["iataCode"] = city_info["iataCode"]

# for city in sheet_data["prices"]:
#     data_manager.update_sheet_data(city, city["id"])

for city in sheet_data["prices"]:
    print(flight_data.get_flight_deal("LHR", city["iataCode"], city["lowestPrice"]))
