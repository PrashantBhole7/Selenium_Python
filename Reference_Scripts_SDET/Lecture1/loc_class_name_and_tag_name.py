from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("/home/rapidratings/Music/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
driver.get("http://automationpractice.com/index.php")

# Locaters: class_name, tag_name
sliders = driver.find_elements(By.CLASS_NAME, "homeslider-container")
print(len(sliders))

links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))
