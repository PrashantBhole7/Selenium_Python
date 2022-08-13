from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
url = "https://theautomationzone.blogspot.com/2020/07/xpath-practice.html"
driver.get(url)

# printing web element text in order
print(driver.find_element(By.XPATH, "//p[@id='id1']").text)
print(driver.find_element(By.XPATH, "//p[text()='unique id']").text)
print(driver.find_element(By.XPATH, "//p[text()='unique id' and @id='id1']").text)
print(driver.find_element(By.XPATH, "//p[@name='name1']").text)
print(driver.find_element(By.XPATH, "//p[@value='value1']").text)
print(driver.find_element(By.XPATH, "//p[@class='class1']").text)
print(driver.find_element(By.XPATH, "//div[@class='class1']").text)
print(driver.find_element(By.XPATH, "//p[@name='a' and @id='a']").text)
print(driver.find_element(By.XPATH, "//p[@name='a' and @id='b']").text)
print(driver.find_element(By.XPATH, "//p[@name='b' and @id='a']").text)
print(driver.find_element(By.XPATH, "//p[@name='b' and @id='b']").text)

# locate parent tag when child is unique
print(driver.find_element(By.XPATH, "//span[@id='link']/..").text)
# Above xpath can be writeen as below one tag in another tag
print(driver.find_element(By.XPATH, "//a[ span[@id='link']]").text)

# locate child tag when parent tag is unique
driver.find_element(By.XPATH, "//div[@id='divA']/input")

# locate grand-child tag when grand-fatehr tag is unique
driver.find_element(By.XPATH, "//div[@id='divC']/span/input")
driver.find_element(By.XPATH, "//div[@id='divC']//input")

# use of indexes
print(driver.find_element(By.XPATH, "//p[@name='a'][1]").text)
print(driver.find_element(By.XPATH, "//p[@name='a'][2]").text)

# here normal indexes is not applicable means it is not giving unique element
print(driver.find_element(By.XPATH, "//label[@id='lable'][1]").text)
print(driver.find_element(By.XPATH, "//label[@id='lable'][1]").text)

# corrected indexes as below
print(driver.find_element(By.XPATH, "(//label[@id='lable'])[1]").text)

print(driver.find_element(By.XPATH, "(//label[@id='lable'])[1]").text)

# contains method
# print(driver.find_element(By.XPATH, "//p[ contains(text(), 'logged in successfully')]").text)
# print(driver.find_element(By.XPATH, "//p[contains(@id, 'd1')]").text)
# print(driver.find_element(By.XPATH, "//p[contains(@id, 'd1') and text()='unique id']").text)
# print(driver.find_element(By.XPATH, "//p[starts-with( text(), 'logged in successfully')]").text)

# Here text Tommy is located even though we added spaced before and after and both
# print(driver.find_element(By.XPATH, "//p[normalize-space(text())='Tommy']").text)
# print(driver.find_element(By.XPATH, "//p[normalize-space( )='Tommy']").text)
print(driver.find_element(By.XPATH, "//p[normalize-space(@name )='aa']").text)

# case in-sensetive inner text
driver.find_element(By.XPATH, "//button[text()='lower case']").click()
print(driver.find_element(By.XPATH,
                          "//p[translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz' )='tommy']").text)



url = "https://theautomationzone.blogspot.com/2020/07/sample-webtable-3.html"
driver.get(url)
# locating whole table
print(driver.find_element(By.XPATH, "//table[@id='table1']").text)
print(driver.find_element(By.XPATH, "//table[count(.//tr)=8 and @id='table1']").text)

# locating first row of thr table
print(driver.find_element(By.XPATH, "//table[@id='table1']//tr[1]").text)
print(driver.find_element(By.XPATH, "//table[@id='table1']//tr[2]/td[2]").text)
driver.find_element(By.XPATH, "//table[@id= 'table1']//tr[2]/td[1]/input").click()
driver.find_element(By.XPATH, "//table[@id= 'table1']//tr[2]/td[1]/child::input").click()
print(driver.find_element(By.XPATH, "//table[@id='table1']//tr[3]").text)
print(driver.find_element(By.XPATH, "//table[@id='table1']//tr[5]").text)

# for locating row we can also used position function
print(driver.find_element(By.XPATH, "//table[@id='table1']//tr[position()=4]").text)
# For locating last row we can use last() function
print(driver.find_element(By.XPATH, "//table[@id='table1']//tr[last()]").text)
#   locating check box in a table
print(driver.find_element(By.XPATH, "//table[@id='table1']//tr[last()]/td/input").text)
print(driver.find_element(By.XPATH, "//table[@id='table1']//tr[last() -1]/td/input").text)
print(driver.find_element(By.XPATH, "//table[@id='table1']//tr[1+2]/td/input").text)

# back to url: https://theautomationzone.blogspot.com/2020/07/xpath-practice.html
