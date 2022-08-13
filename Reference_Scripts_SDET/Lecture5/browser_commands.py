import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)

url = "https://opensource-demo.orangehrmlive.com/"
driver.get(url)
driver.maximize_window()

# Opening links in the home page
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

time.sleep(5)

# Browser Commands
# driver.close() # Close Single Browser Window where driver focused
driver.quit()  # Close multiple browser windows (and also kill process related to it)
