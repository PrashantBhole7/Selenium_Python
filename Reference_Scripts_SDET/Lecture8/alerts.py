import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# Open alert window
driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()

myalert = driver.switch_to.alert

print(myalert.text)  # I am a JS prompt
myalert.send_keys("Welcome")
myalert.accept()  # close alert window by accepting ok button
# myalert.dismiss()  # close alert window by accepting Cancel button


driver.quit()