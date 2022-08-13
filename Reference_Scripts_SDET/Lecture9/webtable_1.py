# 1. Count the number of rows and columns
# 2. Read specific row and coulumn
# 3. Read all the rows and columns
# 4. Read data based on condotions (Lists books names whose author is Mukesh)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chrome_102/chromedriver")
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1. Count the number of rows and columns

no_of_rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
no_of_columns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr[1]/th"))

print(no_of_rows)  # 7
print(no_of_columns)  # 4

# 2. Read specific row and coulumn
# Reading data of 5th row and first column
# spec_row_col_data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
# print(spec_row_col_data)  # Master In Selenium

# 3. Read all the rows and columns
# for r in range(2, no_of_rows+1):
#     for c in range(1, no_of_columns+1):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data, end='   ')
#     print()



# 4. Read data based on condotions (Lists books names whose author is Mukesh)
for r in range(2, no_of_rows+1):
    authhor_name = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authhor_name == "Mukesh":
        book_name = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(book_name, "   ", authhor_name, "    ", price)

driver.close()