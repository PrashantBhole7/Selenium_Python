from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://opensource-demo.orangehrmlive.com//")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='txtUsername']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@id='txtPassword']").send_keys("admin123")
driver.find_element(By.XPATH, "//input[@id='btnLogin']").click()

driver.find_element(By.XPATH, "//b[normalize-space()='Admin']").click()
driver.find_element(By.XPATH, "//a[@id='menu_admin_UserManagement']").click()
driver.find_element(By.XPATH, "//*[@id='menu_admin_viewSystemUsers']").click()

rows = len(driver.find_elements(By.XPATH, "//table[@id='resultTable']/tbody/tr"))
print("Total number of users: ", rows)  # 47

# prining username along with user_role if user_role is ESS
for r in range(1, rows+1):
    user_role  = driver.find_element(By.XPATH, "//table[@id='resultTable']/tbody/tr["+str(r)+"]/td[3]").text
    if user_role == "ESS":
        username = driver.find_element(By.XPATH, "//table[@id='resultTable']/tbody/tr[" + str(r) + "]/td[2]").text
        print("Username:", username,"   ", "Userrole:", user_role)

driver.close()