import requests
import html


parameters = {
    "amount": 10,
    "category": 31,
    "type": "boolean",
}

response = requests.get(
	"https://opentdb.com/api.php", 
	params=parameters
)
data = response.json()
question_data = data["results"]

for question in question_data:
    question["question"] = html.unescape(question["question"])

# json_str = json.dumps(question_data, indent=4)
# print(json_str)