import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://opensource-demo.orangehrmlive.com//")
driver.maximize_window()


#Login
driver.find_element(By.XPATH, "//input[@id='txtUsername']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@id='txtPassword']").send_keys("admin123")
driver.find_element(By.XPATH, "//input[@id='btnLogin']").click()
time.sleep(3)

# admin --> user  management --> users
admin = driver.find_element(By.XPATH, "//b[normalize-space()='Admin']")
user_management = driver.find_element(By.XPATH, "//a[@id='menu_admin_UserManagement']")
users = driver.find_element(By.XPATH, "//*[@id='menu_admin_viewSystemUsers']")

# MouseHover
act = ActionChains(driver)

act.move_to_element(admin).move_to_element(user_management).move_to_element(users).click().perform()
