import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)

url = "https://opensource-demo.orangehrmlive.com/"
driver.get(url)
driver.maximize_window()

# Application Commands
print(driver.title) # OrangeHRM
print(driver.current_url) # https://opensource-demo.orangehrmlive.com/
print(driver.page_source)

time.sleep(3)

driver.quit()