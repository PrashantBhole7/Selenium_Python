from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('/home/rapidratings/Music/chromedriver')
driver = webdriver.Chrome(service=s)
url='https://admin-demo.nopcommerce.com/login'
driver.get(url)
# driver.find_element(By.ID, 'Email').clear()
# driver.find_element(By.ID, 'Email').send_keys("admin@yourstore.com")
# driver.find_element(By.ID, 'Password').clear()
# driver.find_element(By.ID, 'Password').send_keys("admin")
# driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button').click()

# exp_title = 'Dashboard / nopCommerce administration'
# act_title = driver.title
#
# if exp_title == act_title:
#     print("Test is Successful")
# else:
#     print("Test is failed")

# driver.close()