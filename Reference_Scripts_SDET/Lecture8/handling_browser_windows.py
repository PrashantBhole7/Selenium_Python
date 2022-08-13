import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# window_id = driver.current_window_handle
# print(window_id) # CDwindow-CC738751F71B649AB69E29C7454CBBA4
#                  # CDwindow-DA08E85F2F9B49B3C49EAC06D9071F4F

driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']").click()

windows_ids = driver.window_handles


# Approach 1
# parent_win_id = windows_ids[0]  # CDwindow-76D30AF249484AE48D8F7DAA3E4A213A
# child_win_id = windows_ids[1]  # CDwindow-A561937386439EE32634390BA67F0784
# # print(parent_win_id, child_win_id)
# driver.switch_to.window(child_win_id)
# print(driver.title)  # OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS
# driver.switch_to.window(parent_win_id)
# print(driver.title)  # OrangeHRM

# Approach 2
# for win in windows_ids:
#     driver.switch_to.window(win)
#     print(driver.title)

time.sleep(3)

# Closed specific browser window 
for win in windows_ids:
    driver.switch_to.window(win)
    if driver.title == "OrangeHRM" or driver.title == "xyz":  # we can close windows that we want
        driver.close()

driver.quit()