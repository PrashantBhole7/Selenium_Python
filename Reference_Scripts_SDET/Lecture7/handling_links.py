import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# click on link
# driver.find_element(By.LINK_TEXT, "Digital downloads").click()

# find the number of links on the page
# links = driver.find_elements(By.TAG_NAME, ='a')
links = driver.find_elements(By.XPATH, '//a')
print(len(links))  # 95

# print all links names and links 
for link in links:
    print(link.text, link.get_attribute("href"))

driver.quit()
