import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import mysql.connector

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
driver.implicitly_wait(10)

driver.get(
    "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

# insert, update, delete
try:
    con = mysql.connector.connect(host="localhost", port=3306, user="prashant", passwd="Prashantb07089@",
                                  database="pytsel")
    curs = con.cursor()  # create cursor
    curs.execute("select * FROM Caldata")  # execute query through cursor
    for row in curs:
        pric = row[0]
        rate_of_interest = row[1]
        per1 = row[2]
        per2 = row[3]
        freq = row[4]
        exp_mvalue = row[5]

        # PAssing data to application
        driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(pric)
        driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rate_of_interest)
        driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(per1)

        period_drp = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
        period_drp.select_by_visible_text(per2)

        frequency_drp = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
        frequency_drp.select_by_visible_text(freq)
        # driver.find_element(By.XPATH, "//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']").click()
        cal_btn = driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img")  # calculate button
        driver.execute_script("arguments[0].click();", cal_btn)
        act_mvalue = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

        # validation
        if float(exp_mvalue) == float(act_mvalue):
            print("Test Passed")
        else:
            print("Test Failed")
        clear_btn = driver.find_element(By.XPATH, "//img[@class='PL5']")
        driver.execute_script("arguments[0].click();", clear_btn)
        time.sleep(2)
except:
    print("Connection Unsuccessful")

driver.close()
