import html

import requests

# import json


parameters = {
    "amount": 10,
    "category": 31,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]

for question in question_data:
    question["question"] = html.unescape(question["question"])

# json_str = json.dumps(question_data, indent=4)
# print(json_str)

