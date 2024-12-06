import os

import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()


TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")
NUMBER = os.getenv("number")

client = Client(TWILIO_SID, TWILIO_AUTH)
message = client.messages.create(to=NUMBER)
print(message.sid)


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    pass
