from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("/home/prashant/Documents/Browser_Driver/chromedriver")
driver = webdriver.Chrome(service=ser_obj)
url = "https://money.rediff.com/gainers/bse/daily/groupa"
driver.get(url)

# self
# text_msg = driver.find_element(By.XPATH, "//a[normalize-space()='L&T']/self::a").text
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(), 'L&T Infotech')]/self::a").text
# print(text_msg) # L&T Infotech

# parent
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(), 'L&T Infotech')]/parent::td").text
# print(text_msg) # L&T Infotech

# child
# childs = driver.find_elements(By.XPATH, "//a[contains(text(), 'L&T Infotech')]/ancestor::tr/child::td")
# print(len(childs))


# ancestor
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(), 'L&T Infotech')]/ancestor::tr").text
# print(text_msg) # L&T Infotech A 4,043.80 4,070.15 + 0.65

#decendant
# decendants = driver.find_elements(By.XPATH, "//a[contains(text(), 'L&T Infotech')]/ancestor::tr/descendant::*")
# print("Number of descendant nodes: ", len(decendants)) # 7

#following
# followings = driver.find_elements(By.XPATH, "//a[contains(text(), 'L&T Infotech')]/ancestor::tr/following::*")
# print(len(followings)) # 1275555

#following-siblings
# followings = driver.find_elements(By.XPATH, "//a[contains(text(), 'L&T Infotech')]/ancestor::tr/following-sibling::*")
# print(len(followings)) # 139

# precending
# precedings = driver.find_elements(By.XPATH, "//a[contains(text(), 'L&T Infotech')]/ancestor::tr/preceding::*")
# print(len(precedings)) # 1928

#preseding-siblings
precedings = driver.find_elements(By.XPATH, "//a[contains(text(), 'L&T Infotech')]/ancestor::tr/preceding-sibling::*")
print(len(precedings)) # 219


driver.close()