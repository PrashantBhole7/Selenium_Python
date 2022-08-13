import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()

# Open alert window
driver.find_element(By.XPATH, "//input[@value='Login']").click()

time.sleep(3)
driver.switch_to.alert.accept()

driver.quit()