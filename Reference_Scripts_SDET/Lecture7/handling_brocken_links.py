# we need to install requests library for broken links

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests as requests

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

# To find broken links we need to first find all the links in the page
links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))
count = 0

for link in links:
    url = link.get_attribute("href")
    try:
        res = requests.head(url)
    except:
        None
    if res.status_code >= 400:
        print(count, url, "is broken link")
        count += 1
    else:
        print(url, "is valid link")
print("Total number of broken links : ", count)
