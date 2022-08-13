import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(10)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# 1. Scroll down the page by pixel
# driver.execute_script("window.scrollBy(0,3000)", "")
# value = driver.execute_script("return pageYOffset;")
# print("Number of pixel moved: ", value)  #  3000

# 2. Scroll down the page till the element is visible
# flag = driver.find_element(By.XPATH, "//img[@alt='Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# value = driver.execute_script("return pageYOffset;")
# print("Number of pixel moved: ", value) # 4935

# 3. Scroll down the page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return pageYOffset;")
print("Number of pixel moved: ", value)  # 5977

time.sleep(2)

# Scroll upto starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return pageYOffset;")
print("Number of pixel moved: ", value)
