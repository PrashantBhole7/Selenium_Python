from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def headless_chrome():
    ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
    ops = webdriver.ChromeOptions()
    ops.headless = True
    driver = webdriver.Chrome(service=ser_obj, options=ops)
    return driver


driver = headless_chrome()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.close()