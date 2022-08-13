import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()

email_box = driver.find_element(By.XPATH, "//input[@id='Email']")
email_box.clear()
email_box.send_keys("abc@gmail.com")

# text - returns inner text of the web_element
print("Result od text: ", email_box.text)  # prints nothing

# get_attributes() - returns values of any attributes of the web_element
print("Result of get_attributes: ", email_box.get_property('value'))  # print abc@gmail.com

button = driver.find_element(By.XPATH, "//button[normalize-space()='Log in']")
print("Result of text: ", button.text)  # LOG IN
print("Result of get-attributes: ", button.get_attribute('value'))  # prints nothing
print("Result of get-attributes: ", button.get_attribute('type'))  # prints submit
time.sleep(2)
driver.quit()

