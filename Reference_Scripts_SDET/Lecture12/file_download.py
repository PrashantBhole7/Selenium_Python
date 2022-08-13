import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
location = os.getcwd()


def chrome_setup():
    ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
    # Download file in disered location
    preference = {"download.default_directory":location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preference)
    driver = webdriver.Chrome(service=ser_obj, options=ops)
    return driver


def edge_setup():
    ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
    preference = {"download.default_directory":location}
    # Download file in disered location
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", preference)
    driver = webdriver.Edge(service=ser_obj, options=ops)
    return driver


def firefox_setup():
    ser_obj = Service("/home/prashant/Documents/Browser_Driver/geckodriver")
    # settings
    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword")  # mimetype_link : https://www.sitepoint.com/mime-types-complete-list/
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList",2)  # 0-desktop, 1-downloads, 2-Desired location
    ops.set_preference("browser.download.dir", location)
    driver = webdriver.Firefox(service=ser_obj, options=ops)
    return driver

# driver = chrome_setup()
driver = firefox_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download//")
driver.maximize_window()
driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()
# driver.find_element(By.XPATH, "//tr[@class='even']//a[@class='btn btn-orange btn-outline btn-xl page-scroll download-button'][normalize-space()='Download sample DOC file']").click()
