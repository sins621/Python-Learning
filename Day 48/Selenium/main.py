from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"The price is {price_dollar}.{price_cents}")
#
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(
#     By.CSS_SELECTOR, value=".documentation-widget a"
# )
#
# download_link = driver.find_element(
#     By.XPATH, value="/html/body/div/div[3]/div/section/div[2]/div[2]/p[2]/a"
# )
#
# print(documentation_link)
# print(download_link)

upcoming_event_title_elements = driver.find_elements(
    By.CSS_SELECTOR, value="div.medium-widget.event-widget.last div.shrubbery ul.menu a"
)

upcoming_event_date_elements = driver.find_elements(
    By.CSS_SELECTOR,
    value="div.medium-widget.event-widget.last div.shrubbeery ul.menu time",
)


driver.quit()
