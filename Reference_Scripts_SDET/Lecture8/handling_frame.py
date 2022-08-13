import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()

driver.switch_to.frame("packageListFrame")
driver.find_element(By.XPATH, "//a[normalize-space()='org.openqa.selenium']").click()
driver.switch_to.default_content()  # go back to main page

driver.switch_to.frame("packageFrame")
driver.find_element(By.XPATH, "//span[normalize-space()='WebDriver']").click()
driver.switch_to.default_content()  # go back to main page

time.sleep(3)
driver.switch_to.frame("classFrame")
# driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[6]").click()  # working fine
# driver.find_element(By.XPATH, "//div[@class='topNav']//li[text()='Deprecated']").click()  # I am not sure why it is not working as relative Xpath but it is located in browser
driver.find_element(By.XPATH, "//div[@class='topNav']/ul/li[6]").click()  # working fine

driver.close()