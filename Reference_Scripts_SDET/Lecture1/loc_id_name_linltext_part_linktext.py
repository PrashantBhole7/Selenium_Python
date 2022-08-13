from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
url = "http://automationpractice.com/index.php"
driver.get(url)

# Locaters id, name, linktext, partial_link_test
driver.find_element(By.XPATH, "//a[@class='login']").click()
driver.find_element(By.ID, "email").send_keys("prashantdbhole@gmail.com")
driver.find_element(By.ID, "passwd").send_keys("12345")
driver.find_element(By.ID, "SubmitLogin").click()
driver.find_element(By.LINK_TEXT, "Sign out").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "gn out").click()

