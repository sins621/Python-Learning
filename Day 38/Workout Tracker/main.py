import os
import requests
import json
from datetime import datetime
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

# user_exercise = input("Tell me which exercises you did: ")
user_exercise = "I ran for 10 kilometers and did 20 pushups"

params = {
    "query": user_exercise,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

headers = {
    "x-app-key": NUTRITION_AUTH,
    "x-app-id": NUTRITION_ID,
}

print("Attempting API Request")
response = requests.post(NATURAL_LANG_ENDPOINT, headers=headers, json=params)
response.raise_for_status()
print(f"Status Code: {response.status_code}")
print(f"Response Output: {json.dumps(response.json(), indent=2)}")
