import json
import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

NUTRITION_AUTH = os.getenv("NUTRITION_AUTH")
print(f"Getting Auth Key, response: {NUTRITION_AUTH}")
NUTRITION_ID = os.getenv("NUTRITION_ID")
print(f"Getting Auth ID, response: {NUTRITION_ID}")

NATURAL_LANG_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

GENDER = "male"
WEIGHT_KG = 69
HEIGHT_CM = 173
AGE = 27

user_exercise = input("Tell me which exercises you did: ")
#user_exercise = "I ran for 10 kilometers and did 20 pushups"

natural_lang_params = {
    "query": user_exercise,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}
natural_lang_headers = {
    "x-app-key": NUTRITION_AUTH,
    "x-app-id": NUTRITION_ID,
}

print("Attempting Natural Lang API Request")
natural_lang_response = requests.post(
    NATURAL_LANG_ENDPOINT, headers=natural_lang_headers, json=natural_lang_params
)
natural_lang_response.raise_for_status()
print(f"Status Code: {natural_lang_response.status_code}")
print(
    f"Response Output: {json.dumps(natural_lang_response.json()["exercises"], indent=2)}"
)
exercise_info = natural_lang_response.json()["exercises"]

# SHEETY_AUTH = os.getenv("SHEETY_AUTH")
# print(f"Getting Auth Key, response: {SHEETY_AUTH}")
# SHEETY_ID = os.getenv("SHEETY_ID")
# print(f"Getting Auth ID, response: {SHEETY_ID}")
#
# sheety_post_endpoint = f"https://api.sheety.co/{SHEETY_ID}/myWorkouts/workouts"
#
# sheety_header = {
#     "Authorization": f"Bearer {SHEETY_AUTH}"
# }
#
# exercises = []
# current_date = datetime.now()
# for exercise in exercise_info:
#     new_exercise = {
#         "workout": {
#             "date": current_date.strftime("%d/%m/%Y"),
#             "time": current_date.strftime("%H:%M"),
#             "exercise": exercise["user_input"].title(),
#             "duration": exercise["duration_min"],
#             "calories": exercise["nf_calories"],
#         }
#     }
#     print("Attempting to Parse Exercise Data")
#     print(new_exercise)
#     exercises.append(new_exercise)
#
#
# for exercise in exercises:
#     print("Attempting API Post to Sheety")
#     sheety_response = requests.post(sheety_post_endpoint, json=exercise, headers=sheety_header)
#     print(f"Status Code: {sheety_response.status_code}")
#     print(sheety_response)
#     sheety_response.raise_for_status()
