from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('/home/rapidratings/Music/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get("https://www.facebook.com/")
driver.maximize_window()

#tag & id    tagname#valueofID
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc@gmial.com")
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc@gmial.com")

#tag & class     tabname.valueofCLASS
# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abc@gmial.com")
# driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("abc@gmial.com")

# tag & attributes   tagname[attribute=valueofattributes without double or single quote]
# driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_email]").send_keys("abc@gmial.com")
# driver.find_element(By.CSS_SELECTOR, "[data-testid=royal_email]").send_keys("abc@gmial.com")
# driver.find_element(By.CSS_SELECTOR, "[data-testid=royal_pass]").send_keys("xyz")


# tag, class & attributes tagname.valueofCLASS[attribute=value] It is used when tag and class combination mathing with two elements
driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_pass]").send_keys("xyz")
