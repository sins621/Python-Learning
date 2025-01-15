import requests
import json


def send_request(method, url, headers=None, params=None, data=None, json_payload=None):
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            data=data,
            json=json_payload,
        )

        print(f"Status Code: {response.status_code}")
        print("Response Headers:")
        for key, value in response.headers.items():
            print(f"  {key}: {value}")

        print("\nResponse Body:")
        try:
            parsed_json = response.json()
            print(json.dumps(parsed_json, indent=2))
        except json.JSONDecodeError:
            print(response.text)

    except requests.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    method = "DELETE"
    url = "http://127.0.0.1:5000/delete-cafe/8"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_TOKEN_HERE",
    }

    params = {
        # "name": "My Cafe",
        # "map_url": "http://cool.com",
        # "img_url": "http://cool_image_url",
        # "location": "Kraaifontein",
        # "seats": "2",
        # "has_toilet": False,
        # "has_wifi": True,
        # "has_sockets": True,
        # "can_take_calls": True,
        # "coffee_price": 1.1,
        "api_key": "secret_key"
    }

    json_payload = {"title": "foo", "body": "bar", "userId": 1}

    send_request(method, url, params)
