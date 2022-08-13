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

# driver.save_screenshot("/home/prashant/PycharmProjects/SeleniumPython/Reference_Scripts_SDET/Lecture13/homepage.png")
driver.save_screenshot(os.getcwd()+"/homepage1.png")
# driver.get_screenshot_as_file(os.getcwd()+"/homepage2.png")


driver.quit()