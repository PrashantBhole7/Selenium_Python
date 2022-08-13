import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation/")
driver.maximize_window()

# 1) select specific checkbox
# driver.find_element(By.XPATH, "//input[@id='monday']").click()

# 2) select all the 7 checkboxes
all_checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
print(len(all_checkboxes))  #7

# Approach 1
# for i in range(len(all_checkboxes)):
#     all_checkboxes[i].click()
time.sleep(2)
# Approach 2
for checkbox in all_checkboxes:
    checkbox.click()

# 3) select multiple checkboxes by choice
# for checkbox in all_checkboxes:
#     weekday = checkbox.get_attribute("id")
#     if weekday == 'monday' or weekday == 'sunday':
#         checkbox.click()

# 4) select last two checkboxes
# for i in range(len(all_checkboxes)-2, len(all_checkboxes)):
#     all_checkboxes[i].click()

# 5) select first two checkboxes
# for i in range(len(all_checkboxes)):
#     if i<2:
#         all_checkboxes[i].click()

time.sleep(2)
# 6) clearing all checkboxes
for checkbox in all_checkboxes:
    if checkbox.is_selected():
        checkbox.click()
