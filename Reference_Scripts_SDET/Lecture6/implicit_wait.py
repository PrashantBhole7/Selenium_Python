import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://www.google.com/")
driver.maximize_window()

driver.implicitly_wait(10)  # seconds

search_box = driver.find_element(By.XPATH, "//input[@name='q']")
search_box.send_keys("Selenium")
search_box.submit()

# time.sleep(5)  # Performance of the scripts is very low
driver.find_element(By.XPATH, "//h3[text()='Selenium']").click()
    
driver.quit()
