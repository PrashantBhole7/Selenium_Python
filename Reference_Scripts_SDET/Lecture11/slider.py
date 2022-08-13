import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(10)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min_slider = driver.find_element(By.XPATH, "//span[1]")
max_slider = driver.find_element(By.XPATH, "//span[2]")

print("Location of slider before moving.....")
print(min_slider.location)  # {'x': 59, 'y': 250}
print(max_slider.location)  # {'x': 517, 'y': 250}

act = ActionChains(driver)

act.drag_and_drop_by_offset(min_slider, 100, 0).perform()
act.drag_and_drop_by_offset(max_slider, -39, 0).perform()

print("Location of slider after moving.....")
print(min_slider.location)  # {'x': 160, 'y': 250}
print(max_slider.location)  # {'x': 475, 'y': 250}

time.sleep(5)
driver.close()
