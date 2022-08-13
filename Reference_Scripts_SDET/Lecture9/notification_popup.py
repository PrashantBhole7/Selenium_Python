from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj, options=ops)

driver.get("https://whatmylocation.com/")
driver.maximize_window()