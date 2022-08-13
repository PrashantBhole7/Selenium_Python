from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("/home/rapidratings/Music/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

# absolute xpath
# driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys("T-shirts")
# driver.find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button").click()

# relative xpath
# driver.find_element(By.XPATH, "//*[@id='search_query_top']").send_keys("T-shirts")
# driver.find_element(By.XPATH, "//*[@id='searchbox']/button").click()

# or and and
# driver.find_element(By.XPATH, "//*[@id='search_query_top' or @name='search_query']").send_keys("T-shirts")
# driver.find_element(By.XPATH, "//*[@name='submit_search' and @class='btn btn-default button-search']").click()

# Contains and start-with
# driver.find_element(By.XPATH, "//input[contains(@id, 'search')").send_keys("T-shirt")
# driver.find_element(By.XPATH, "//input[starts-with(@name, 'submit_')").click()

#text()
driver.find_element(By.XPATH, "//a[text()='Women']").click()
