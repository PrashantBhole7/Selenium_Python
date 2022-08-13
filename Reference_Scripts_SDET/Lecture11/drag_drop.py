import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(10)

driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

act = ActionChains(driver)

source_ele = driver.find_element(By.ID, "box1")
target_ele = driver.find_element(By.ID, "box106")
act.drag_and_drop(source_ele, target_ele).perform()

source_ele = driver.find_element(By.ID, "box6")
target_ele = driver.find_element(By.ID, "box103")
act.drag_and_drop(source_ele, target_ele).perform()

time.sleep(5)
driver.close()
