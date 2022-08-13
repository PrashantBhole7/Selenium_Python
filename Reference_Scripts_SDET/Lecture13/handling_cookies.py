import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Capture cookies from browser
cookies = driver.get_cookies()
print("Size of cookies: ", len(cookies))  # 3

# Prints details of cookies
# for c in cookies:
#     # print(c)
#     print(c.get('name'), ":", c.get('value'))

# Add new cookies to browser
driver.add_cookie({"name":"Mycookies", "value":"123456"})
cookies = driver.get_cookies()
print("Size of cookies after adding new onex: ", len(cookies))  # 4

# Delete specific cookie
driver.delete_cookie("Mycookies")
cookies = driver.get_cookies()
print("Size of cookies after deleting one: ", len(cookies))  # 3

# Deleting all the cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("Size of cookies after deleting all: ", len(cookies))  # 0

driver.quit()
