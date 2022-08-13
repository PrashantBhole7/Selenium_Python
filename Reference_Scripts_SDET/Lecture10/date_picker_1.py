from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

frame_obj = driver.find_element(By.XPATH, "//*[@id='content']/iframe")
driver.switch_to.frame(frame_obj)

# driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("05/30/2022")

# For the date_picker whose not supported by send_keys method

year = "2021"
month = "August"
date = "7"


driver.find_element(By.XPATH, "//input[@id='datepicker']").click()  # opens datepicker

# For finding required year and month
while True:
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']")
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']")
    if yr.text == year and mon.text == month:
        break
    else:
        # driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]").click()  # next arrow
        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/a[1]/span').click()  # previous arrow

# for finding required date
dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for ele in dates:
    if ele.text == date:
        ele.click()
        break
