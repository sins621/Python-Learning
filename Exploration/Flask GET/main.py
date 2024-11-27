import requests

params = {
    "books": "books"
}

response = requests.get(url="http://41.164.76.23:5000/books")
print(response)
print(response.text)
