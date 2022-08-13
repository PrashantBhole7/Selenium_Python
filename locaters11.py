from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("/home/rapidratings/Music/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
url = "http://automationpractice.com/index.php"
driver.get(url)

driver.find_element(By.LINK_TEXT, "Sign in").click()
driver.find_element(By.ID, "email").send_keys("prashantdbhole@gmail.com")
driver.find_element(By.ID, "passwd").send_keys("12345")
driver.find_element(By.ID, "SubmitLogin").click()
driver.find_element(By.LINK_TEXT, "Sign out").click()