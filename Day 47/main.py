import os
import smtplib

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()


class Mail:
    def __init__(self):
        self.my_email = "fl0586114@gmail.com"
        self.my_password = os.getenv("MAIL")

    def send_mail(self, message, to_address):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(
                user=self.my_email, password=self.my_password  # pyright: ignore
            )
            connection.sendmail(
                from_addr=self.my_email,
                to_addrs=to_address,
                msg=message,
            )
            print(f"Sending Amazon Offer Mail to {to_address}")


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0",
    "Accept-Language": "en-US,en;q=0.5",
}

website_url = "https://www.amazon.co.za/SAMSUNG-WIFI-64GB-GRAPHITE-SM-X210NZAAAFA/dp/B0D17C6GD5?crid=37U91QHWMXAXO&dib=eyJ2IjoiMSJ9.aIe1nS12HQn183XEvLj-tyKUTd3dz7cvYnBTf-ck-LfMSv6z5zZURqHj7EBoMTHqSbXU3I_pvXaGCfE0UpVX6NF09FgPpu1mlO21L24U2blvWWWAJt8Twduz73Sf0YhgKegEZ6e2o1pzAwR9K0T9L3sJ7YWnShASktAAQ5Qln2plCqPTiGG1bsf7UIVVet1_TZc9U6jcEdiCGbUWHvpoROBtbXXVTYuxE7vDmnWPMlGlumwWN2Kj9E751I96Bp5V-3_r24AFIQGWNcbkDyflv1CupUHNI2wWTkfz7cAp3ZDij92K25KYmtXcaiRssfvgmvRrVhtr7BCdWGvMULI9NZA1htesHprhu-rJ0so3n2gIQ_ckbu8yAP1Xb65FTeQrpJAAWu9AHT2zlgahl8bBDLEvfEEZSLCnu9pr3h6cdDfndqkLx_M8HrN1EcMjiOtG.-1nq7Nz0qHVDOERbw_m4qtccLeCke_RJiT3mARjY_1Q&dib_tag=se&keywords=galaxy+a9%2B&qid=1734169079&sprefix=galaxy+a9+%2Caps%2C569&sr=8-2"
response = requests.get(url=website_url, headers=headers)
response.raise_for_status()
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

price_whole = soup.find(class_="a-price-whole").getText().replace(",","")  # pyright: ignore
price_fraction = soup.find(class_="a-price-fraction").getText()  # pyright:ignore
full_price = float(f"{price_whole}{price_fraction}")

mail = Mail()

if full_price < 4000.00:
    mail.send_mail(
        f"The product you were watching is only {full_price}",
        "bradlycarpenterza@gmail.com",
    )
