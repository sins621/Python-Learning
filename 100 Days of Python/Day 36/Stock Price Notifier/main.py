import json
import os

import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
PROJECT_PATH = "./Day 36/Stock Price Notifier"

ALPHAVANTAGE_AUTH = os.environ.get("ALPHAVANTAGE_AUTH")

alphavantage_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_AUTH,
}

alphavantage_endpoint = "https://www.alphavantage.co/query"


def get_test_stocks() -> dict:
    with open(f"{PROJECT_PATH}/stocks_test_data.json") as json_file:
        stocks_data: dict = json.load(json_file)
    return stocks_data


def get_stocks() -> dict:
    stocks_response = requests.get(alphavantage_endpoint, alphavantage_params)
    stocks_response.raise_for_status()
    print(f"Querying Stocks API, Status: {stocks_response.status_code}")
    return stocks_response.json()


def get_closing_balances(stocks_data: dict) -> list:
    time_series = stocks_data.get("Time Series (Daily)", {})
    closing_balances = [
        float(balances["4. close"]) for balances in time_series.values()
    ]
    return closing_balances


def calculate_diff_percent(closing_balance1, closing_balance2):
    return (closing_balance2 - closing_balance1) / closing_balance1 * 100


NEWSAPI_AUTH = os.environ.get("NEWSAPI_AUTH")

news_params = {
    "apiKey": NEWSAPI_AUTH,
    "pageSize": 3,
    "q": COMPANY_NAME,
}

news_endpoint = "https://newsapi.org/v2/top-headlines?"


def get_test_news() -> dict:
    with open(f"{PROJECT_PATH}/news_test_data.json") as json_file:
        news_data: dict = json.load(json_file)
    return news_data


def get_news() -> dict:
    news_response = requests.get(news_endpoint, news_params)
    news_response.raise_for_status()
    status_code = news_response.status_code
    print(f"Querying News API, Status: {status_code}")
    return news_response.json()


def filter_news(news_data: dict) -> list:
    required_keys = {"title", "description"}
    news_list = []
    for article in news_data.get("articles", []):
        filtered_article = {
            key: article[key] for key in required_keys if key in article
        }
        news_list.append(filtered_article)
    return news_list


TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH = os.environ.get("TWILIO_AUTH")


def send_sms(body_text):
    client = Client(TWILIO_SID, TWILIO_AUTH)
    message = client.messages.create(
        from_="+17753682906", body=body_text, to="+27765261782"
    )
    print(f"Attempting to send SMS, Status: {message.status}")


closing_balances = get_closing_balances(get_stocks())
day_to_day_difference = round(
    calculate_diff_percent(closing_balances[2], closing_balances[1]), 2
)

day_to_day_formatted = ""
if day_to_day_difference < 0:
    day_to_day_formatted = f"🔻{str(day_to_day_difference).strip('-')}"
else:
    day_to_day_formatted = f"🔺{day_to_day_difference}"


if day_to_day_difference > 5 or day_to_day_difference < -5:
    filtered_news = filter_news(get_news())
    body_text = f"""{STOCK}: {day_to_day_formatted}%
Headline 1: {filtered_news[0]["title"]}
Brief: {filtered_news[0]["description"]}
Headline 2: {filtered_news[1]["title"]}
Brief: {filtered_news[1]["description"]}
Headline 3: {filtered_news[2]["title"]}
Brief: {filtered_news[2]["description"]}
"""
    send_sms(body_text)
