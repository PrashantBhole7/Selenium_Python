import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://www.snapdeal.com/")
driver.get("https://www.amazon.in/")

time.sleep(3)

# Navigational Commands
driver.back()  # snapdeal
driver.forward()  # amazon

driver.refresh()  # refresh the page

driver.quit()