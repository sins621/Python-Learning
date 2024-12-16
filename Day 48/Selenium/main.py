from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

event_title_selector = "div.medium-widget.event-widget.last div.shrubbery ul.menu a"
event_date_selector = "div.medium-widget.event-widget.last div.shrubbery ul.menu time"

event_title_elements = driver.find_elements(By.CSS_SELECTOR, value=event_title_selector)
event_date_elements = driver.find_elements(By.CSS_SELECTOR, value=event_date_selector)

event_titles = [element.text for element in event_title_elements]

event_dates = []
for date_element in event_date_elements:
    datetime_str = date_element.get_attribute(
        "datetime"
    )  # Get the 'datetime' attribute
    if datetime_str:
        dt_object = datetime.fromisoformat(datetime_str.replace("Z", "+00:00"))
        event_dates.append(dt_object)

for title, event_date in zip(event_titles, event_dates):
    print(f"{title}: {event_date.strftime('%Y-%m-%d')}")

driver.quit()
