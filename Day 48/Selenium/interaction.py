from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

fname_field = driver.find_element(By.NAME, value="fName")
fname_field.send_keys("Brad")
lname_field = driver.find_element(By.NAME, value="lName")
lname_field.send_keys("Bossman")
email_field = driver.find_element(By.NAME, value="email")
email_field.send_keys("coolmail@mail.com")

sign_up_button = driver.find_element(By.CSS_SELECTOR, value="button")
sign_up_button.click()
# driver.quit()
