from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

# date of birth
driver.find_element(By.XPATH, "//input[@id='dob']").click()  # opens the datepicker

# selecting year
date_picker_year = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
date_picker_year.select_by_visible_text("1990")

# selecting month
date_picker_month = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
date_picker_month.select_by_visible_text("Aug")

dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for ele in dates:
    if ele.text == "7":
        ele.click()
        break
