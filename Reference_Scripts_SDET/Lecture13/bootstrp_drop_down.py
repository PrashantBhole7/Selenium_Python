import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()

country_lists = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")

for country in country_lists:
    if country.text == "India":
        country.click()
        break

time.sleep(5)
driver.close()