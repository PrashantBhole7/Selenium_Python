# Ctrl+C
# Ctrl+A
# tab
# Ctrl+V

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(10)

driver.get("https://text-compare.com/")
driver.maximize_window()

input_1  = driver.find_element(By.ID, "inputText1")
input_2  = driver.find_element(By.ID, "inputText2")

input_1.send_keys("Welcome to Selenium")

act = ActionChains(driver)

# input_1 : Ctrl + A : Select all the text in input_1
# act.key_down(Keys.CONTROL)
# act.send_keys("a")
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# input_1 : Ctrl + C : Copy text
# act.key_down(Keys.CONTROL)
# act.send_keys("c")
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# Press tab key to naviagte to input_2
# act.send_keys(Keys.TAB)
# act.perform()

act.send_keys(Keys.TAB).perform()

# Press Ctrl + V : To paste text in input_2

act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()