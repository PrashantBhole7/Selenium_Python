from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('/home/rapidratings/Music/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get("https://www.facebook.com/")
driver.maximize_window()

# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc@gmial.com")
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc@gmial.com")
# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abc@gmial.com")
# driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("abc@gmial.com")
# driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_email]").send_keys("abc@gmial.com")
driver.find_element(By.CSS_SELECTOR, "[data-testid=royal_email]").send_keys("abc@gmial.com")
driver.find_element(By.CSS_SELECTOR, "[data-testid=royal_pass]").send_keys("xyz")
