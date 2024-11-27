import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "bradlycarpenterza"
TOKEN = os.getenv("pixela_auth")

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(f"Attemping to Post to Pixela, Status: {response.status_code}")
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

GRAPH_ID = "graph1"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

headers = {"X-USER-TOKEN": TOKEN}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(f"Making Request to Add Graph to Pixela, Status: {response.status_code}")
# print(response.text)

pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()
today_date = today.strftime("%Y%m%d")

pixel_data = {
    "date": today_date,
    "quantity": "20",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(f"Making Request to Add a Pixel to Pixela, Status: {response.status_code}")
# print(response.text)

update_endpoint = f"{pixel_creation_endpoint}/{today_date}"

update_data = {
    "quantity": "19"
}

# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(f"Making Request to Update a Pixel to Pixela, Status: {response.status_code}")
# print(response.text)


response = requests.delete(url=update_endpoint, headers=headers)
print(f"Making Request to Delete a Pixel to Pixela, Status: {response.status_code}")
print(response.text)
