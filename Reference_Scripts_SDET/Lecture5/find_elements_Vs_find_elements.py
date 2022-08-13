import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)

url = "https://demo.nopcommerce.com/"
driver.get(url)
driver.maximize_window()

#######  find_element()  - Return Single Webelement

# 1) Locator Matchings with single webelement
# element = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
# element.send_keys("Apple Latest Iphone")

# 2) Locators Matching with multiple webelements
# element = driver.find_element(By.XPATH, "//div[@class= 'footer']//a")
# print(element.text)  # prints first link from footer that is Sitemap

# 3) Element is not available then gives Exception "NoSuchElementException"
# login_element = driver.find_element(By.LINK_TEXT, "Log")
# login_element.click()

####### find_elements() - Return multiple elements

# 1) Locator Matchings with single webelement
# elements = driver.find_elements(By.XPATH, "//input[@id='small-searchterms']")
# print(len(elements))  # 1
# elements[0].send_keys("Apple Latest Iphone")

# 2) Locators Matching with multiple webelements
# elements = driver.find_elements(By.XPATH, "//div[@class= 'footer']//a")
# print(len(elements))  # 23
# # print(elements[0].text)     # prints first link from footer that is Sitemap
# for ele in elements:
#     print(ele.text)
# time.sleep(2)



# 3) Element is not available then gives Zero
login_elements = driver.find_elements(By.LINK_TEXT, "Log")
print("Elements Returns: ", len(login_elements))  # 0

driver.quit()