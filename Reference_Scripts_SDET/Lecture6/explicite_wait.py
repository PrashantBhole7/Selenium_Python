import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)

# mywait = WebDriverWait(driver, 10) # explicit wait basic declaration
mywait = WebDriverWait(driver, 10, ignored_exceptions=[NoSuchElementException,
                       ElementNotVisibleException,
                       ElementNotSelectableException,
                       Exception])
driver.get("https://www.google.com/")
driver.maximize_window()

search_box = driver.find_element(By.XPATH, "//input[@name='q']")
search_box.send_keys("Selenium")
search_box.submit()

search_link = mywait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
search_link.click()

driver.quit()
