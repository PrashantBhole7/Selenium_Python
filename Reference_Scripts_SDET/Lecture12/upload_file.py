from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(10)

driver.get("https://www.monsterindia.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[@class='btn block resume-btn btn-orange mt20']").click()
# driver.switch_to.frame("parsingResponseForm")
driver.find_element(By.XPATH, "//*[@id='file-upload']").send_keys("/home/prashant/Documents/sample.pdf")

