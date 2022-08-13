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

# Opening register page in another tab
# regi_link = Keys.CONTROL+Keys.RETURN
# driver.find_element(By.LINK_TEXT, "Register").send_keys(regi_link)

# New Tab : Selenium4 : Open new tab and switches to new tab
# driver.get("https://opencart.com/")
# driver.switch_to.new_window('tab')
# driver.get("https://opencart.com/")

# New Tab : Selenium4 : Open new browser window and switches to new window
driver.get("https://opencart.com/")
driver.switch_to.new_window('window')
driver.get("https://opencart.com/")

time.sleep(3)
driver.quit()
