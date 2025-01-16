import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
count = 0

purchase_timer = time.time() + 5


def attempt_purchase(store_buttons, money):
    for button in reversed(store_buttons):
        if button.text != "":
            button_cost = int(button.text.split("-")[1].strip().replace(",", ""))
            if money > button_cost:
                button.click()
                return


while True:
    cookie.click()
    if time.time() > purchase_timer:
        store_buttons = driver.find_elements(By.CSS_SELECTOR, value="div#store b")
        money = int(driver.find_element(By.ID, value="money").text.replace(",", ""))
        attempt_purchase(store_buttons, money)
        purchase_timer = time.time() + 10
