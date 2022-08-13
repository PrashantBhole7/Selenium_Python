import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)

url = "https://demo.nopcommerce.com/register"
driver.get(url)
driver.maximize_window()

# Conditional Commands
# is_displayed() and is_enabled()
search_box = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("Display Status: ", search_box.is_displayed())  # True
print("Enable Status: ", search_box.is_enabled())  # True

# is_selected() - used for radio_buttons and check_boxes
rd_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
rd_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")

print(rd_male.is_selected())  # False
print(rd_female.is_selected())  # False

rd_male.click()  # selected radio button
time.sleep(3)
print("After Selecting male radio button....")
print(rd_male.is_selected())  # True
print(rd_female.is_selected())  # False

rd_female.click()  # selected radio button
time.sleep(3)
print("After Selecting female radio button....")
print(rd_male.is_selected())  # False
print(rd_female.is_selected())  # True

driver.quit()
