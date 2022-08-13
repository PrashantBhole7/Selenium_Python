import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

drpcountry = Select(driver.find_element(By.XPATH, "//select[@id='input-country']"))

# select option from dropdown
# drpcountry.select_by_visible_text("India")
# drpcountry.select_by_value("10")  # Argentina
# drpcountry.select_by_index(13=)

# Capture all the options and print them
# all_option = drpcountry.options
# print("Total Options : ", len(all_option))
#
# for opt in all_option:
#     print(opt.text)

# capture option form dropdown without using built-in method
# for opt in all_option:
#     if opt.text == "Armenia":
#         opt.click()
#         break

#  We can also get all the options without using inbuilt options keyword as
allOptions = driver.find_elements(By.XPATH, "//select[@id='input-country']/option")
print(len(allOptions))  # 242

# Assignment bt using url : https://testautomationpractice.blogspot.com/ : practice dropdown

time.sleep(2)
driver.quit()