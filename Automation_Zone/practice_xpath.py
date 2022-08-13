import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
url = "https://theautomationzone.blogspot.com/2020/07/xpath-practice.html"
driver.get(url)

driver.find_element(By.XPATH, "//a[@href='#'][text()='Home']").click()
driver.find_element(By.XPATH, "//div[@id='divA']/input").send_keys("Prashant")

time.sleep(3)
#Switch to iframe
iframe = driver.find_element(By.XPATH, "//iframe[@title='fb:page Facebook Social Plugin']")
driver.switch_to.frame(iframe)
driver.find_element(By.XPATH, "//a[@title= 'The Automation Zone']").click()
